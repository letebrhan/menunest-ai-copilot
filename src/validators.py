"""Validation helpers for generated launch plans."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, ValidationError


class MenuItem(BaseModel):
    name: str
    category: str
    description: str
    complexity: str
    suggested_price: str
    pricing_note: str
    ingredients: list[str]
    allergens: list[str]
    preparation_note: str
    operational_tip: str


class CustomerPersona(BaseModel):
    name: str
    profile: str
    needs: str
    recommended_offer: str
    marketing_angle: str


class MarketingContent(BaseModel):
    slogan: str
    instagram_bio: str
    captions: list[str] = Field(min_length=1)
    launch_announcement: str


class LaunchChecklist(BaseModel):
    before_launch: list[str]
    menu_validation: list[str]
    marketing_setup: list[str]
    operations: list[str]
    first_week_testing: list[str]


class LaunchPlan(BaseModel):
    business_summary: str
    positioning: str
    launch_readiness_score: int = Field(ge=0, le=100)
    estimated_complexity: str
    best_customer_segment: str
    key_recommendation: str
    main_risks: list[str]
    next_steps: list[str]
    menu_items: list[MenuItem] = Field(min_length=1)
    customer_personas: list[CustomerPersona] = Field(min_length=1)
    marketing: MarketingContent
    launch_checklist: LaunchChecklist


def validate_launch_plan(data: dict[str, Any]) -> tuple[bool, str]:
    """Return whether generated data matches the expected launch plan schema."""
    try:
        LaunchPlan.model_validate(data)
        return True, "Launch plan is valid."
    except ValidationError as exc:
        return False, str(exc)


def coerce_launch_plan(data: dict[str, Any]) -> dict[str, Any]:
    """Validate and return a normalized launch plan dictionary."""
    return LaunchPlan.model_validate(data).model_dump()
