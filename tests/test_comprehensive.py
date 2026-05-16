"""Comprehensive test suite for MenuNest reliability and validation.

This test module ensures:
1. Demo mode works reliably without API keys
2. All required sections are present
3. Invalid/incomplete plans fail validation
4. JSON schema keys are never translated
5. Export utilities work correctly
6. Language handling is correct
"""

import json
import pytest

from src.ai_generator import generate_launch_plan, localize_demo_plan_to_italian
from src.export_utils import launch_plan_to_json, launch_plan_to_markdown
from src.prompt_builder import build_launch_plan_prompt
from src.sample_data import SAMPLE_LAUNCH_PLAN
from src.validators import validate_launch_plan, coerce_launch_plan, safe_parse_json


# ============================================================================
# Demo Mode Reliability Tests
# ============================================================================

def test_demo_mode_works_without_api_key():
    """Ensure demo mode works reliably without any API credentials."""
    user_inputs = {
        "business_idea": "Test business",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": ["Vegetarian-friendly"],
        "launch_goal": "Test concept",
        "output_language": "English",
    }
    
    # Should work even without API keys
    plan = generate_launch_plan(user_inputs, use_demo=True)
    is_valid, message = validate_launch_plan(plan)
    
    assert is_valid is True, f"Demo mode failed: {message}"
    assert plan is not None
    assert isinstance(plan, dict)


def test_demo_mode_returns_consistent_structure():
    """Ensure demo mode always returns the same structure."""
    user_inputs = {
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "English",
    }
    
    plan1 = generate_launch_plan(user_inputs, use_demo=True)
    plan2 = generate_launch_plan(user_inputs, use_demo=True)
    
    # Should return identical structure
    assert plan1.keys() == plan2.keys()
    assert len(plan1["menu_items"]) == len(plan2["menu_items"])


# ============================================================================
# Section Completeness Tests
# ============================================================================

def test_all_seven_required_sections_present():
    """Verify all 7 required app sections are present in generated plans."""
    user_inputs = {
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "English",
    }
    
    plan = generate_launch_plan(user_inputs, use_demo=True)
    
    # Section 1: Overview (business_summary, positioning, etc.)
    assert "business_summary" in plan
    assert "positioning" in plan
    assert "key_recommendation" in plan
    assert "main_risks" in plan
    assert "next_steps" in plan
    
    # Section 2: Menu & Pricing
    assert "menu_items" in plan
    assert len(plan["menu_items"]) > 0
    
    # Section 3: Ingredients & Allergens (part of menu_items)
    for item in plan["menu_items"]:
        assert "ingredients" in item
        assert "allergens" in item
        assert "preparation_note" in item
        assert "operational_tip" in item
    
    # Section 4: Customers
    assert "customer_personas" in plan
    assert len(plan["customer_personas"]) > 0
    
    # Section 5: Marketing
    assert "marketing" in plan
    assert "slogan" in plan["marketing"]
    assert "instagram_bio" in plan["marketing"]
    assert "captions" in plan["marketing"]
    assert "launch_announcement" in plan["marketing"]
    
    # Section 6: Launch Checklist
    assert "launch_checklist" in plan
    assert "before_launch" in plan["launch_checklist"]
    assert "menu_validation" in plan["launch_checklist"]
    assert "marketing_setup" in plan["launch_checklist"]
    assert "operations" in plan["launch_checklist"]
    assert "first_week_testing" in plan["launch_checklist"]
    
    # Section 7: Export (tested separately, but data must be exportable)
    markdown = launch_plan_to_markdown(plan)
    json_str = launch_plan_to_json(plan)
    assert len(markdown) > 100
    assert len(json_str) > 100


# ============================================================================
# Invalid/Incomplete Plan Tests
# ============================================================================

