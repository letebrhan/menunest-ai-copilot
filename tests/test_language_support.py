"""Test language support for demo mode."""

from src.ai_generator import generate_launch_plan
from src.validators import validate_launch_plan


def test_demo_mode_english():
    """Test that demo mode works with English output."""
    user_inputs = {
        "business_idea": "Ethiopian coffee kiosk",
        "business_type": "Coffee kiosk",
        "cuisine": "Ethiopian",
        "location": "Milan",
        "budget": "5,000-10,000 EUR",
        "target_customers": "Commuters",
        "dietary_focus": ["Vegetarian-friendly"],
        "launch_goal": "Test concept",
        "output_language": "English",
    }
    
    plan = generate_launch_plan(user_inputs, use_demo=True)
    is_valid, message = validate_launch_plan(plan)
    
    assert is_valid is True, f"English demo plan validation failed: {message}"
    assert plan["estimated_complexity"] in ["Low", "Medium", "High"]
    assert len(plan["menu_items"]) >= 3
    assert all(item["complexity"] in ["Low", "Medium", "High"] for item in plan["menu_items"])


def test_demo_mode_italian():
    """Test that demo mode works with Italian output."""
    user_inputs = {
        "business_idea": "Chiosco di caffè etiope",
        "business_type": "Coffee kiosk",
        "cuisine": "Etiope",
        "location": "Milano",
        "budget": "5.000-10.000 EUR",
        "target_customers": "Pendolari",
        "dietary_focus": ["Vegetariano"],
        "launch_goal": "Testare il concetto",
        "output_language": "Italian",
    }
    
    plan = generate_launch_plan(user_inputs, use_demo=True)
    is_valid, message = validate_launch_plan(plan)
    
    assert is_valid is True, f"Italian demo plan validation failed: {message}"
    # Complexity values must remain in English for validation
    assert plan["estimated_complexity"] in ["Low", "Medium", "High"]
    assert len(plan["menu_items"]) >= 3
    assert all(item["complexity"] in ["Low", "Medium", "High"] for item in plan["menu_items"])
    # But user-facing text should be in Italian
    assert "Caffè" in plan["menu_items"][0]["name"]
    assert "Pendolari" in plan["best_customer_segment"]


def test_all_required_sections_present():
    """Test that all required sections are present in both languages."""
    required_keys = [
        "business_summary",
        "positioning",
        "launch_readiness_score",
        "estimated_complexity",
        "best_customer_segment",
        "key_recommendation",
        "main_risks",
        "next_steps",
        "menu_items",
        "customer_personas",
        "marketing",
        "launch_checklist",
    ]
    
    for language in ["English", "Italian"]:
        user_inputs = {
            "business_idea": "Test",
            "business_type": "Coffee kiosk",
            "cuisine": "Ethiopian",
            "location": "Milan",
            "budget": "5,000-10,000 EUR",
            "target_customers": "Commuters",
            "dietary_focus": [],
            "launch_goal": "Test",
            "output_language": language,
        }
        
        plan = generate_launch_plan(user_inputs, use_demo=True)
        
        for key in required_keys:
            assert key in plan, f"Missing key '{key}' in {language} output"
        
        # Check nested structures
        assert "slogan" in plan["marketing"]
        assert "instagram_bio" in plan["marketing"]
        assert "captions" in plan["marketing"]
        assert "launch_announcement" in plan["marketing"]
        
        assert "before_launch" in plan["launch_checklist"]
        assert "menu_validation" in plan["launch_checklist"]
        assert "marketing_setup" in plan["launch_checklist"]
        assert "operations" in plan["launch_checklist"]
        assert "first_week_testing" in plan["launch_checklist"]

# Made with Bob
