"""Tests for Business Idea parsing and cleaning functionality."""

import pytest
from src.sample_data import clean_business_idea, extract_concept_snippet, generate_dynamic_demo_plan


class TestBusinessIdeaCleaning:
    """Test business idea cleaning and normalization."""
    
    def test_removes_greeting_hi(self):
        """Test that 'Hi' greeting is removed."""
        raw = "Hi, I want to launch a bakery in Milan"
        cleaned = clean_business_idea(raw)
        assert not cleaned.lower().startswith("hi")
        assert "bakery" in cleaned.lower()
        assert "milan" in cleaned.lower()
    
    def test_removes_greeting_hello(self):
        """Test that 'Hello' greeting is removed."""
        raw = "Hello, I want to open a coffee shop"
        cleaned = clean_business_idea(raw)
        assert not cleaned.lower().startswith("hello")
        assert "coffee" in cleaned.lower()
    
    def test_removes_multiline_greeting(self):
        """Test that greetings in multiline input are removed."""
        raw = "Hi,\nI want to launch Bakery in Milan Italy"
        cleaned = clean_business_idea(raw)
        assert not cleaned.lower().startswith("hi")
        assert "bakery" in cleaned.lower()
    
    def test_normalizes_whitespace(self):
        """Test that multiple spaces and newlines are normalized."""
        raw = "A   bakery\n\nwith    fresh   bread"
        cleaned = clean_business_idea(raw)
        assert "  " not in cleaned  # No double spaces
        assert "\n" not in cleaned  # No newlines
        assert "bakery with fresh bread" in cleaned.lower()
    
    def test_removes_filler_phrase_i_want_to(self):
        """Test that 'I want to' is removed."""
        raw = "I want to launch a pizza restaurant"
        cleaned = clean_business_idea(raw)
        assert not cleaned.lower().startswith("i want to")
        assert cleaned.startswith("Launch") or cleaned.startswith("launch")
    
    def test_removes_filler_phrase_i_would_like_to(self):
        """Test that 'I would like to' is removed."""
        raw = "I would like to open a vegan cafe"
        cleaned = clean_business_idea(raw)
        assert not cleaned.lower().startswith("i would like to")
        assert "vegan" in cleaned.lower()
    
    def test_capitalizes_first_letter(self):
        """Test that first letter is capitalized."""
        raw = "a small bakery in rome"
        cleaned = clean_business_idea(raw)
        assert cleaned[0].isupper()
    
    def test_adds_period_if_missing(self):
        """Test that period is added if missing."""
        raw = "A bakery in Milan"
        cleaned = clean_business_idea(raw)
        assert cleaned.endswith(".")
    
    def test_preserves_existing_punctuation(self):
        """Test that existing punctuation is preserved."""
        raw = "A bakery in Milan!"
        cleaned = clean_business_idea(raw)
        assert cleaned.endswith("!")
    
    def test_complex_multiline_with_greeting(self):
        """Test complex real-world input."""
        raw = """Hi,
        I want to launch Bakery in Milan Italy
        with traditional Italian breads"""
        cleaned = clean_business_idea(raw)
        assert not cleaned.lower().startswith("hi")
        assert "bakery" in cleaned.lower()
        assert "milan" in cleaned.lower()
        assert "traditional" in cleaned.lower()
        assert "\n" not in cleaned


class TestConceptSnippet:
    """Test concept snippet extraction."""
    
    def test_short_concept_returned_as_is(self):
        """Test that short concepts are returned without truncation."""
        idea = "A bakery in Milan."
        snippet = extract_concept_snippet(idea, max_words=8)
        assert snippet == "A bakery in Milan"
    
    def test_long_concept_truncated(self):
        """Test that long concepts are truncated with ellipsis."""
        idea = "A traditional Italian bakery specializing in sourdough and artisan breads in Milan."
        snippet = extract_concept_snippet(idea, max_words=5)
        assert snippet.endswith("...")
        assert len(snippet.split()) <= 6  # 5 words + ellipsis
    
    def test_removes_trailing_period(self):
        """Test that trailing period is removed from snippet."""
        idea = "A bakery in Milan."
        snippet = extract_concept_snippet(idea, max_words=10)
        assert not snippet.endswith("..")  # No double period
    
    def test_cleans_before_extracting(self):
        """Test that idea is cleaned before extraction."""
        idea = "Hi, I want to launch a bakery"
        snippet = extract_concept_snippet(idea, max_words=5)
        assert "hi" not in snippet.lower()
        assert "bakery" in snippet.lower()
    
    def test_empty_input_returns_default(self):
        """Test that empty input returns default text."""
        snippet = extract_concept_snippet("", max_words=5)
        assert snippet == "this concept"