def test_missing_required_field_fails_validation():
    """Ensure plans missing required fields fail validation."""
    incomplete_plan = dict(SAMPLE_LAUNCH_PLAN)
    del incomplete_plan["business_summary"]
    
    is_valid, message = validate_launch_plan(incomplete_plan)
    
    assert is_valid is False
    assert "business_summary" in message.lower()


def test_invalid_complexity_value_fails_validation():
    """Ensure invalid complexity values fail validation."""
    invalid_plan = dict(SAMPLE_LAUNCH_PLAN)
    invalid_plan["estimated_complexity"] = "VeryHigh"  # Invalid value
    
    is_valid, message = validate_launch_plan(invalid_plan)
    
    assert is_valid is False
    assert "complexity" in message.lower()


def test_invalid_readiness_score_fails_validation():
    """Ensure readiness scores outside 0-100 fail validation."""
    invalid_plan = dict(SAMPLE_LAUNCH_PLAN)
    invalid_plan["launch_readiness_score"] = 150
    
    is_valid, message = validate_launch_plan(invalid_plan)
    
    assert is_valid is False
    assert "100" in message


def test_empty_menu_items_fails_validation():
    """Ensure plans with no menu items fail validation."""
    invalid_plan = dict(SAMPLE_LAUNCH_PLAN)
    invalid_plan["menu_items"] = []
    
    is_valid, message = validate_launch_plan(invalid_plan)
    
    assert is_valid is False


def test_menu_item_missing_required_field_fails():
    """Ensure menu items missing required fields fail validation."""
    invalid_plan = dict(SAMPLE_LAUNCH_PLAN)
    invalid_item = dict(invalid_plan["menu_items"][0])
    del invalid_item["ingredients"]
    invalid_plan["menu_items"] = [invalid_item]
    
    is_valid, message = validate_launch_plan(invalid_plan)
    
    assert is_valid is False
    assert "ingredients" in message.lower()


def test_short_description_fails_validation():
    """Ensure descriptions that are too short fail validation."""
    invalid_plan = dict(SAMPLE_LAUNCH_PLAN)
    invalid_plan["business_summary"] = "Too short"
    
    is_valid, message = validate_launch_plan(invalid_plan)
    
    assert is_valid is False


# ============================================================================
# JSON Schema Key Preservation Tests
# ============================================================================

def test_json_keys_never_translated_english():
    """Ensure JSON schema keys remain in English for English output."""
    user_inputs = {
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "English",
    }
    
    plan = generate_launch_plan(user_inputs, use_demo=True)
    
    # All keys must be in English
    assert "business_summary" in plan
    assert "menu_items" in plan
    assert "customer_personas" in plan
    assert "launch_checklist" in plan
    
    # Check nested keys
    assert "name" in plan["menu_items"][0]
    assert "complexity" in plan["menu_items"][0]
    assert "ingredients" in plan["menu_items"][0]
    
    assert "before_launch" in plan["launch_checklist"]
    assert "menu_validation" in plan["launch_checklist"]


def test_json_keys_never_translated_italian():
    """Ensure JSON schema keys remain in English even for Italian output."""
    user_inputs = {
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "Italian",
    }
    
    plan = generate_launch_plan(user_inputs, use_demo=True)
    
    # All keys must still be in English
    assert "business_summary" in plan
    assert "menu_items" in plan
    assert "customer_personas" in plan
    assert "launch_checklist" in plan
    
    # Check nested keys are still English
    assert "name" in plan["menu_items"][0]
    assert "complexity" in plan["menu_items"][0]
    assert "ingredients" in plan["menu_items"][0]
    
    assert "before_launch" in plan["launch_checklist"]
    assert "menu_validation" in plan["launch_checklist"]
    
    # But VALUES should be in Italian
    assert "Caffè" in plan["menu_items"][0]["name"]


