from src.prompt_builder import build_launch_plan_prompt


def test_prompt_contains_user_inputs():
    prompt = build_launch_plan_prompt(
        {
            "business_idea": "Open an Ethiopian coffee kiosk",
            "business_type": "Coffee kiosk",
            "cuisine": "Ethiopian",
            "location": "Milan",
            "budget": "5,000-10,000 EUR",
            "target_customers": "Commuters",
            "dietary_focus": ["Vegetarian-friendly"],
            "launch_goal": "Test demand",
            "output_language": "English",
        }
    )

    assert "Open an Ethiopian coffee kiosk" in prompt
    assert "Coffee kiosk" in prompt
    assert "valid JSON" in prompt
    assert "menu_items" in prompt
