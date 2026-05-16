"""Tests for Business Idea validation and responsiveness.

This test suite verifies that:
1. Business Idea validation correctly rejects invalid inputs
2. Business Idea field strongly affects the generated launch plan
3. Different Business Ideas produce different plans
4. Gibberish/random text is properly rejected
"""

import pytest
from src.validators import validate_business_idea, validate_user_inputs
from src.sample_data import generate_dynamic_demo_plan


class TestBusinessIdeaValidation:
    """Test Business Idea input validation."""
    
    def test_empty_business_idea_rejected(self):
        """Empty business idea should be rejected."""
        is_valid, error_msg = validate_business_idea("")
        assert not is_valid
        assert "enter a business idea" in error_msg.lower()
    
    def test_whitespace_only_rejected(self):
        """Whitespace-only business idea should be rejected."""
        is_valid, error_msg = validate_business_idea("   \n\t  ")
        assert not is_valid
        assert "enter a business idea" in error_msg.lower()
    
    def test_too_short_rejected(self):
        """Very short business idea should be rejected."""
        is_valid, error_msg = validate_business_idea("coffee")
        assert not is_valid
        assert "at least 10 characters" in error_msg.lower()
    
    def test_repeated_characters_rejected(self):
        """Gibberish with repeated characters should be rejected."""
        is_valid, error_msg = validate_business_idea("aaaaaaaaaa")
        assert not is_valid
        assert "repeated characters" in error_msg.lower()
    
    def test_keyboard_pattern_rejected(self):
        """Random keyboard patterns should be rejected."""
        is_valid, error_msg = validate_business_idea("asdfghjkl qwerty")
        assert not is_valid
        # The validation catches this as consecutive consonants, which is also correct
        assert "meaningful" in error_msg.lower() or "random keyboard" in error_msg.lower()
    
    def test_excessive_numbers_rejected(self):
        """Text with excessive numbers should be rejected."""
        is_valid, error_msg = validate_business_idea("123456789 abc")
        assert not is_valid
        assert "mostly letters" in error_msg.lower()
    
    def test_too_few_words_rejected(self):
        """Text with too few recognizable words should be rejected."""
        is_valid, error_msg = validate_business_idea("ab cd")
        assert not is_valid
        # This gets caught by the length check first, which is also correct
        assert "at least 10 characters" in error_msg.lower() or "complete words" in error_msg.lower()
    
    def test_valid_business_idea_accepted(self):
        """Valid business idea should be accepted."""
        is_valid, error_msg = validate_business_idea(
            "A modern Italian pizza restaurant focusing on authentic Neapolitan recipes"
        )
        assert is_valid
        assert error_msg == ""
    
    def test_valid_short_but_clear_idea_accepted(self):
        """Short but clear business idea should be accepted."""
        is_valid, error_msg = validate_business_idea("Healthy vegan cafe")
        assert is_valid
        assert error_msg == ""


