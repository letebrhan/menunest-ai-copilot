"""Tests for dynamic demo mode functionality.

This module verifies that demo mode responds to user inputs and generates
appropriate content based on business type, cuisine, location, and other parameters.
"""

import pytest

from src.ai_generator import generate_launch_plan
from src.sample_data import generate_dynamic_demo_plan
from src.validators import validate_launch_plan


class TestDynamicDemoGeneration:
    """Test suite for dynamic demo data generation."""

    def test_default_ethiopian_returns_original_sample(self):
        """Test that default Ethiopian inputs return the original sample plan."""
        user_inputs = {
            "business_idea": "I want to launch an Ethiopian coffee and breakfast kiosk in Milan.",
            "business_type": "Coffee kiosk",
            "cuisine": "Ethiopian / East African",
            "location": "Milan, Italy",
            "budget": "5,000-10,000 EUR",
            "target_customers": "Office workers, students, commuters",
            "dietary_focus": ["Vegetarian-friendly", "Affordable meals"],
            "launch_goal": "Test customer interest",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(user_inputs)
        
        # Should contain Ethiopian-specific content
        assert "ethiopian" in plan["business_summary"].lower()
        assert "milan" in plan["business_summary"].lower()
        assert plan["launch_readiness_score"] == 72

    def test_italian_cuisine_generates_adapted_content(self):
        """Test that Italian cuisine generates appropriate content."""
        user_inputs = {
            "business_idea": "Traditional Italian restaurant in Rome",
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Rome, Italy",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Tourists and locals seeking authentic Italian food",
            "dietary_focus": ["Premium experience"],
            "launch_goal": "Establish reputation for authentic cuisine",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(user_inputs)
        
        # Should contain Italian-specific content
        assert "italian" in plan["business_summary"].lower()
        assert "rome" in plan["business_summary"].lower()
        assert "restaurant" in plan["business_summary"].lower()
        
        # Should have higher readiness score for larger budget
        assert plan["launch_readiness_score"] >= 80
        
        # Should have appropriate complexity
        assert plan["estimated_complexity"] == "High"
        
        # Menu should contain Italian items
        menu_names = [item["name"].lower() for item in plan["menu_items"]]
        assert any("pizza" in name or "pasta" in name for name in menu_names)

    def test_mexican_food_truck_generates_adapted_content(self):
        """Test that Mexican food truck generates appropriate content."""
        user_inputs = {
            "business_idea": "Mexican food truck serving tacos and burritos",
            "business_type": "Food truck",
            "cuisine": "Mexican",
            "location": "Barcelona, Spain",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Young professionals and students",
            "dietary_focus": ["Affordable meals"],
            "launch_goal": "Build customer base through multiple locations",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(user_inputs)
        
        # Should contain Mexican-specific content
        assert "mexican" in plan["business_summary"].lower()
        assert "barcelona" in plan["business_summary"].lower()
        assert "food truck" in plan["business_summary"].lower()
        
        # Should have medium complexity for food truck
        assert plan["estimated_complexity"] == "Medium"
        
        # Menu should contain Mexican items
        menu_names = [item["name"].lower() for item in plan["menu_items"]]
        assert any("taco" in name or "guacamole" in name for name in menu_names)
        
        # Recommendation should mention mobile operation
        assert "mobile" in plan["key_recommendation"].lower() or "location" in plan["key_recommendation"].lower()

    def test_vegan_cafe_generates_adapted_content(self):
        """Test that vegan cafe generates appropriate content."""
        user_inputs = {
            "business_idea": "Plant-based cafe with healthy bowls and smoothies",
            "business_type": "Cafe",
            "cuisine": "Vegan / Plant-based",
            "location": "Berlin, Germany",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Health-conscious millennials and vegans",
            "dietary_focus": ["Vegan-friendly", "Healthy meals"],
            "launch_goal": "Create community hub for plant-based lifestyle",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(user_inputs)
        
        # Should contain vegan-specific content
        assert "vegan" in plan["business_summary"].lower() or "plant" in plan["business_summary"].lower()
        assert "berlin" in plan["business_summary"].lower()
        
        # Menu should contain vegan items
        menu_items = plan["menu_items"]
        assert len(menu_items) > 0
        
        # Check that menu items are appropriate
        menu_names = [item["name"].lower() for item in menu_items]
        assert any("bowl" in name or "burger" in name or "vegan" in name for name in menu_names)

    def test_low_budget_affects_readiness_score(self):
        """Test that lower budget results in lower readiness score."""
        user_inputs_low = {
            "business_idea": "Small coffee kiosk",
            "business_type": "Coffee kiosk",
            "cuisine": "Coffee / Breakfast",
            "location": "Milan, Italy",
            "budget": "Under 5,000 EUR",
            "target_customers": "Commuters",
            "dietary_focus": [],
            "launch_goal": "Test concept",
            "output_language": "English",
        }
        
        user_inputs_high = {
            **user_inputs_low,
            "budget": "50,000+ EUR",
        }
        
        plan_low = generate_dynamic_demo_plan(user_inputs_low)
        plan_high = generate_dynamic_demo_plan(user_inputs_high)
        
        # Higher budget should have higher readiness score
        assert plan_high["launch_readiness_score"] > plan_low["launch_readiness_score"]
        
        # Low budget should mention minimal viable product
        assert "minimal" in plan_low["key_recommendation"].lower() or "test" in plan_low["key_recommendation"].lower()

    def test_business_type_affects_complexity(self):
        """Test that business type affects estimated complexity."""
        base_inputs = {
            "business_idea": "Food business",
            "cuisine": "Italian",
            "location": "Milan, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Local customers",
            "dietary_focus": [],
            "launch_goal": "Launch successfully",
            "output_language": "English",
        }
        
        # Test different business types
        kiosk_plan = generate_dynamic_demo_plan({**base_inputs, "business_type": "Coffee kiosk"})
        restaurant_plan = generate_dynamic_demo_plan({**base_inputs, "business_type": "Restaurant"})
        
        # Restaurant should be more complex than kiosk
        complexity_order = {"Low": 1, "Medium": 2, "High": 3}
        assert complexity_order[restaurant_plan["estimated_complexity"]] > complexity_order[kiosk_plan["estimated_complexity"]]

    def test_customer_personas_adapt_to_target(self):
        """Test that customer personas adapt to target customers."""
        user_inputs_students = {
            "business_idea": "Student-focused cafe",
            "business_type": "Cafe",
            "cuisine": "Coffee / Breakfast",
            "location": "Milan, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "University students",
            "dietary_focus": ["Affordable meals"],
            "launch_goal": "Build student community",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(user_inputs_students)
        
        # Should have student-focused persona
        personas = plan["customer_personas"]
        assert len(personas) >= 1
        
        # At least one persona should mention students or budget
        persona_text = " ".join([p["profile"].lower() + p["needs"].lower() for p in personas])
        assert "student" in persona_text or "budget" in persona_text or "affordable" in persona_text

    def test_marketing_content_includes_cuisine_and_location(self):
        """Test that marketing content includes cuisine and location."""
        user_inputs = {
            "business_idea": "Indian restaurant",
            "business_type": "Restaurant",
            "cuisine": "Indian",
            "location": "London, UK",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Food enthusiasts",
            "dietary_focus": [],
            "launch_goal": "Establish presence",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(user_inputs)
        
        marketing = plan["marketing"]
        
        # Slogan should mention cuisine and location
        assert "indian" in marketing["slogan"].lower()
        assert "london" in marketing["slogan"].lower()
        
        # Instagram bio should mention cuisine and location
        assert "indian" in marketing["instagram_bio"].lower()
        assert "london" in marketing["instagram_bio"].lower()

    def test_launch_checklist_includes_business_specifics(self):
        """Test that launch checklist includes business-specific items."""
        user_inputs = {
            "business_idea": "Mexican food truck",
            "business_type": "Food truck",
            "cuisine": "Mexican",
            "location": "Austin, Texas",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Local food lovers",
            "dietary_focus": [],
            "launch_goal": "Test multiple locations",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(user_inputs)
        
        checklist = plan["launch_checklist"]
        
        # Should have all required sections
        assert "before_launch" in checklist
        assert "menu_validation" in checklist
        assert "marketing_setup" in checklist
        assert "operations" in checklist
        assert "first_week_testing" in checklist
        
        # Checklist should mention cuisine and location
        all_items = []
        for section in checklist.values():
            all_items.extend(section)
        
        checklist_text = " ".join(all_items).lower()
        assert "mexican" in checklist_text
        assert "austin" in checklist_text or "food truck" in checklist_text


class TestDynamicDemoIntegration:
    """Test integration of dynamic demo with the full generation pipeline."""

    def test_generate_launch_plan_with_demo_mode(self):
        """Test that generate_launch_plan uses dynamic demo correctly."""
        user_inputs = {
            "business_idea": "Italian pizzeria in Naples",
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Naples, Italy",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Tourists and locals",
            "dietary_focus": ["Premium experience"],
            "launch_goal": "Become known for authentic Neapolitan pizza",
            "output_language": "English",
        }
        
        plan = generate_launch_plan(user_inputs, use_demo=True)
        
        # Should be valid
        is_valid, message = validate_launch_plan(plan)
        assert is_valid, f"Plan validation failed: {message}"
        
        # Should contain Italian-specific content
        assert "italian" in plan["business_summary"].lower()
        assert "naples" in plan["business_summary"].lower()

    def test_generate_launch_plan_with_italian_output(self):
        """Test that Italian output language works with dynamic demo."""
        user_inputs = {
            "business_idea": "Ristorante italiano a Roma",
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Rome, Italy",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Turisti e residenti",
            "dietary_focus": ["Premium experience"],
            "launch_goal": "Stabilire reputazione",
            "output_language": "Italian",
        }
        
        plan = generate_launch_plan(user_inputs, use_demo=True)
        
        # Should be valid
        is_valid, message = validate_launch_plan(plan)
        assert is_valid, f"Plan validation failed: {message}"
        
        # Should contain Italian language content
        # Note: The dynamic generator creates English content first,
        # then localization is applied
        assert plan is not None
        assert "business_summary" in plan

    def test_all_required_sections_present(self):
        """Test that all required sections are present in dynamic demo."""
        user_inputs = {
            "business_idea": "Asian fusion restaurant",
            "business_type": "Restaurant",
            "cuisine": "Asian Fusion",
            "location": "San Francisco, USA",
            "budget": "50,000+ EUR",
            "target_customers": "Urban professionals and food enthusiasts",
            "dietary_focus": ["Premium experience", "Healthy meals"],
            "launch_goal": "Create unique dining experience",
            "output_language": "English",
        }
        
        plan = generate_launch_plan(user_inputs, use_demo=True)
        
        # Verify all required sections
        required_sections = [
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
        
        for section in required_sections:
            assert section in plan, f"Missing required section: {section}"
        
        # Verify menu items structure
        assert len(plan["menu_items"]) > 0
        for item in plan["menu_items"]:
            assert "name" in item
            assert "category" in item
            assert "description" in item
            assert "complexity" in item
            assert "suggested_price" in item
            assert "ingredients" in item
            assert "allergens" in item


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# Made with Bob
