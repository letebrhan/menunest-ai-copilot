"""Tests for enhanced business idea cleaning and validation.

This module tests the improved cleaning and validation logic that:
1. Removes personal introductions (I am [Name])
2. Removes request fillers (please help me, could you help me)
3. Normalizes common typos (resturan->restaurant, barkery->bakery)
4. Rejects non-food business text (math problems, school exercises)
5. Requires food/business context
"""

import pytest

from src.sample_data import clean_business_idea
from src.validators import validate_business_idea


class TestEnhancedBusinessIdeaCleaning:
    """Test enhanced cleaning of business idea text."""
    
    def test_removes_personal_introduction_i_am(self):
        """Should remove 'I am [Name]' introductions."""
        input_text = "I am Meaza. Please could you help me to prepare a business idea to launch a Restaurant in Milan"
        cleaned = clean_business_idea(input_text)
        
        assert "I am Meaza" not in cleaned
        assert "Meaza" not in cleaned
        assert "restaurant" in cleaned.lower()
        assert "Milan" in cleaned
    
    def test_removes_personal_introduction_my_name_is(self):
        """Should remove 'My name is [Name]' introductions."""
        input_text = "My name is John. I want to open a bakery in Rome"
        cleaned = clean_business_idea(input_text)
        
        assert "My name is" not in cleaned
        assert "John" not in cleaned
        assert "bakery" in cleaned.lower()
        assert "Rome" in cleaned
    
    def test_removes_request_filler_please_could_you_help_me(self):
        """Should remove 'please could you help me' request fillers."""
        input_text = "Please could you help me to prepare a business idea to launch a Restaurant in Milan"
        cleaned = clean_business_idea(input_text)
        
        assert "Please could you help me" not in cleaned
        assert "please" not in cleaned.lower()
        assert "help" not in cleaned.lower()
        assert "restaurant" in cleaned.lower()
        assert "Milan" in cleaned
    
    def test_removes_request_filler_please_help_me(self):
        """Should remove 'please help me' request fillers."""
        input_text = "Please help me launch a coffee shop in Florence"
        cleaned = clean_business_idea(input_text)
        
        assert "Please help me" not in cleaned
        assert "coffee shop" in cleaned.lower()
        assert "Florence" in cleaned
    
    def test_removes_request_filler_could_you_help_me(self):
        """Should remove 'could you help me' request fillers."""
        input_text = "Could you help me to start a food truck business"
        cleaned = clean_business_idea(input_text)
        
        assert "Could you help me" not in cleaned
        assert "food truck" in cleaned.lower()
    
    def test_removes_request_filler_i_want_you_to(self):
        """Should remove 'I want you to' request fillers."""
        input_text = "I want you to help me create a catering business"
        cleaned = clean_business_idea(input_text)
        
        assert "I want you to" not in cleaned
        assert "catering business" in cleaned.lower()
    
    def test_normalizes_typo_resturan_to_restaurant(self):
        """Should normalize 'resturan' to 'restaurant'."""
        input_text = "I want to launch a resturan in Milan"
        cleaned = clean_business_idea(input_text)
        
        assert "restaurant" in cleaned.lower()
        assert "resturan" not in cleaned.lower()
    
    def test_normalizes_typo_resturant_to_restaurant(self):
        """Should normalize 'resturant' to 'restaurant'."""
        input_text = "Opening a resturant in Rome"
        cleaned = clean_business_idea(input_text)
        
        assert "restaurant" in cleaned.lower()
        assert "resturant" not in cleaned.lower()
    
    def test_normalizes_typo_barkery_to_bakery(self):
        """Should normalize 'barkery' to 'bakery'."""
        input_text = "Launch a barkery in Milan"
        cleaned = clean_business_idea(input_text)
        
        assert "bakery" in cleaned.lower()
        assert "barkery" not in cleaned.lower()
    
    def test_normalizes_typo_bussiness_to_business(self):
        """Should normalize 'bussiness' to 'business'."""
        input_text = "Start a food bussiness in Florence"
        cleaned = clean_business_idea(input_text)
        
        assert "business" in cleaned.lower()
        assert "bussiness" not in cleaned.lower()
    
    def test_normalizes_typo_coffe_to_coffee(self):
        """Should normalize 'coffe' to 'coffee'."""
        input_text = "Open a coffe shop in Milan"
        cleaned = clean_business_idea(input_text)
        
        assert "coffee" in cleaned.lower()
        assert "coffe" not in cleaned.lower() or "coffee" in cleaned.lower()
    
    def test_complex_cleaning_example(self):
        """Should handle complex input with multiple issues."""
        input_text = "I am Meaza. Please could you help me to prepare a business idea to launch a Resturan in Milan"
        cleaned = clean_business_idea(input_text)
        
        # Should remove personal intro
        assert "I am Meaza" not in cleaned
        assert "Meaza" not in cleaned
        
        # Should remove request filler
        assert "Please could you help me" not in cleaned
        assert "prepare a business idea" not in cleaned
        
        # Should normalize typo
        assert "restaurant" in cleaned.lower()
        assert "resturan" not in cleaned.lower()
        
        # Should keep essential content
        assert "Milan" in cleaned
        assert "launch" in cleaned.lower()
    
    def test_capitalizes_first_letter(self):
        """Should capitalize the first letter of cleaned text."""
        input_text = "i want to launch a bakery"
        cleaned = clean_business_idea(input_text)
        
        assert cleaned[0].isupper()
        assert "Launch" in cleaned or "Bakery" in cleaned
    
    def test_adds_period_if_missing(self):
        """Should add period at the end if missing."""
        input_text = "Launch a bakery in Milan"
        cleaned = clean_business_idea(input_text)
        
        assert cleaned.endswith('.')


