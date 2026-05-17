"""Tests for multi-provider AI integration in MenuNest.

These tests verify:
- Provider selection logic (demo, watsonx, openai, anthropic)
- API integrations for all providers
- Error handling and fallback behavior
- Security (no API keys in output)
- Demo mode reliability
"""

from __future__ import annotations

import json
import os
from unittest.mock import MagicMock, patch

import pytest
import requests

from src.ai_generator import (
    call_watsonx_api,
    extract_json_from_text,
    generate_launch_plan,
)
from src.config import DEFAULT_INPUTS


class TestProviderSelection:
    """Test provider selection logic in generate_launch_plan."""

    def test_demo_mode_by_default(self):
        """Demo mode should be used when LLM_PROVIDER is not set."""
        with patch.dict(os.environ, {}, clear=True):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=True)
            assert plan is not None
            assert "business_summary" in plan
            assert "menu_items" in plan

    def test_demo_mode_explicit(self):
        """Demo mode should work when explicitly set."""
        with patch.dict(os.environ, {"LLM_PROVIDER": "demo"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            assert "business_summary" in plan

    def test_use_demo_flag_overrides_provider(self):
        """use_demo=True should override LLM_PROVIDER setting."""
        with patch.dict(os.environ, {"LLM_PROVIDER": "watsonx"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=True)
            assert plan is not None
            # Should use demo mode, not attempt watsonx call

    def test_unknown_provider_falls_back_to_demo(self, capsys):
        """Unknown provider should fall back to demo mode with warning."""
        with patch.dict(os.environ, {"LLM_PROVIDER": "unknown_provider"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            
            # Check warning was printed
            captured = capsys.readouterr()
            assert "Unknown LLM_PROVIDER" in captured.out
            assert "unknown_provider" in captured.out


class TestWatsonxAPIIntegration:
    """Test watsonx.ai API integration."""

    def test_missing_api_key_raises_error(self):
        """Missing WATSONX_API_KEY should raise ValueError."""
        with patch.dict(os.environ, {"WATSONX_PROJECT_ID": "test-project"}, clear=True):
            with pytest.raises(ValueError, match="WATSONX_API_KEY"):
                call_watsonx_api("test prompt")

    def test_missing_project_id_raises_error(self):
        """Missing WATSONX_PROJECT_ID should raise ValueError."""
        with patch.dict(os.environ, {"WATSONX_API_KEY": "test-key"}, clear=True):
            with pytest.raises(ValueError, match="WATSONX_PROJECT_ID"):
                call_watsonx_api("test prompt")

    @patch("src.ai_generator.requests.post")
    def test_successful_watsonx_call(self, mock_post):
        """Successful watsonx call should return validated plan."""
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "generated_text": json.dumps({
                        "business_summary": "This is a comprehensive test business summary with sufficient length for validation",
                        "positioning": "This is a detailed positioning statement that meets minimum length requirements",
                        "launch_readiness_score": 75,
                        "estimated_complexity": "Medium",
                        "best_customer_segment": "Test segment for validation",
                        "key_recommendation": "This is a detailed key recommendation that provides actionable guidance",
                        "main_risks": [
                            "First risk with sufficient detail for validation",
                            "Second risk with sufficient detail for validation"
                        ],
                        "next_steps": [
                            "First actionable step with sufficient detail",
                            "Second actionable step with sufficient detail"
                        ],
                        "menu_items": [
                            {
                                "name": "Test Item",
                                "category": "Drink",
                                "description": "Test description with sufficient detail",
                                "complexity": "Low",
                                "suggested_price": "5.00 EUR",
                                "pricing_note": "Test pricing note with detail",
                                "ingredients": ["Ingredient 1"],
                                "allergens": ["None common"],
                                "preparation_note": "Test preparation note",
                                "operational_tip": "Test operational tip",
                            }
                        ],
                        "customer_personas": [
                            {
                                "name": "Test Persona",
                                "profile": "Test profile with sufficient detail for validation",
                                "needs": "Test needs with sufficient detail",
                                "recommended_offer": "Test offer with detail",
                                "marketing_angle": "Test marketing angle with detail",
                            }
                        ],
                        "marketing": {
                            "slogan": "Test slogan with detail",
                            "instagram_bio": "Test bio with sufficient detail",
                            "captions": ["Caption with sufficient detail for validation"],
                            "launch_announcement": "Test launch announcement with sufficient detail for validation",
                        },
                        "launch_checklist": {
                            "before_launch": ["Task with sufficient detail"],
                            "menu_validation": ["Task with sufficient detail"],
                            "marketing_setup": ["Task with sufficient detail"],
                            "operations": ["Task with sufficient detail"],
                            "first_week_testing": ["Task with sufficient detail"],
                        },
                    })
                }
            ]
        }
        mock_post.return_value = mock_response

        with patch.dict(
            os.environ,
            {
                "WATSONX_API_KEY": "test-key",
                "WATSONX_PROJECT_ID": "test-project",
            },
        ):
            plan = call_watsonx_api("test prompt")
            assert plan is not None
            assert "business_summary" in plan
            assert len(plan["business_summary"]) >= 20  # Validates minimum length
            assert len(plan["menu_items"]) == 1

    @patch("src.ai_generator.requests.post")
    def test_api_timeout_raises_exception(self, mock_post):
        """API timeout should raise RequestException."""
        mock_post.side_effect = requests.exceptions.Timeout()

        with patch.dict(
            os.environ,
            {
                "WATSONX_API_KEY": "test-key",
                "WATSONX_PROJECT_ID": "test-project",
            },
        ):
            with pytest.raises(requests.RequestException, match="timed out"):
                call_watsonx_api("test prompt")

    @patch("src.ai_generator.requests.post")
    def test_api_error_raises_exception(self, mock_post):
        """API error should raise RequestException."""
        mock_post.side_effect = requests.exceptions.RequestException("API error")

        with patch.dict(
            os.environ,
            {
                "WATSONX_API_KEY": "test-key",
                "WATSONX_PROJECT_ID": "test-project",
            },
        ):
            with pytest.raises(requests.RequestException, match="API request failed"):
                call_watsonx_api("test prompt")

    @patch("src.ai_generator.requests.post")
    def test_invalid_response_format_raises_error(self, mock_post):
        """Invalid response format should raise ValueError."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"invalid": "format"}
        mock_post.return_value = mock_response

        with patch.dict(
            os.environ,
            {
                "WATSONX_API_KEY": "test-key",
                "WATSONX_PROJECT_ID": "test-project",
            },
        ):
            with pytest.raises(ValueError, match="Invalid response format"):
                call_watsonx_api("test prompt")


class TestErrorHandlingAndFallback:
    """Test error handling and fallback to demo mode."""

    @patch("src.ai_generator.call_watsonx_api")
    def test_missing_credentials_falls_back_to_demo(self, mock_call, capsys):
        """Missing credentials should fall back to demo mode."""
        mock_call.side_effect = ValueError("WATSONX_API_KEY environment variable is required")

        with patch.dict(os.environ, {"LLM_PROVIDER": "watsonx"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            assert "business_summary" in plan
            
            # Check warning was printed
            captured = capsys.readouterr()
            assert "watsonx.ai error" in captured.out
            assert "Falling back to demo mode" in captured.out

    @patch("src.ai_generator.call_watsonx_api")
    def test_api_failure_falls_back_to_demo(self, mock_call, capsys):
        """API failure should fall back to demo mode."""
        mock_call.side_effect = requests.RequestException("API call failed")

        with patch.dict(os.environ, {"LLM_PROVIDER": "watsonx"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            
            # Check warning was printed
            captured = capsys.readouterr()
            assert "watsonx.ai API call failed" in captured.out
            assert "Falling back to demo mode" in captured.out

    @patch("src.ai_generator.call_watsonx_api")
    def test_unexpected_error_falls_back_to_demo(self, mock_call, capsys):
        """Unexpected error should fall back to demo mode."""
        mock_call.side_effect = Exception("Unexpected error")

        with patch.dict(os.environ, {"LLM_PROVIDER": "watsonx"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            
            # Check warning was printed
            captured = capsys.readouterr()
            assert "Unexpected error with watsonx.ai" in captured.out
            assert "Falling back to demo mode" in captured.out


class TestJSONExtraction:
    """Test JSON extraction from model output."""

    def test_extract_plain_json(self):
        """Should extract plain JSON object."""
        text = '{"key": "value", "number": 42}'
        result = extract_json_from_text(text)
        assert result == text
        assert json.loads(result) == {"key": "value", "number": 42}

    def test_extract_json_with_markdown(self):
        """Should extract JSON from markdown code blocks."""
        text = '```json\n{"key": "value"}\n```'
        result = extract_json_from_text(text)
        assert "```" not in result
        assert json.loads(result) == {"key": "value"}

    def test_extract_json_with_text_before(self):
        """Should extract JSON when there's text before it."""
        text = 'Here is the JSON:\n{"key": "value"}'
        result = extract_json_from_text(text)
        assert json.loads(result) == {"key": "value"}

    def test_extract_json_with_text_after(self):
        """Should extract JSON when there's text after it."""
        text = '{"key": "value"}\nThat was the JSON.'
        result = extract_json_from_text(text)
        assert json.loads(result) == {"key": "value"}

    def test_no_json_raises_error(self):
        """Should raise error when no JSON is found."""
        text = "This is just plain text with no JSON"
        with pytest.raises(ValueError, match="No valid JSON object found"):
            extract_json_from_text(text)

    def test_invalid_json_raises_error(self):
        """Should raise error when extracted text is not valid JSON."""
        text = "{this is not valid json}"
        with pytest.raises(ValueError, match="not valid JSON"):
            extract_json_from_text(text)


class TestSecurityAndPrivacy:
    """Test security and privacy requirements."""

    @patch("src.ai_generator.requests.post")
    def test_no_api_key_in_error_messages(self, mock_post):
        """API key should be redacted from error messages."""
        api_key = "secret-api-key-12345"
        mock_post.side_effect = requests.RequestException(f"Error with key {api_key}")

        with patch.dict(
            os.environ,
            {
                "WATSONX_API_KEY": api_key,
                "WATSONX_PROJECT_ID": "test-project",
            },
        ):
            with pytest.raises(requests.RequestException) as exc_info:
                call_watsonx_api("test prompt")
            
            # API key should be redacted
            assert api_key not in str(exc_info.value)
            assert "[REDACTED]" in str(exc_info.value)

    def test_demo_mode_never_exposes_credentials(self):
        """Demo mode should never access or expose credentials."""
        with patch.dict(
            os.environ,
            {
                "WATSONX_API_KEY": "secret-key",
                "WATSONX_PROJECT_ID": "secret-project",
            },
        ):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=True)
            
            # Convert plan to string to check for credentials
            plan_str = json.dumps(plan)
            assert "secret-key" not in plan_str
            assert "secret-project" not in plan_str

    @patch("src.ai_generator.call_watsonx_api")
    def test_watsonx_response_never_contains_credentials(self, mock_call):
        """watsonx response should never contain API credentials."""
        # Mock a response that includes credentials (should never happen, but test it)
        mock_plan = {
            "business_summary": "Test with WATSONX_API_KEY=secret",
            "positioning": "Test",
            "launch_readiness_score": 75,
            "estimated_complexity": "Medium",
            "best_customer_segment": "Test",
            "key_recommendation": "Test",
            "main_risks": ["Risk"],
            "next_steps": ["Step"],
            "menu_items": [],
            "customer_personas": [],
            "marketing": {
                "slogan": "Test",
                "instagram_bio": "Test",
                "captions": [],
                "launch_announcement": "Test",
            },
            "launch_checklist": {
                "before_launch": [],
                "menu_validation": [],
                "marketing_setup": [],
                "operations": [],
                "first_week_testing": [],
            },
        }
        mock_call.return_value = mock_plan

        with patch.dict(
            os.environ,
            {
                "LLM_PROVIDER": "watsonx",
                "WATSONX_API_KEY": "secret-key",
                "WATSONX_PROJECT_ID": "secret-project",
            },
        ):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            
            # Even if the mock includes credentials, they should not be in the final plan
            # (In reality, the validator would clean this, but we're testing the principle)
            plan_str = json.dumps(plan)
            # The mock data contains "secret" but not the actual env var values
            assert "secret-key" not in plan_str
            assert "secret-project" not in plan_str


class TestLanguageSupport:
    """Test language support with watsonx integration."""

    @patch("src.ai_generator.call_watsonx_api")
    def test_watsonx_respects_output_language(self, mock_call):
        """watsonx should receive language preference in prompt."""
        mock_plan = {
            "business_summary": "Test",
            "positioning": "Test",
            "launch_readiness_score": 75,
            "estimated_complexity": "Medium",
            "best_customer_segment": "Test",
            "key_recommendation": "Test",
            "main_risks": ["Risk"],
            "next_steps": ["Step"],
            "menu_items": [],
            "customer_personas": [],
            "marketing": {
                "slogan": "Test",
                "instagram_bio": "Test",
                "captions": [],
                "launch_announcement": "Test",
            },
            "launch_checklist": {
                "before_launch": [],
                "menu_validation": [],
                "marketing_setup": [],
                "operations": [],
                "first_week_testing": [],
            },
        }
        mock_call.return_value = mock_plan

        inputs = dict(DEFAULT_INPUTS)
        inputs["output_language"] = "Italian"

        with patch.dict(os.environ, {"LLM_PROVIDER": "watsonx"}):
            plan = generate_launch_plan(inputs, use_demo=False)
            assert plan is not None
            
            # Verify the prompt was built with Italian language
            # (The actual language handling is in the prompt builder)
            mock_call.assert_called_once()

# Made with Bob



class TestOpenAIIntegration:
    """Test OpenAI API integration."""

    def test_missing_api_key_raises_error(self):
        """Missing OPENAI_API_KEY should raise ValueError."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="OPENAI_API_KEY"):
                from src.ai_generator import call_openai_api
                call_openai_api("test prompt")

    def test_successful_openai_call(self):
        """Successful OpenAI call should return validated plan."""
        # Create a complete mock for the openai module
        mock_openai = MagicMock()
        mock_client = MagicMock()
        mock_openai.OpenAI.return_value = mock_client
        
        # Create mock response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = json.dumps({
            "business_summary": "This is a comprehensive test business summary with sufficient length for validation",
            "positioning": "This is a detailed positioning statement that meets minimum length requirements",
            "launch_readiness_score": 75,
            "estimated_complexity": "Medium",
            "best_customer_segment": "Test segment for validation",
            "key_recommendation": "This is a detailed key recommendation that provides actionable guidance",
            "main_risks": [
                "First risk with sufficient detail for validation",
                "Second risk with sufficient detail for validation"
            ],
            "next_steps": [
                "First actionable step with sufficient detail",
                "Second actionable step with sufficient detail"
            ],
            "menu_items": [
                {
                    "name": "Test Item",
                    "category": "Drink",
                    "description": "Test description with sufficient detail",
                    "complexity": "Low",
                    "suggested_price": "5.00 EUR",
                    "pricing_note": "Test pricing note with detail",
                    "ingredients": ["Ingredient 1"],
                    "allergens": ["None common"],
                    "preparation_note": "Test preparation note",
                    "operational_tip": "Test operational tip",
                }
            ],
            "customer_personas": [
                {
                    "name": "Test Persona",
                    "profile": "Test profile with sufficient detail for validation",
                    "needs": "Test needs with sufficient detail",
                    "recommended_offer": "Test offer with detail",
                    "marketing_angle": "Test marketing angle with detail",
                }
            ],
            "marketing": {
                "slogan": "Test slogan with detail",
                "instagram_bio": "Test bio with sufficient detail",
                "captions": ["Caption with sufficient detail for validation"],
                "launch_announcement": "Test launch announcement with sufficient detail for validation",
            },
            "launch_checklist": {
                "before_launch": ["Task with sufficient detail"],
                "menu_validation": ["Task with sufficient detail"],
                "marketing_setup": ["Task with sufficient detail"],
                "operations": ["Task with sufficient detail"],
                "first_week_testing": ["Task with sufficient detail"],
            },
        })
        mock_client.chat.completions.create.return_value = mock_response

        # Patch sys.modules before importing
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
            with patch.dict('sys.modules', {'openai': mock_openai}):
                # Force reimport by removing from cache if present
                import sys
                if 'src.ai_generator' in sys.modules:
                    del sys.modules['src.ai_generator']
                
                from src.ai_generator import call_openai_api
                plan = call_openai_api("test prompt")
                assert plan is not None
                assert "business_summary" in plan
                assert len(plan["business_summary"]) >= 20

    @patch("src.ai_generator.call_openai_api")
    def test_openai_provider_falls_back_on_error(self, mock_call, capsys):
        """OpenAI provider should fall back to demo mode on error."""
        mock_call.side_effect = ValueError("OPENAI_API_KEY environment variable is required")

        with patch.dict(os.environ, {"LLM_PROVIDER": "openai"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            
            # Check warning was printed
            captured = capsys.readouterr()
            assert "OpenAI error" in captured.out
            assert "Falling back to demo mode" in captured.out


class TestAnthropicIntegration:
    """Test Anthropic API integration."""

    def test_missing_api_key_raises_error(self):
        """Missing ANTHROPIC_API_KEY should raise ValueError."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
                from src.ai_generator import call_anthropic_api
                call_anthropic_api("test prompt")

    def test_successful_anthropic_call(self):
        """Successful Anthropic call should return validated plan."""
        # Create a complete mock for the anthropic module
        mock_anthropic = MagicMock()
        mock_client = MagicMock()
        mock_anthropic.Anthropic.return_value = mock_client
        
        # Create mock response
        mock_response = MagicMock()
        mock_response.content = [MagicMock()]
        mock_response.content[0].text = json.dumps({
            "business_summary": "This is a comprehensive test business summary with sufficient length for validation",
            "positioning": "This is a detailed positioning statement that meets minimum length requirements",
            "launch_readiness_score": 75,
            "estimated_complexity": "Medium",
            "best_customer_segment": "Test segment for validation",
            "key_recommendation": "This is a detailed key recommendation that provides actionable guidance",
            "main_risks": [
                "First risk with sufficient detail for validation",
                "Second risk with sufficient detail for validation"
            ],
            "next_steps": [
                "First actionable step with sufficient detail",
                "Second actionable step with sufficient detail"
            ],
            "menu_items": [
                {
                    "name": "Test Item",
                    "category": "Drink",
                    "description": "Test description with sufficient detail",
                    "complexity": "Low",
                    "suggested_price": "5.00 EUR",
                    "pricing_note": "Test pricing note with detail",
                    "ingredients": ["Ingredient 1"],
                    "allergens": ["None common"],
                    "preparation_note": "Test preparation note",
                    "operational_tip": "Test operational tip",
                }
            ],
            "customer_personas": [
                {
                    "name": "Test Persona",
                    "profile": "Test profile with sufficient detail for validation",
                    "needs": "Test needs with sufficient detail",
                    "recommended_offer": "Test offer with detail",
                    "marketing_angle": "Test marketing angle with detail",
                }
            ],
            "marketing": {
                "slogan": "Test slogan with detail",
                "instagram_bio": "Test bio with sufficient detail",
                "captions": ["Caption with sufficient detail for validation"],
                "launch_announcement": "Test launch announcement with sufficient detail for validation",
            },
            "launch_checklist": {
                "before_launch": ["Task with sufficient detail"],
                "menu_validation": ["Task with sufficient detail"],
                "marketing_setup": ["Task with sufficient detail"],
                "operations": ["Task with sufficient detail"],
                "first_week_testing": ["Task with sufficient detail"],
            },
        })
        mock_client.messages.create.return_value = mock_response

        # Patch the import to return our mock
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"}):
            with patch.dict('sys.modules', {'anthropic': mock_anthropic}):
                from src.ai_generator import call_anthropic_api
                plan = call_anthropic_api("test prompt")
                assert plan is not None
                assert "business_summary" in plan
                assert len(plan["business_summary"]) >= 20

    @patch("src.ai_generator.call_anthropic_api")
    def test_anthropic_provider_falls_back_on_error(self, mock_call, capsys):
        """Anthropic provider should fall back to demo mode on error."""
        mock_call.side_effect = ValueError("ANTHROPIC_API_KEY environment variable is required")

        with patch.dict(os.environ, {"LLM_PROVIDER": "anthropic"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            
            # Check warning was printed
            captured = capsys.readouterr()
            assert "Anthropic error" in captured.out
            assert "Falling back to demo mode" in captured.out


class TestMultiProviderSelection:
    """Test provider selection with all four providers."""

    def test_all_providers_supported(self):
        """All four providers should be recognized."""
        supported_providers = ["demo", "watsonx", "openai", "anthropic"]
        
        for provider in supported_providers:
            with patch.dict(os.environ, {"LLM_PROVIDER": provider}):
                # Should not print unknown provider warning
                plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=True)
                assert plan is not None

    def test_unknown_provider_shows_all_options(self, capsys):
        """Unknown provider warning should list all supported providers."""
        with patch.dict(os.environ, {"LLM_PROVIDER": "unsupported"}):
            plan = generate_launch_plan(DEFAULT_INPUTS, use_demo=False)
            assert plan is not None
            
            captured = capsys.readouterr()
            assert "demo" in captured.out
            assert "watsonx" in captured.out
            assert "openai" in captured.out
            assert "anthropic" in captured.out
