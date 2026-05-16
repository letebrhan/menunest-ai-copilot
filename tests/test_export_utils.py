import json

from src.export_utils import launch_plan_to_json, launch_plan_to_markdown
from src.sample_data import SAMPLE_LAUNCH_PLAN


def test_markdown_export_contains_core_sections():
    markdown = launch_plan_to_markdown(SAMPLE_LAUNCH_PLAN)

    assert "# MenuNest Launch Report" in markdown
    assert "## Menu and Pricing" in markdown
    assert "## Launch Checklist" in markdown
    assert "Ethiopian Coffee" in markdown


def test_json_export_is_valid_json():
    raw_json = launch_plan_to_json(SAMPLE_LAUNCH_PLAN)
    parsed = json.loads(raw_json)

    assert parsed["launch_readiness_score"] == 72
    assert len(parsed["menu_items"]) >= 1