class TestEnhancedBusinessIdeaValidation:
    """Test enhanced validation of business idea text."""
    
    def test_rejects_math_problem_addition(self):
        """Should reject math problems like '2 + 2 = 4'."""
        is_valid, error = validate_business_idea("Please solve this math problem: 2 + 2 = 4")
        
        assert not is_valid
        assert "math problem" in error.lower() or "academic exercise" in error.lower()
    
    def test_rejects_math_problem_equation(self):
        """Should reject text containing 'solve equation'."""
        is_valid, error = validate_business_idea("Solve this equation: x + 5 = 10")
        
        assert not is_valid
        assert "math problem" in error.lower() or "academic exercise" in error.lower()
    
    def test_rejects_homework_assignment(self):
        """Should reject homework assignments."""
        is_valid, error = validate_business_idea("This is my homework assignment for school")
        
        assert not is_valid
        assert "food business idea" in error.lower()
    
    def test_rejects_school_exercise(self):
        """Should reject school-related text."""
        is_valid, error = validate_business_idea("Write an essay about the university course")
        
        assert not is_valid
        assert "food business idea" in error.lower()
    
    def test_rejects_programming_code(self):
        """Should reject programming-related text."""
        is_valid, error = validate_business_idea("Write a function to calculate the algorithm")
        
        assert not is_valid
        assert "food business idea" in error.lower()
    
    def test_rejects_physics_problem(self):
        """Should reject physics/science problems."""
        is_valid, error = validate_business_idea("Calculate the physics formula for chemistry")
        
        assert not is_valid
        assert "food business idea" in error.lower()
    
    def test_rejects_text_without_food_context(self):
        """Should reject text that doesn't mention food/business."""
        is_valid, error = validate_business_idea("I want to build something interesting and unique for people")
        
        assert not is_valid
        assert "food" in error.lower() or "restaurant" in error.lower()
    
    def test_accepts_valid_restaurant_idea(self):
        """Should accept valid restaurant business idea."""
        is_valid, error = validate_business_idea("Launch a restaurant in Milan")
        
        assert is_valid
        assert error == ""
    
    def test_accepts_valid_bakery_idea(self):
        """Should accept valid bakery business idea."""
        is_valid, error = validate_business_idea("Open a bakery in Rome")
        
        assert is_valid
        assert error == ""
    
    def test_accepts_valid_coffee_shop_idea(self):
        """Should accept valid coffee shop business idea."""
        is_valid, error = validate_business_idea("Start a coffee shop for morning commuters")
        
        assert is_valid
        assert error == ""
    
    def test_accepts_valid_food_truck_idea(self):
        """Should accept valid food truck business idea."""
        is_valid, error = validate_business_idea("Launch a food truck serving Mexican cuisine")
        
        assert is_valid
        assert error == ""
    
    def test_accepts_idea_with_typos_after_cleaning(self):
        """Should accept ideas with typos that get normalized."""
        # Note: validation happens before cleaning in the app flow
        # But the idea should still be valid if it contains food keywords
        is_valid, error = validate_business_idea("Launch a resturan in Milan")
        
        # Should be valid because it contains "Milan" and implies food business
        # The typo will be fixed during cleaning
        assert is_valid
        assert error == ""
    
    def test_accepts_complex_valid_idea(self):
        """Should accept complex but valid food business idea."""
        input_text = "I am Meaza. Please could you help me to prepare a business idea to launch a Restaurant in Milan"
        is_valid, error = validate_business_idea(input_text)
        
        # Should be valid because it contains "Restaurant" and "Milan"
        assert is_valid
        assert error == ""
    
    def test_rejects_random_french_text(self):
        """Should reject random French text without food context."""
        is_valid, error = validate_business_idea("Bonjour, comment allez-vous aujourd'hui?")
        
        assert not is_valid
        assert "food" in error.lower()
    
    def test_accepts_french_text_with_food_context(self):
        """Should accept French text if it mentions food/restaurant."""
        is_valid, error = validate_business_idea("Ouvrir un restaurant français à Milan")
        
        # Should be valid because it contains "restaurant"
        assert is_valid
        assert error == ""


