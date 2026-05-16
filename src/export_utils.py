"""Export helpers for MenuNest launch plans."""

from __future__ import annotations

import json
from typing import Any


def launch_plan_to_json(data: dict[str, Any]) -> str:
    """Return a pretty JSON export string."""
    return json.dumps(data, indent=2, ensure_ascii=False)


def launch_plan_to_markdown(data: dict[str, Any]) -> str:
    """Render a launch plan as Markdown."""
    lines: list[str] = []
    lines.append("# MenuNest Launch Report")
    lines.append("")
    lines.append("## Business Summary")
    lines.append(data["business_summary"])
    lines.append("")
    lines.append("## Positioning")
    lines.append(data["positioning"])
    lines.append("")
    lines.append("## Launch Dashboard")
    lines.append(f"- Launch readiness score: {data['launch_readiness_score']}/100")
    lines.append(f"- Estimated complexity: {data['estimated_complexity']}")
    lines.append(f"- Best customer segment: {data['best_customer_segment']}")
    lines.append("")
    lines.append("## Key Recommendation")
    lines.append(data["key_recommendation"])
    lines.append("")
    lines.append("## Main Risks")
    for risk in data["main_risks"]:
        lines.append(f"- {risk}")
    lines.append("")
    lines.append("## Next Steps")
    for step in data["next_steps"]:
        lines.append(f"- {step}")
    lines.append("")
    lines.append("## Menu and Pricing")
    for item in data["menu_items"]:
        lines.append(f"### {item['name']}")
        lines.append(f"- Category: {item['category']}")
        lines.append(f"- Description: {item['description']}")
        lines.append(f"- Complexity: {item['complexity']}")
        lines.append(f"- Suggested price: {item['suggested_price']}")
        lines.append(f"- Pricing note: {item['pricing_note']}")
        lines.append(f"- Ingredients: {', '.join(item['ingredients'])}")
        lines.append(f"- Allergens: {', '.join(item['allergens'])}")
        lines.append(f"- Preparation note: {item['preparation_note']}")
        lines.append(f"- Operational tip: {item['operational_tip']}")
        lines.append("")
    lines.append("## Customer Personas")
    for persona in data["customer_personas"]:
        lines.append(f"### {persona['name']}")
        lines.append(f"- Profile: {persona['profile']}")
        lines.append(f"- Needs: {persona['needs']}")
        lines.append(f"- Recommended offer: {persona['recommended_offer']}")
        lines.append(f"- Marketing angle: {persona['marketing_angle']}")
        lines.append("")
    lines.append("## Marketing Content")
    marketing = data["marketing"]
    lines.append(f"- Slogan: {marketing['slogan']}")
    lines.append(f"- Instagram bio: {marketing['instagram_bio']}")
    lines.append("")
    lines.append("### Captions")
    for caption in marketing["captions"]:
        lines.append(f"- {caption}")
    lines.append("")
    lines.append("### Launch Announcement")
    lines.append(marketing["launch_announcement"])
    lines.append("")
    lines.append("## Launch Checklist")
    checklist = data["launch_checklist"]
    section_titles = {
        "before_launch": "Before launch",
        "menu_validation": "Menu validation",
        "marketing_setup": "Marketing setup",
        "operations": "Operations",
        "first_week_testing": "First-week testing",
    }
    for key, title in section_titles.items():
        lines.append(f"### {title}")
        for task in checklist[key]:
            lines.append(f"- [ ] {task}")
        lines.append("")
    lines.append("## Disclaimer")
    lines.append(
        "This report is a starting point and should be validated with real costs, "
        "local regulations, supplier information, and customer feedback."
    )
    lines.append("")
    return "\n".join(lines)
