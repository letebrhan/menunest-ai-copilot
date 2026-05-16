"""MenuNest Streamlit app."""

from __future__ import annotations

import time

import streamlit as st

from src.ai_generator import generate_launch_plan
from src.config import (
    APP_SUBTITLE,
    APP_TITLE,
    BUDGET_RANGES,
    BUSINESS_TYPES,
    DEFAULT_INPUTS,
    DIETARY_OPTIONS,
    OUTPUT_LANGUAGES,
)
from src.report_renderer import render_dashboard, render_tabs
from src.validators import validate_launch_plan


st.set_page_config(
    page_title="MenuNest",
    page_icon="🍽️",
    layout="wide",
)

st.title(APP_TITLE)
st.subheader(APP_SUBTITLE)
st.write(
    "Turn your food idea into a market-ready menu, pricing plan, "
    "marketing content, and launch checklist."
)
st.caption(
    "MenuNest helps food entrepreneurs test and shape a food business idea "
    "before spending heavily on rent, equipment, ingredients, and marketing."
)

with st.sidebar:
    st.markdown("### IBM Bob Hackathon Story")
    st.write(
        "MenuNest was built with IBM Bob as the AI-powered development partner."
    )

    st.markdown("### How IBM Bob helped")
    st.write("- Product workflow design")
    st.write("- Repository structure")
    st.write("- Streamlit prototype")
    st.write("- Prompt and schema design")
    st.write("- Debugging and UI polish")
    st.write("- Tests and documentation")

    st.markdown("### Demo scenario")
    st.write("Ethiopian coffee and breakfast kiosk in Milan.")

    st.markdown("### What MenuNest generates")
    st.write("- Menu and pricing ideas")
    st.write("- Ingredient and allergen notes")
    st.write("- Customer personas")
    st.write("- Marketing content")
    st.write("- Launch checklist")
    st.write("- Exportable launch report")

    st.markdown("### Demo reliability")
    use_demo = st.toggle("Use stable demo generation", value=True)
    st.caption("Recommended for live judging. No external API key is required.")

with st.form("business_form"):
    st.header("Describe your food business idea")

    col1, col2 = st.columns(2)

    with col1:
        business_idea = st.text_area(
            "Business idea",
            value=DEFAULT_INPUTS["business_idea"],
            height=120,
        )
        business_type = st.selectbox(
            "Business type",
            BUSINESS_TYPES,
            index=BUSINESS_TYPES.index(DEFAULT_INPUTS["business_type"]),
        )
        cuisine = st.text_input("Cuisine type", value=DEFAULT_INPUTS["cuisine"])
        location = st.text_input("Location", value=DEFAULT_INPUTS["location"])

    with col2:
        budget = st.selectbox(
            "Budget range",
            BUDGET_RANGES,
            index=BUDGET_RANGES.index(DEFAULT_INPUTS["budget"]),
        )
        target_customers = st.text_area(
            "Target customers",
            value=DEFAULT_INPUTS["target_customers"],
            height=90,
        )
        dietary_focus = st.multiselect(
            "Dietary focus",
            DIETARY_OPTIONS,
            default=DEFAULT_INPUTS["dietary_focus"],
        )
        launch_goal = st.text_area(
            "Launch goal",
            value=DEFAULT_INPUTS["launch_goal"],
            height=90,
        )
        output_language = st.selectbox(
            "Output language",
            OUTPUT_LANGUAGES,
            index=OUTPUT_LANGUAGES.index(DEFAULT_INPUTS["output_language"]),
        )

    submitted = st.form_submit_button("Generate Launch Plan", use_container_width=True)

if submitted:
    user_inputs = {
        "business_idea": business_idea,
        "business_type": business_type,
        "cuisine": cuisine,
        "location": location,
        "budget": budget,
        "target_customers": target_customers,
        "dietary_focus": dietary_focus,
        "launch_goal": launch_goal,
        "output_language": output_language,
    }

    progress_messages = [
        "Analyzing business idea...",
        "Creating menu suggestions...",
        "Building ingredient plan...",
        "Estimating pricing ranges...",
        "Creating customer personas...",
        "Preparing marketing content...",
        "Generating launch checklist...",
    ]

    progress = st.progress(0)
    status = st.empty()
    for i, message in enumerate(progress_messages, start=1):
        status.write(message)
        progress.progress(i / len(progress_messages))
        time.sleep(0.15)

    plan = generate_launch_plan(user_inputs, use_demo=use_demo)
    is_valid, validation_message = validate_launch_plan(plan)

    if not is_valid:
        st.error("The generated launch plan is not valid.")
        st.code(validation_message)
    else:
        status.empty()
        progress.empty()
        st.success("Launch plan generated.")
        render_dashboard(plan)
        render_tabs(plan)
else:
    st.info("Describe your food business idea above, then click Generate Launch Plan.")