class TestBusinessIdeaIntegration:
    """Test integration of cleaning and validation."""
    
    def test_full_workflow_with_personal_intro(self):
        """Test complete workflow: validation -> cleaning -> output."""
        input_text = "I am Meaza. Please could you help me to prepare a business idea to launch a Restaurant in Milan"
        
        # Step 1: Validate (should pass because it contains "Restaurant")
        is_valid, error = validate_business_idea(input_text)
        assert is_valid
        
        # Step 2: Clean (should remove personal intro and request filler)
        cleaned = clean_business_idea(input_text)
        assert "I am Meaza" not in cleaned
        assert "Please could you help me" not in cleaned
        assert "restaurant" in cleaned.lower()
        assert "Milan" in cleaned
    
    def test_full_workflow_with_typos(self):
        """Test complete workflow with typos."""
        input_text = "Launch a resturan and barkery in Milan"
        
        # Step 1: Validate (should pass)
        is_valid, error = validate_business_idea(input_text)
        assert is_valid
        
        # Step 2: Clean (should normalize typos)
        cleaned = clean_business_idea(input_text)
        assert "restaurant" in cleaned.lower()
        assert "bakery" in cleaned.lower()
        assert "resturan" not in cleaned.lower()
        assert "barkery" not in cleaned.lower()
    
    def test_rejects_then_no_cleaning_needed(self):
        """If validation fails, cleaning shouldn't matter."""
        input_text = "Solve this math problem: 2 + 2 = 4"
        
        # Step 1: Validate (should fail)
        is_valid, error = validate_business_idea(input_text)
        assert not is_valid
        assert "math problem" in error.lower()
        
        # Cleaning would happen but output wouldn't be used
        # since validation failed

# Made with Bob