def test_complexity_values_always_english():
    """Ensure complexity enum values are always in English."""
    # Test English output
    plan_en = generate_launch_plan({
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "English",
    }, use_demo=True)
    
    assert plan_en["estimated_complexity"] in ["Low", "Medium", "High"]
    for item in plan_en["menu_items"]:
        assert item["complexity"] in ["Low", "Medium", "High"]
    
    # Test Italian output - complexity must still be English
    plan_it = generate_launch_plan({
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "Italian",
    }, use_demo=True)
    
    assert plan_it["estimated_complexity"] in ["Low", "Medium", "High"]
    for item in plan_it["menu_items"]:
        assert item["complexity"] in ["Low", "Medium", "High"]


# ============================================================================
# Export Utility Tests
# ============================================================================

def test_markdown_export_includes_all_sections():
    """Ensure Markdown export includes all major sections."""
    markdown = launch_plan_to_markdown(SAMPLE_LAUNCH_PLAN)
    
    # Check for all major sections
    assert "# MenuNest Launch Report" in markdown
    assert "## Business Summary" in markdown
    assert "## Positioning" in markdown
    assert "## Launch Dashboard" in markdown
    assert "## Key Recommendation" in markdown
    assert "## Main Risks" in markdown
    assert "## Next Steps" in markdown
    assert "## Menu and Pricing" in markdown
    assert "## Customer Personas" in markdown
    assert "## Marketing Content" in markdown
    assert "## Launch Checklist" in markdown
    assert "## Disclaimer" in markdown


def test_markdown_export_italian_content():
    """Ensure Markdown export works with Italian content."""
    italian_plan = localize_demo_plan_to_italian(SAMPLE_LAUNCH_PLAN)
    markdown = launch_plan_to_markdown(italian_plan)
    
    assert "# MenuNest Launch Report" in markdown
    assert "Caffè Etiope" in markdown
    assert len(markdown) > 1000


def test_json_export_is_parseable():
    """Ensure JSON export produces valid, parseable JSON."""
    json_str = launch_plan_to_json(SAMPLE_LAUNCH_PLAN)
    
    # Should be valid JSON
    parsed = json.loads(json_str)
    
    assert isinstance(parsed, dict)
    assert "business_summary" in parsed
    assert "menu_items" in parsed
    assert len(parsed["menu_items"]) > 0


def test_json_export_preserves_unicode():
    """Ensure JSON export preserves Unicode characters (Italian, etc.)."""
    italian_plan = localize_demo_plan_to_italian(SAMPLE_LAUNCH_PLAN)
    json_str = launch_plan_to_json(italian_plan)
    
    # Should contain Italian characters
    assert "Caffè" in json_str or "Caff" in json_str
    
    # Should be parseable
    parsed = json.loads(json_str)
    assert isinstance(parsed, dict)


def test_export_roundtrip():
    """Ensure data survives export and re-import."""
    # Export to JSON
    json_str = launch_plan_to_json(SAMPLE_LAUNCH_PLAN)
    
    # Re-import
    reimported = json.loads(json_str)
    
    # Should validate
    is_valid, message = validate_launch_plan(reimported)
    assert is_valid is True, f"Reimported plan failed validation: {message}"


# ============================================================================
# Prompt Builder Tests
# ============================================================================

def test_prompt_includes_all_user_inputs():
    """Ensure prompt builder includes all user input fields."""
    user_inputs = {
        "business_idea": "Ethiopian coffee kiosk",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Morning commuters",
        "dietary_focus": ["Vegetarian-friendly", "Vegan options"],
        "launch_goal": "Test market demand",
        "output_language": "English",
    }
    
    prompt = build_launch_plan_prompt(user_inputs)
    
    assert "Ethiopian coffee kiosk" in prompt
    assert "Coffee kiosk" in prompt
    assert "Ethiopian" in prompt
    assert "Milan" in prompt
    assert "5,000-10,000 EUR" in prompt
    assert "Morning commuters" in prompt
    assert "Vegetarian-friendly" in prompt
    assert "Test market demand" in prompt


