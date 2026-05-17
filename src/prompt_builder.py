"""Prompt construction utilities for MenuNest AI generation."""

from __future__ import annotations

from typing import Any


def build_launch_plan_prompt(user_inputs: dict[str, Any]) -> str:
    """Build a structured prompt for generating a food business launch plan.
    
    This prompt is designed to produce practical, actionable advice for food
    entrepreneurs while maintaining a consistent JSON schema for validation.
    """
    dietary_focus = user_inputs.get("dietary_focus") or []
    if isinstance(dietary_focus, list):
        dietary_focus_text = ", ".join(dietary_focus) if dietary_focus else "No specific focus"
    else:
        dietary_focus_text = str(dietary_focus)

    output_language = user_inputs.get("output_language", "English")
    
    # Build language-specific instructions
    language_instruction = ""
    if output_language == "Italian":
        language_instruction = "\n- Generate ALL content in Italian language, including field values, descriptions, and recommendations."
    elif output_language == "English":
        language_instruction = "\n- Generate ALL content in English language."

    prompt = f"""
You are MenuNest, an AI copilot for food entrepreneurs. Your role is to provide practical,
actionable business advice for small food business launches.

# Business Context
Business idea: {user_inputs.get("business_idea", "")}
Business type: {user_inputs.get("business_type", "")}
Cuisine type: {user_inputs.get("cuisine", "")}
Location: {user_inputs.get("location", "")}
Budget range: {user_inputs.get("budget", "")}
Target customers: {user_inputs.get("target_customers", "")}
Dietary focus: {dietary_focus_text}
Launch goal: {user_inputs.get("launch_goal", "")}
Output language: {output_language}

# Your Task
Generate a comprehensive, realistic launch plan that helps this entrepreneur validate their
concept before investing heavily in rent, equipment, or inventory.

# Output Requirements
CRITICAL: You MUST return ONLY a valid JSON object. Do not include:
- Markdown code blocks (no ```json or ```)
- Explanatory text before or after the JSON
- Comments inside the JSON
- Any text that is not part of the JSON structure

Return this exact JSON structure with all fields populated:

{{
  "business_summary": "2-3 sentence overview of the business concept and target market",
  "positioning": "Clear positioning statement explaining what makes this business unique",
  "launch_readiness_score": 0-100,
  "estimated_complexity": "Low | Medium | High",
  "best_customer_segment": "Primary target customer group",
  "key_recommendation": "Single most important strategic recommendation",
  "main_risks": ["Risk 1", "Risk 2", "Risk 3", "Risk 4"],
  "next_steps": ["Action 1", "Action 2", "Action 3", "Action 4"],
  "menu_items": [
    {{
      "name": "Item name",
      "category": "Drink | Snack | Breakfast | Lunch | Dessert | Other",
      "description": "Brief customer-facing description",
      "complexity": "Low | Medium | High",
      "suggested_price": "X.XX-Y.YY EUR (or local currency)",
      "pricing_note": "Strategic pricing guidance",
      "ingredients": ["Ingredient 1", "Ingredient 2", "..."],
      "allergens": ["Allergen 1", "Allergen 2", "None common"],
      "preparation_note": "Practical prep guidance",
      "operational_tip": "Efficiency or quality tip"
    }}
  ],
  "customer_personas": [
    {{
      "name": "Persona name",
      "profile": "Demographic and behavioral description",
      "needs": "What they're looking for",
      "recommended_offer": "Best menu item or combo for them",
      "marketing_angle": "How to attract this segment"
    }}
  ],
  "marketing": {{
    "slogan": "Memorable tagline under 12 words",
    "instagram_bio": "Compelling bio under 150 characters",
    "captions": ["Caption 1", "Caption 2", "Caption 3"],
    "launch_announcement": "Launch strategy recommendation"
  }},
  "launch_checklist": {{
    "before_launch": ["Task 1", "Task 2", "Task 3", "Task 4"],
    "menu_validation": ["Task 1", "Task 2", "Task 3"],
    "marketing_setup": ["Task 1", "Task 2", "Task 3"],
    "operations": ["Task 1", "Task 2", "Task 3"],
    "first_week_testing": ["Task 1", "Task 2", "Task 3", "Task 4"]
  }}
}}

# Critical Guidelines
- Provide 5-8 menu items that are realistic for the budget and business type
- Include at least 3 customer personas representing different segments
- Make pricing suggestions realistic for the location and market
- Focus on validation and testing before heavy investment
- Include specific, actionable tasks in the launch checklist
- Mention allergens clearly (use "None common" if truly allergen-free)
- Keep complexity assessments honest (don't oversimplify)
- Provide operational tips that save time or reduce waste{language_instruction}
- NEVER include legal advice, health claims, or compliance guarantees
- Emphasize that all pricing must be validated with real ingredient costs
- Focus on practical entrepreneurship, not aspirational marketing

# Quality Standards
- Business summary: Must clearly explain WHO the customers are and WHAT problem is solved
- Positioning: Must differentiate from competitors in the same location
- Launch readiness score: Base on budget adequacy, market clarity, and operational feasibility
- Menu items: Must be achievable with stated budget and complexity level
- Customer personas: Must reflect real market segments in the specified location
- Marketing content: Must be authentic and culturally appropriate for the location
- Launch checklist: Must be sequential and actionable (not vague aspirations)

Generate the launch plan now. Return ONLY the JSON object, nothing else.
""".strip()
    return prompt
