"""Prompt construction utilities."""

from __future__ import annotations

from typing import Any


def build_launch_plan_prompt(user_inputs: dict[str, Any]) -> str:
    """Build a structured prompt for generating a food business launch plan."""
    dietary_focus = user_inputs.get("dietary_focus") or []
    if isinstance(dietary_focus, list):
        dietary_focus_text = ", ".join(dietary_focus)
    else:
        dietary_focus_text = str(dietary_focus)

    prompt = f"""
You are MenuNest, an AI copilot for food entrepreneurs.

Generate a practical launch plan for this food business idea.

Business idea: {user_inputs.get("business_idea", "")}
Business type: {user_inputs.get("business_type", "")}
Cuisine type: {user_inputs.get("cuisine", "")}
Location: {user_inputs.get("location", "")}
Budget range: {user_inputs.get("budget", "")}
Target customers: {user_inputs.get("target_customers", "")}
Dietary focus: {dietary_focus_text}
Launch goal: {user_inputs.get("launch_goal", "")}
Output language: {user_inputs.get("output_language", "English")}

Return only valid JSON with this structure:
{{
  "business_summary": "...",
  "positioning": "...",
  "launch_readiness_score": 0,
  "estimated_complexity": "Low | Medium | High",
  "best_customer_segment": "...",
  "key_recommendation": "...",
  "main_risks": ["...", "..."],
  "next_steps": ["...", "..."],
  "menu_items": [
    {{
      "name": "...",
      "category": "...",
      "description": "...",
      "complexity": "Low | Medium | High",
      "suggested_price": "...",
      "pricing_note": "...",
      "ingredients": ["...", "..."],
      "allergens": ["...", "..."],
      "preparation_note": "...",
      "operational_tip": "..."
    }}
  ],
  "customer_personas": [
    {{
      "name": "...",
      "profile": "...",
      "needs": "...",
      "recommended_offer": "...",
      "marketing_angle": "..."
    }}
  ],
  "marketing": {{
    "slogan": "...",
    "instagram_bio": "...",
    "captions": ["...", "...", "..."],
    "launch_announcement": "..."
  }},
  "launch_checklist": {{
    "before_launch": ["...", "..."],
    "menu_validation": ["...", "..."],
    "marketing_setup": ["...", "..."],
    "operations": ["...", "..."],
    "first_week_testing": ["...", "..."]
  }}
}}

Important:
- Keep the plan realistic for a small food entrepreneur.
- Mention that pricing is a starting estimate and must be validated with real costs.
- Include allergen notes where relevant.
- Avoid legal or compliance guarantees.
""".strip()
    return prompt