class TestNoPythonListsInOutput:
    """Test that Python list syntax never appears in generated output."""
    
    def test_no_list_syntax_in_summary(self):
        """Test that business summary doesn't contain Python list syntax."""
        inputs = {
            "business_idea": "Hi,\nI want to launch Bakery in Milan Italy",
            "business_type": "Bakery",
            "cuisine": "Italian",
            "location": "Milan, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Local families",
            "dietary_focus": [],
            "launch_goal": "Test market",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        summary = plan["business_summary"]
        
        # Should not contain Python list syntax
        assert "[" not in summary
        assert "]" not in summary
        assert "['Hi" not in summary
        assert "['I'" not in summary
    
    def test_no_list_syntax_in_positioning(self):
        """Test that positioning doesn't contain Python list syntax."""
        inputs = {
            "business_idea": "Hello, I want to open a modern coffee shop with specialty brews",
            "business_type": "Cafe",
            "cuisine": "Coffee / Beverages",
            "location": "London, UK",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Young professionals",
            "dietary_focus": [],
            "launch_goal": "Build brand",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        positioning = plan["positioning"]
        
        # Should not contain Python list syntax
        assert "[" not in positioning
        assert "]" not in positioning
        assert "['Hello" not in positioning
    
    def test_no_list_syntax_in_recommendation(self):
        """Test that key recommendation doesn't contain Python list syntax."""
        inputs = {
            "business_idea": "Hi, I want to launch a vegan burger restaurant",
            "business_type": "Restaurant",
            "cuisine": "Vegan",
            "location": "Berlin, Germany",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Health-conscious millennials",
            "dietary_focus": ["Vegan-friendly"],
            "launch_goal": "Grand opening",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        recommendation = plan["key_recommendation"]
        
        # Should not contain Python list syntax or "For your Hi"
        assert "[" not in recommendation
        assert "]" not in recommendation
        assert "For your Hi" not in recommendation
        assert "For your ['Hi" not in recommendation
    
    def test_no_list_syntax_in_next_steps(self):
        """Test that next steps don't contain Python list syntax."""
        inputs = {
            "business_idea": "Hey, I want to start a food truck selling tacos",
            "business_type": "Food truck",
            "cuisine": "Mexican",
            "location": "Austin, USA",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Festival goers",
            "dietary_focus": [],
            "launch_goal": "Test concept",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        next_steps = plan["next_steps"]
        
        # Should not contain Python list syntax in any step
        for step in next_steps:
            assert "[" not in step
            assert "]" not in step
            assert "['Hey" not in step
    
    def test_no_list_syntax_in_marketing(self):
        """Test that marketing content doesn't contain Python list syntax."""
        inputs = {
            "business_idea": "Hi, I want to launch a healthy meal prep service",
            "business_type": "Catering service",
            "cuisine": "Mediterranean",
            "location": "New York, USA",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Busy professionals",
            "dietary_focus": ["Healthy meals"],
            "launch_goal": "Launch MVP",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        marketing = plan["marketing"]
        
        # Check all marketing fields
        assert "[" not in marketing["slogan"]
        assert "]" not in marketing["slogan"]
        assert "[" not in marketing["instagram_bio"]
        assert "]" not in marketing["instagram_bio"]
        
        for caption in marketing["captions"]:
            assert "[" not in caption
            assert "]" not in caption


class TestMultilineBusinessIdea:
    """Test that multiline business ideas are handled correctly."""
    
    def test_multiline_with_greeting_generates_valid_plan(self):
        """Test that multiline input with greeting generates valid plan."""
        inputs = {
            "business_idea": "Hi,\nI want to launch Bakery in Milan Italy",
            "business_type": "Bakery",
            "cuisine": "Italian",
            "location": "Milan, Italy",
            "budget": "10,000-25,000 EUR",
            "target_customers": "Local residents",
            "dietary_focus": [],
            "launch_goal": "Test market",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        
        # Plan should be valid
        assert "business_summary" in plan
        assert "positioning" in plan
        assert "key_recommendation" in plan
        
        # Should not contain greeting or newlines
        assert "Hi," not in plan["business_summary"]
        assert "\n" not in plan["business_summary"]
        
        # Should contain the actual concept
        assert "bakery" in plan["business_summary"].lower()
        assert "milan" in plan["business_summary"].lower()
    
    def test_multiline_preserves_concept_meaning(self):
        """Test that multiline input preserves the core concept."""
        inputs = {
            "business_idea": """Hello,
            I want to open a traditional Italian pizzeria
            with wood-fired oven and authentic recipes""",
            "business_type": "Restaurant",
            "cuisine": "Italian",
            "location": "Rome, Italy",
            "budget": "25,000-50,000 EUR",
            "target_customers": "Tourists and locals",
            "dietary_focus": [],
            "launch_goal": "Grand opening",
        }
        
        plan = generate_dynamic_demo_plan(inputs)
        
        # Core concept should be preserved
        summary_lower = plan["business_summary"].lower()
        assert "pizzeria" in summary_lower or "pizza" in summary_lower
        assert "traditional" in summary_lower or "authentic" in summary_lower
        assert "italian" in summary_lower

# Made with Bob
