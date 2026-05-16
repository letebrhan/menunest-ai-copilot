from src.sample_data import SAMPLE_LAUNCH_PLAN
from src.validators import validate_launch_plan


def test_sample_launch_plan_is_valid():
    is_valid, message = validate_launch_plan(SAMPLE_LAUNCH_PLAN)

    assert is_valid is True
    assert message == "Launch plan is valid."


def test_launch_readiness_score_must_be_valid():
    broken = dict(SAMPLE_LAUNCH_PLAN)
    broken["launch_readiness_score"] = 120

    is_valid, message = validate_launch_plan(broken)

    assert is_valid is False
    assert "less than or equal to 100" in message
