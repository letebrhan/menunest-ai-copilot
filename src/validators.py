"""Validation helpers for generated launch plans.

This module provides robust JSON schema validation using Pydantic models
to ensure all generated launch plans meet the required structure and
data quality standards.
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, Field, ValidationError, validator


class MenuItem(BaseModel):
    """Menu item with pricing, ingredients, and operational guidance."""
    
    name: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=10, max_length=500)
    complexity: str
    suggested_price: str = Field(min_length=1, max_length=50)
    pricing_note: str = Field(min_length=5, max_length=300)
    ingredients: list[str] = Field(min_length=1)
    allergens: list[str] = Field(min_length=1)
    preparation_note: str = Field(min_length=5, max_length=500)
    operational_tip: str = Field(min_length=5, max_length=500)
    
    @validator("complexity")
    def validate_complexity(cls, v: str) -> str:
        """Ensure complexity is one of the allowed values."""
        allowed = {"Low", "Medium", "High"}
        if v not in allowed:
            raise ValueError(f"Complexity must be one of {allowed}, got '{v}'")
        return v
    
    @validator("ingredients", "allergens")
    def validate_string_lists(cls, v: list[str]) -> list[str]:
        """Ensure list items are non-empty strings."""
        if not all(isinstance(item, str) and item.strip() for item in v):
            raise ValueError("All list items must be non-empty strings")
        return v


class CustomerPersona(BaseModel):
    """Customer segment with needs and marketing strategy."""
    
    name: str = Field(min_length=1, max_length=100)
    profile: str = Field(min_length=10, max_length=500)
    needs: str = Field(min_length=5, max_length=500)
    recommended_offer: str = Field(min_length=5, max_length=300)
    marketing_angle: str = Field(min_length=5, max_length=500)


class MarketingContent(BaseModel):
    """Marketing copy and social media content."""
    
    slogan: str = Field(min_length=5, max_length=200)
    instagram_bio: str = Field(min_length=10, max_length=300)
    captions: list[str]
    launch_announcement: str = Field(min_length=20, max_length=1000)
    
    @validator("captions")
    def validate_captions(cls, v: list[str]) -> list[str]:
        """Ensure captions are meaningful."""
        if not all(isinstance(item, str) and len(item.strip()) >= 10 for item in v):
            raise ValueError("All captions must be at least 10 characters")
        return v


class LaunchChecklist(BaseModel):
    """Structured checklist for launch preparation."""
    
    before_launch: list[str]
    menu_validation: list[str]
    marketing_setup: list[str]
    operations: list[str]
    first_week_testing: list[str]
    
    @validator("before_launch", "menu_validation", "marketing_setup",
               "operations", "first_week_testing")
    def validate_checklist_items(cls, v: list[str]) -> list[str]:
        """Ensure checklist items are actionable."""
        if not all(isinstance(item, str) and len(item.strip()) >= 5 for item in v):
            raise ValueError("All checklist items must be at least 5 characters")
        return v


class LaunchPlan(BaseModel):
    """Complete launch plan with all required sections."""
    
    business_summary: str = Field(min_length=20, max_length=1000)
    positioning: str = Field(min_length=20, max_length=1000)
    launch_readiness_score: int = Field(ge=0, le=100)
    estimated_complexity: str
    best_customer_segment: str = Field(min_length=5, max_length=200)
    key_recommendation: str = Field(min_length=20, max_length=1000)
    main_risks: list[str]
    next_steps: list[str]
    menu_items: list[MenuItem]
    customer_personas: list[CustomerPersona]
    marketing: MarketingContent
    launch_checklist: LaunchChecklist
    
    @validator("estimated_complexity")
    def validate_complexity(cls, v: str) -> str:
        """Ensure complexity is one of the allowed values."""
        allowed = {"Low", "Medium", "High"}
        if v not in allowed:
            raise ValueError(f"Complexity must be one of {allowed}, got '{v}'")
        return v
    
    @validator("main_risks", "next_steps")
    def validate_string_lists(cls, v: list[str]) -> list[str]:
        """Ensure list items are meaningful."""
        if not all(isinstance(item, str) and len(item.strip()) >= 10 for item in v):
            raise ValueError("All list items must be at least 10 characters")
        return v


def validate_launch_plan(data: dict[str, Any]) -> tuple[bool, str]:
    """Validate that generated data matches the expected launch plan schema.
    
    Args:
        data: Dictionary containing the launch plan data
        
    Returns:
        Tuple of (is_valid, message) where message contains error details if invalid
    """
    try:
        LaunchPlan(**data)
        return True, "Launch plan is valid."
    except ValidationError as exc:
        # Format validation errors in a user-friendly way
        error_messages = []
        for error in exc.errors():
            field = " -> ".join(str(loc) for loc in error["loc"])
            msg = error["msg"]
            error_messages.append(f"  • {field}: {msg}")
        
        formatted_errors = "\n".join(error_messages)
        return False, f"Validation failed:\n{formatted_errors}"
    except Exception as exc:
        return False, f"Unexpected validation error: {str(exc)}"


def coerce_launch_plan(data: dict[str, Any]) -> dict[str, Any]:
    """Validate and return a normalized launch plan dictionary.
    
    This function ensures the data structure is valid and returns a clean
    dictionary representation suitable for rendering and export.
    
    Args:
        data: Dictionary containing the launch plan data
        
    Returns:
        Validated and normalized dictionary
        
    Raises:
        ValidationError: If the data doesn't match the schema
    """
    return LaunchPlan(**data).dict()


def safe_parse_json(raw_text: str) -> dict[str, Any] | None:
    """Safely parse JSON from LLM output, handling common formatting issues.
    
    This function attempts to extract and parse JSON from LLM responses that
    may include markdown code blocks or other formatting.
    
    Args:
        raw_text: Raw text response from LLM
        
    Returns:
        Parsed dictionary or None if parsing fails
    """
    if not raw_text or not isinstance(raw_text, str):
        return None
    
    # Remove common markdown code block markers
    text = raw_text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    
    if text.endswith("```"):
        text = text[:-3]
    
    text = text.strip()
    
    try:
        parsed = json.loads(text)
        if not isinstance(parsed, dict):
            return None
        return parsed
    except json.JSONDecodeError:
        return None
