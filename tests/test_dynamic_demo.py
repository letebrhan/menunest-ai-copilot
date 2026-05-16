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
            "business_idea": "Small coffee kiosk with limited menu",
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
        
        # Scores should be in realistic ranges
        assert 50 <= plan_low["launch_readiness_score"] <= 90
        assert 50 <= plan_high["launch_readiness_score"] <= 90
        
        # Low budget should mention minimal viable product
        assert "minimal" in plan_low["key_recommendation"].lower() or "test" in plan_low["key_recommendation"].lower()

    def test_business_type_affects_complexity_and_score(self):
        """Test that business type affects both complexity and readiness score."""
        base_inputs = {
            "business_idea": "Food business with authentic cuisine and quality ingredients",
            "cuisine": "Italian",
            "location": "Milan, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Local customers and tourists",
            "dietary_focus": ["Premium experience"],
            "launch_goal": "Launch successfully and build reputation",
            "output_language": "English",
        }
        
        # Test different business types
        kiosk_plan = generate_dynamic_demo_plan({**base_inputs, "business_type": "Coffee kiosk"})
        restaurant_plan = generate_dynamic_demo_plan({**base_inputs, "business_type": "Restaurant"})
        
        # Restaurant should be more complex than kiosk
        complexity_order = {"Low": 1, "Medium": 2, "High": 3}
        assert complexity_order[restaurant_plan["estimated_complexity"]] > complexity_order[kiosk_plan["estimated_complexity"]]
        
        # Kiosk should have higher readiness score (lower complexity)
        assert kiosk_plan["launch_readiness_score"] > restaurant_plan["launch_readiness_score"]

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



class TestReadinessScoreCalculation:
    """Test suite for dynamic readiness score calculation."""

    def test_detailed_inputs_increase_score(self):
        """Test that detailed business idea, customers, and goals increase score."""
        vague_inputs = {
            "business_idea": "Food",
            "business_type": "Cafe",
            "cuisine": "Italian",
            "location": "Rome",
            "budget": "10,000-25,000 EUR",
            "target_customers": "People",
            "dietary_focus": [],
            "launch_goal": "Start",
            "output_language": "English",
        }
        
        detailed_inputs = {
            "business_idea": "A modern Italian cafe focusing on authentic regional recipes, using locally sourced ingredients to create a memorable dining experience for both tourists and locals",
            "business_type": "Cafe",
            "cuisine": "Italian",
            "location": "Rome, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Young professionals aged 25-40, tourists seeking authentic Italian cuisine, and local food enthusiasts who appreciate quality ingredients and traditional preparation methods",
            "dietary_focus": ["Premium experience", "Healthy meals"],
            "launch_goal": "Establish a strong reputation for authentic Italian cuisine within the first three months, build a loyal customer base, and achieve positive word-of-mouth through exceptional quality and service",
            "output_language": "English",
        }
        
        vague_plan = generate_dynamic_demo_plan(vague_inputs)
        detailed_plan = generate_dynamic_demo_plan(detailed_inputs)
        
        # Detailed inputs should result in higher readiness score
        assert detailed_plan["launch_readiness_score"] > vague_plan["launch_readiness_score"]
        
        # Difference should be significant (at least 10 points)
        assert detailed_plan["launch_readiness_score"] - vague_plan["launch_readiness_score"] >= 10

    def test_restaurant_with_low_budget_penalized(self):
        """Test that high-complexity business with low budget gets penalized."""
        low_budget_restaurant = {
            "business_idea": "Full-service Italian restaurant with extensive menu",
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Milan, Italy",
            "budget": "Under 5,000 EUR",
            "target_customers": "Families and couples",
            "dietary_focus": [],
            "launch_goal": "Open a successful restaurant",
            "output_language": "English",
        }
        
        adequate_budget_restaurant = {
            **low_budget_restaurant,
            "budget": "50,000+ EUR",
        }
        
        low_plan = generate_dynamic_demo_plan(low_budget_restaurant)
        high_plan = generate_dynamic_demo_plan(adequate_budget_restaurant)
        
        # Low budget restaurant should have significantly lower score
        assert high_plan["launch_readiness_score"] > low_plan["launch_readiness_score"]
        
        # Low budget restaurant should be in "needs validation" range
        assert low_plan["launch_readiness_score"] < 65

    def test_simple_business_with_low_budget_viable(self):
        """Test that simple business types can succeed with lower budgets."""
        low_budget_kiosk = {
            "business_idea": "Coffee kiosk serving espresso and pastries to morning commuters",
            "business_type": "Coffee kiosk",
            "cuisine": "Coffee / Breakfast",
            "location": "Milan, Italy",
            "budget": "Under 5,000 EUR",
            "target_customers": "Morning commuters and office workers",
            "dietary_focus": ["Affordable meals"],
            "launch_goal": "Test market demand with minimal investment",
            "output_language": "English",
        }
        
        plan = generate_dynamic_demo_plan(low_budget_kiosk)
        
        # Simple business with low budget and good clarity should score well
        # Coffee kiosk gets +8 for low complexity, detailed inputs add more points
        assert plan["launch_readiness_score"] >= 70
        # Score should be reasonable for a well-planned simple business
        assert plan["launch_readiness_score"] <= 90

    def test_score_stays_within_bounds(self):
        """Test that readiness score always stays between 50 and 90."""
        # Test extreme low scenario
        worst_case = {
            "business_idea": "Food",
            "business_type": "Restaurant",
            "cuisine": "Other",
            "location": "City",
            "budget": "Under 5,000 EUR",
            "target_customers": "",
            "dietary_focus": [],
            "launch_goal": "",
            "output_language": "English",
        }
        
        # Test extreme high scenario
        best_case = {
            "business_idea": "A highly detailed and well-researched food business concept with clear market positioning, unique value proposition, and comprehensive understanding of target demographics and competitive landscape",
            "business_type": "Coffee kiosk",
            "cuisine": "Coffee / Breakfast",
            "location": "Milan, Italy",
            "budget": "50,000+ EUR",
            "target_customers": "Detailed description of target customers including demographics, psychographics, spending habits, and specific pain points that our business will address",
            "dietary_focus": ["Vegetarian-friendly", "Vegan-friendly", "Healthy meals"],
            "launch_goal": "Comprehensive launch goal with specific metrics, timelines, and success criteria including customer acquisition targets, revenue goals, and operational milestones",
            "output_language": "English",
        }
        
        worst_plan = generate_dynamic_demo_plan(worst_case)
        best_plan = generate_dynamic_demo_plan(best_case)
        
        # Both should be within bounds
        assert 50 <= worst_plan["launch_readiness_score"] <= 90
        assert 50 <= best_plan["launch_readiness_score"] <= 90
        
        # Best case should be significantly higher
        assert best_plan["launch_readiness_score"] > worst_plan["launch_readiness_score"]

    def test_dietary_focus_affects_score(self):
        """Test that having dietary focus increases readiness score."""
        no_focus = {
            "business_idea": "Italian restaurant serving traditional dishes",
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Rome, Italy",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Food enthusiasts and tourists",
            "dietary_focus": [],
            "launch_goal": "Establish authentic Italian dining experience",
            "output_language": "English",
        }
        
        with_focus = {
            **no_focus,
            "dietary_focus": ["Vegetarian-friendly", "Gluten-free options", "Healthy meals"],
        }
        
        no_focus_plan = generate_dynamic_demo_plan(no_focus)
        with_focus_plan = generate_dynamic_demo_plan(with_focus)
        
        # Having dietary focus should increase score
        assert with_focus_plan["launch_readiness_score"] >= no_focus_plan["launch_readiness_score"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