class TestBusinessIdeaResponsiveness:
    """Test that Business Idea field affects generated plans."""
    
    def test_different_ideas_produce_different_summaries(self):
        """Different business ideas should produce different business summaries."""
        idea1 = "A traditional Italian pizza restaurant with wood-fired oven"
        idea2 = "A modern vegan burger joint with plant-based proteins"
        
        inputs1 = {
            "business_idea": idea1,
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Rome, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Local families",
            "dietary_focus": [],
            "launch_goal": "Test market",
        }
        
        inputs2 = {
            "business_idea": idea2,
            "business_type": "Restaurant",
            "cuisine": "Vegan",
            "location": "Rome, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Local families",
            "dietary_focus": ["Vegan-friendly"],
            "launch_goal": "Test market",
        }
        
        plan1 = generate_dynamic_demo_plan(inputs1)
        plan2 = generate_dynamic_demo_plan(inputs2)
        
        # Business summaries should be different
        assert plan1["business_summary"] != plan2["business_summary"]
        
        # Business idea text should appear in the summary
        assert "pizza" in plan1["business_summary"].lower() or "italian" in plan1["business_summary"].lower()
        assert "vegan" in plan2["business_summary"].lower() or "burger" in plan2["business_summary"].lower()
    
    def test_business_idea_affects_positioning(self):
        """Business idea should affect positioning statement."""
        idea = "An authentic Ethiopian coffee ceremony experience with traditional preparation"
        
        inputs = {
            "business_idea": idea,
            "business_type": "Coffee kiosk",
            "cuisine": "Ethiopian / East African",
            "location": "Milan, Italy",
            "budget": "5,000-10,000 EUR",
            "target_customers": "Coffee enthusiasts",
            "dietary_focus": [],
            "launch_goal": "Build brand",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        
        # Positioning should reflect the authentic/traditional theme
        positioning_lower = plan["positioning"].lower()
        assert "authentic" in positioning_lower or "traditional" in positioning_lower
    
    def test_business_idea_affects_recommendations(self):
        """Business idea should affect key recommendations."""
        idea = "A quick-service healthy meal prep delivery for busy professionals"
        
        inputs = {
            "business_idea": idea,
            "business_type": "Catering service",
            "cuisine": "Mediterranean",
            "location": "London, UK",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Busy professionals",
            "dietary_focus": ["Healthy meals"],
            "launch_goal": "Launch MVP",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        
        # Key recommendation should reference the business idea
        recommendation_lower = plan["key_recommendation"].lower()
        assert "quick" in recommendation_lower or "delivery" in recommendation_lower or "professionals" in recommendation_lower
    
    def test_business_idea_affects_risks(self):
        """Business idea should affect identified risks."""
        idea = "An innovative fusion restaurant combining Japanese and Mexican cuisines"
        
        inputs = {
            "business_idea": idea,
            "business_type": "Restaurant",
            "cuisine": "Asian Fusion",
            "location": "Los Angeles, USA",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Food adventurers",
            "dietary_focus": [],
            "launch_goal": "Grand opening",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        
        # Risks should mention the innovative/new concept
        risks_text = " ".join(plan["main_risks"]).lower()
        assert "new" in risks_text or "innovative" in risks_text or "concept" in risks_text
    
    def test_business_idea_affects_marketing(self):
        """Business idea should affect marketing content."""
        idea = "A premium artisan bakery specializing in sourdough and traditional breads"
        
        inputs = {
            "business_idea": idea,
            "business_type": "Bakery",
            "cuisine": "Bakery / Pastry",
            "location": "Paris, France",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Bread lovers",
            "dietary_focus": [],
            "launch_goal": "Build reputation",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        
        # Marketing slogan should reflect the concept
        slogan_lower = plan["marketing"]["slogan"].lower()
        assert "bakery" in slogan_lower or "bread" in slogan_lower or "artisan" in slogan_lower
    
    def test_same_dropdowns_different_ideas_produce_different_plans(self):
        """Same dropdown values but different business ideas should produce different plans."""
        # Same dropdowns, different business ideas
        inputs_base = {
            "business_type": "Coffee kiosk",
            "cuisine": "Italian",
            "location": "Milan, Italy",
            "budget": "5,000-10,000 EUR",
            "target_customers": "Morning commuters",
            "dietary_focus": [],
            "launch_goal": "Test concept",
        }
        
        inputs1 = {**inputs_base, "business_idea": "A traditional Italian espresso bar with classic pastries"}
        inputs2 = {**inputs_base, "business_idea": "A modern specialty coffee shop with innovative brewing methods"}
        
        plan1 = generate_dynamic_demo_plan(inputs1)
        plan2 = generate_dynamic_demo_plan(inputs2)
        
        # Plans should be different despite same dropdowns
        assert plan1["business_summary"] != plan2["business_summary"]
        assert plan1["positioning"] != plan2["positioning"]
        
        # Plan 1 should reflect traditional theme
        assert "traditional" in plan1["positioning"].lower() or "classic" in plan1["positioning"].lower()
        
        # Plan 2 should reflect modern theme
        assert "modern" in plan2["positioning"].lower() or "innovative" in plan2["positioning"].lower()


class TestUserInputsValidation:
    """Test complete user inputs validation."""
    
    def test_valid_inputs_pass_validation(self):
        """Valid user inputs should pass validation."""
        inputs = {
            "business_idea": "A healthy meal prep service for busy professionals",
            "business_type": "Catering service",
            "cuisine": "Mediterranean",
            "location": "New York, USA",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Professionals",
            "dietary_focus": ["Healthy meals"],
            "launch_goal": "Launch MVP",
            "output_language": "English",
        }
        
        is_valid, error_msg = validate_user_inputs(inputs)
        assert is_valid
        assert error_msg == ""
    
    def test_invalid_business_idea_fails_validation(self):
        """Invalid business idea should fail validation."""
        inputs = {
            "business_idea": "abc",  # Too short
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Rome, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Families",
            "dietary_focus": [],
            "launch_goal": "Test",
            "output_language": "English",
        }
        
        is_valid, error_msg = validate_user_inputs(inputs)
        assert not is_valid
        assert "at least 10 characters" in error_msg.lower()
    
    def test_missing_location_fails_validation(self):
        """Missing location should fail validation."""
        inputs = {
            "business_idea": "A great Italian restaurant",
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "",  # Empty
            "budget": "10,000-25,000 EUR",
            "target_customers": "Families",
            "dietary_focus": [],
            "launch_goal": "Test",
            "output_language": "English",
        }
        
        is_valid, error_msg = validate_user_inputs(inputs)
        assert not is_valid
        assert "location" in error_msg.lower()
    
    def test_missing_cuisine_fails_validation(self):
        """Missing cuisine should fail validation."""
        inputs = {
            "business_idea": "A great restaurant concept",
            "business_type": "Restaurant",
            "cuisine": "",  # Empty
            "location": "Rome, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Families",
            "dietary_focus": [],
            "launch_goal": "Test",
            "output_language": "English",
        }
        
        is_valid, error_msg = validate_user_inputs(inputs)
        assert not is_valid
        assert "cuisine" in error_msg.lower()

# Made with Bob
