"""Validation helpers for generated launch plans.

This module provides robust JSON schema validation using Pydantic models
to ensure all generated launch plans meet the required structure and
data quality standards.
"""

from __future__ import annotations

import json
import re
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
    def validate_estimated_complexity(cls, v: str) -> str:
        """Ensure complexity is one of the allowed values."""
        allowed = {"Low", "Medium", "High"}
        if v not in allowed:
            raise ValueError(f"Complexity must be one of {allowed}, got '{v}'")
        return v
    
    @validator("menu_items", "customer_personas")
    def validate_non_empty_lists(cls, v: list) -> list:
        """Ensure lists have at least one item."""
        if not v or len(v) == 0:
            raise ValueError("List must contain at least one item")
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
    return LaunchPlan(**data).model_dump()


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


def validate_business_idea(business_idea: str) -> tuple[bool, str]:
    """Validate that the business idea is clear and meaningful.
    
    This function checks for:
    - Empty or whitespace-only input
    - Very short input (less than 10 characters)
    - Gibberish or random text patterns
    - Non-food business text (math problems, school exercises, etc.)
    - Lack of food-related context (REQUIRED - must contain food/business keywords)
    
    Args:
        business_idea: The business idea text to validate
        
    Returns:
        Tuple of (is_valid, error_message) where error_message is empty if valid
    """
    if not business_idea or not business_idea.strip():
        return False, "Please enter a business idea. Describe your food business concept in 1-2 sentences."
    
    idea = business_idea.strip()
    
    # Check minimum length
    if len(idea) < 10:
        return False, "Please provide more details about your business idea (at least 10 characters)."
    
    # Check for gibberish patterns
    # 1. Too many repeated characters (e.g., "aaaaaaa", "123123123")
    if re.search(r'(.)\1{4,}', idea):
        return False, "Please enter a clear food business idea. The text appears to contain repeated characters."
    
    # 2. Too many consecutive consonants or vowels (gibberish indicator)
    if re.search(r'[bcdfghjklmnpqrstvwxyz]{7,}', idea.lower()):
        return False, "Please enter a clear food business idea. The text doesn't appear to be meaningful."
    
    # 3. Random keyboard patterns (e.g., "asdfghjkl", "qwertyuiop")
    keyboard_patterns = [
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm',
        'qwerty', 'asdfgh', 'zxcvb',
        '1234567890', '0987654321'
    ]
    idea_lower = idea.lower().replace(' ', '')
    for pattern in keyboard_patterns:
        if pattern in idea_lower or pattern[::-1] in idea_lower:
            return False, "Please enter a clear food business idea. The text appears to be random keyboard input."
    
    # 4. Check for excessive numbers or special characters (>50% of content)
    alphanumeric_chars = sum(c.isalnum() for c in idea)
    letter_chars = sum(c.isalpha() for c in idea)
    if alphanumeric_chars > 0 and letter_chars / alphanumeric_chars < 0.5:
        return False, "Please enter a clear food business idea using mostly letters and words."
    
    # 5. Check for at least some recognizable words (at least 2 words with 3+ letters)
    words = re.findall(r'\b[a-zA-Z]{3,}\b', idea)
    if len(words) < 2:
        return False, "Please describe your food business idea using complete words and sentences."
    
    # 6. Detect non-food business text patterns
    # Check for math problems, equations, or academic exercises
    math_patterns = [
        r'\d+\s*[\+\-\*\/\=]\s*\d+',  # Math operations like "2 + 2 = 4"
        r'\b(solve|calculate|equation|formula|theorem|proof)\b',
        r'\b(x|y|z)\s*[\+\-\*\/\=]',  # Algebraic variables
    ]
    for pattern in math_patterns:
        if re.search(pattern, idea.lower()):
            return False, "Please enter a food business idea, not a math problem or academic exercise. Example: 'I want to launch a bakery in Milan.'"
    
    # Check for obvious non-food topics
    non_food_indicators = [
        r'\b(homework|assignment|essay|report|thesis|dissertation)\b',
        r'\b(school|university|college|class|course|lecture)\b',
        r'\b(programming|code|software|algorithm|function|variable)\b',
        r'\b(physics|chemistry|biology|mathematics|geometry|algebra)\b',
        r'\b(history|geography|literature|poetry|novel|book)\b',
    ]
    for pattern in non_food_indicators:
        if re.search(pattern, idea.lower()):
            return False, "Please enter a food business idea. Example: 'I want to launch a bakery in Milan' or 'Ethiopian coffee kiosk for morning commuters.'"
    
    # 7. Check for food/business context (now a REQUIRED check)
    # This ensures the text is actually about food business
    food_business_keywords = [
        'food', 'restaurant', 'cafe', 'coffee', 'kitchen', 'chef', 'cook', 'meal',
        'breakfast', 'lunch', 'dinner', 'snack', 'drink', 'beverage', 'menu',
        'cuisine', 'dish', 'recipe', 'bakery', 'bar', 'grill', 'bistro', 'deli',
        'catering', 'truck', 'kiosk', 'stall', 'market', 'shop', 'store',
        'pizza', 'burger', 'sandwich', 'salad', 'soup', 'pasta', 'rice', 'bread',
        'vegan', 'vegetarian', 'organic', 'healthy', 'fresh', 'local', 'eat', 'eating',
        'serve', 'serving', 'offer', 'sell', 'selling', 'business', 'customers',
        'ethiopian', 'italian', 'mexican', 'indian', 'chinese', 'japanese', 'thai',
        'mediterranean', 'asian', 'american', 'french', 'greek', 'middle eastern',
        'launch', 'open', 'start', 'create', 'establish', 'run', 'operate',
        'dessert', 'sweet', 'savory', 'spicy', 'flavor', 'taste', 'delicious',
        'wine', 'beer', 'juice', 'smoothie', 'tea', 'espresso', 'latte',
    ]
    
    idea_lower_words = idea.lower().split()
    has_food_context = any(
        keyword in idea.lower() or
        any(keyword in word for word in idea_lower_words)
        for keyword in food_business_keywords
    )
    
    if not has_food_context:
        return False, (
            "Please enter a food business idea. Your text doesn't appear to describe a food or restaurant concept. "
            "Example: 'I want to launch a bakery in Milan' or 'Ethiopian coffee kiosk for morning commuters.'"
        )
    
    return True, ""


def validate_user_inputs(user_inputs: dict[str, Any]) -> tuple[bool, str]:
    """Validate user inputs before generating a launch plan.
    
    This function performs comprehensive validation of all user inputs
    to ensure they are suitable for generating a meaningful launch plan.
    
    Args:
        user_inputs: Dictionary containing all user form inputs
        
    Returns:
        Tuple of (is_valid, error_message) where error_message is empty if valid
    """
    # Validate business idea
    business_idea = user_inputs.get("business_idea", "")
    is_valid, error_msg = validate_business_idea(business_idea)
    if not is_valid:
        return False, error_msg
    
    # Validate other required fields
    location = user_inputs.get("location", "")
    if not location or not location.strip():
        return False, "Please provide a location for your business."
    
    cuisine = user_inputs.get("cuisine", "")
    if not cuisine or not cuisine.strip() or cuisine == "Other / Custom":
        return False, "Please specify a cuisine type."
    
    # All validations passed
    return True, ""