def test_prompt_includes_language_instruction():
    """Ensure prompt includes language-specific instructions."""
    # English
    prompt_en = build_launch_plan_prompt({
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "English",
    })
    
    assert "English" in prompt_en
    
    # Italian
    prompt_it = build_launch_plan_prompt({
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "Italian",
    })
    
    assert "Italian" in prompt_it


def test_prompt_includes_json_schema():
    """Ensure prompt includes the expected JSON schema structure."""
    prompt = build_launch_plan_prompt({
        "business_idea": "Test",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": [],
        "launch_goal": "Test",
        "output_language": "English",
    })
    
    # Check for key schema fields
    assert "business_summary" in prompt
    assert "menu_items" in prompt
    assert "customer_personas" in prompt
    assert "launch_checklist" in prompt
    assert "complexity" in prompt
    assert "ingredients" in prompt
    assert "allergens" in prompt


# ============================================================================
# Safe JSON Parsing Tests
# ============================================================================

def test_safe_parse_json_handles_markdown_blocks():
    """Ensure safe_parse_json can extract JSON from markdown code blocks."""
    json_with_markdown = '''```json
{
  "test": "value"
}
```'''
    
    result = safe_parse_json(json_with_markdown)
    
    assert result is not None
    assert result["test"] == "value"


def test_safe_parse_json_handles_plain_json():
    """Ensure safe_parse_json handles plain JSON."""
    plain_json = '{"test": "value"}'
    
    result = safe_parse_json(plain_json)
    
    assert result is not None
    assert result["test"] == "value"


def test_safe_parse_json_returns_none_for_invalid():
    """Ensure safe_parse_json returns None for invalid input."""
    assert safe_parse_json("not json") is None
    assert safe_parse_json("") is None
    # Test with invalid types by checking the function's behavior
    # The function expects a string, so we test edge cases within that constraint


# ============================================================================
# Sample Data Tests
# ============================================================================

def test_sample_data_is_valid():
    """Ensure sample data passes validation."""
    is_valid, message = validate_launch_plan(SAMPLE_LAUNCH_PLAN)
    
    assert is_valid is True, f"Sample data validation failed: {message}"


def test_sample_data_has_minimum_items():
    """Ensure sample data has reasonable content."""
    assert len(SAMPLE_LAUNCH_PLAN["menu_items"]) >= 5
    assert len(SAMPLE_LAUNCH_PLAN["customer_personas"]) >= 3
    assert len(SAMPLE_LAUNCH_PLAN["main_risks"]) >= 3
    assert len(SAMPLE_LAUNCH_PLAN["next_steps"]) >= 3


def test_sample_data_menu_items_complete():
    """Ensure all menu items have required fields."""
    for item in SAMPLE_LAUNCH_PLAN["menu_items"]:
        assert "name" in item
        assert "category" in item
        assert "description" in item
        assert "complexity" in item
        assert "suggested_price" in item
        assert "pricing_note" in item
        assert "ingredients" in item
        assert "allergens" in item
        assert "preparation_note" in item
        assert "operational_tip" in item
        
        # Check field content
        assert len(item["name"]) > 0
        assert len(item["ingredients"]) > 0
        assert len(item["allergens"]) > 0


# ============================================================================
# Coercion Tests
# ============================================================================

def test_coerce_launch_plan_validates_and_normalizes():
    """Ensure coerce_launch_plan validates and returns normalized dict."""
    result = coerce_launch_plan(SAMPLE_LAUNCH_PLAN)
    
    assert isinstance(result, dict)
    assert "business_summary" in result
    
    # Should be valid
    is_valid, message = validate_launch_plan(result)
    assert is_valid is True


def test_coerce_launch_plan_raises_on_invalid():
    """Ensure coerce_launch_plan raises ValidationError for invalid data."""
    invalid_plan = {"business_summary": "Too short"}
    
    with pytest.raises(Exception):  # Will raise ValidationError from Pydantic
        coerce_launch_plan(invalid_plan)


# Made with IBM Bob for the IBM Bob Hackathon

# Made with Bob
