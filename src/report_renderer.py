"""Streamlit rendering helpers for MenuNest."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.export_utils import launch_plan_to_json, launch_plan_to_markdown


def render_dashboard(plan: dict) -> None:
    """Render top-level launch dashboard cards."""
    st.header("Launch Dashboard")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Launch Readiness", f"{plan['launch_readiness_score']}/100")
    m2.metric("Menu Items", str(len(plan["menu_items"])))
    m3.metric("Complexity", plan["estimated_complexity"])
    m4.metric("Best Segment", plan["best_customer_segment"])


def render_tabs(plan: dict) -> None:
    """Render all launch-plan result tabs."""
    tabs = st.tabs(
        [
            "Overview",
            "Menu & Pricing",
            "Ingredients",
            "Customers",
            "Marketing",
            "Launch Checklist",
            "Export",
        ]
    )

    with tabs[0]:
        st.subheader("Business Summary")
        st.write(plan["business_summary"])

        st.subheader("Concept Positioning")
        st.write(plan["positioning"])

        st.subheader("Key Recommendation")
        st.info(plan["key_recommendation"])

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Main Risks")
            for risk in plan["main_risks"]:
                st.write(f"- {risk}")
        with col2:
            st.subheader("Next Steps")
            for step in plan["next_steps"]:
                st.write(f"- {step}")

    with tabs[1]:
        st.subheader("Menu and Pricing")
        rows = [
            {
                "Menu Item": item["name"],
                "Category": item["category"],
                "Description": item["description"],
                "Complexity": item["complexity"],
                "Suggested Price": item["suggested_price"],
                "Pricing Note": item["pricing_note"],
            }
            for item in plan["menu_items"]
        ]
        st.dataframe(pd.DataFrame(rows), use_container_width=True)
        st.caption(
            "Pricing is an approximate starting range and should be validated "
            "with real ingredient costs and customer testing."
        )

    with tabs[2]:
        st.subheader("Ingredients and Allergens")
        for item in plan["menu_items"]:
            with st.expander(item["name"]):
                st.write("Main ingredients:")
                for ingredient in item["ingredients"]:
                    st.write(f"- {ingredient}")

                st.write("Common allergens:")
                for allergen in item["allergens"]:
                    st.write(f"- {allergen}")

                st.write("Preparation note:")
                st.write(item["preparation_note"])

                st.write("Operational tip:")
                st.write(item["operational_tip"])

    with tabs[3]:
        st.subheader("Customer Personas")
        for persona in plan["customer_personas"]:
            with st.container(border=True):
                st.markdown(f"### {persona['name']}")
                st.write(f"**Profile:** {persona['profile']}")
                st.write(f"**Needs:** {persona['needs']}")
                st.write(f"**Recommended offer:** {persona['recommended_offer']}")
                st.write(f"**Marketing angle:** {persona['marketing_angle']}")

    with tabs[4]:
        st.subheader("Marketing Content")
        marketing = plan["marketing"]

        st.markdown("### Brand slogan")
        st.code(marketing["slogan"])

        st.markdown("### Instagram bio")
        st.text_area("Copy Instagram bio", marketing["instagram_bio"], height=100)

        st.markdown("### Social media captions")
        for index, caption in enumerate(marketing["captions"], start=1):
            st.text_area(f"Caption {index}", caption, height=80)

        st.markdown("### Launch announcement")
        st.text_area("Copy launch announcement", marketing["launch_announcement"], height=120)

    with tabs[5]:
        st.subheader("Launch Checklist")
        checklist = plan["launch_checklist"]
        sections = [
            ("Before launch", "before_launch"),
            ("Menu validation", "menu_validation"),
            ("Marketing setup", "marketing_setup"),
            ("Operations", "operations"),
            ("First-week testing", "first_week_testing"),
        ]
        for title, key in sections:
            st.markdown(f"### {title}")
            for task in checklist[key]:
                st.checkbox(task, value=True, key=f"{key}_{task}")

    with tabs[6]:
        st.subheader("Export Report")
        markdown_report = launch_plan_to_markdown(plan)
        json_report = launch_plan_to_json(plan)

        st.download_button(
            label="Download Markdown Report",
            data=markdown_report,
            file_name="menunest_launch_report.md",
            mime="text/markdown",
        )

        st.download_button(
            label="Download JSON Data",
            data=json_report,
            file_name="menunest_launch_plan.json",
            mime="application/json",
        )

        st.warning(
            "This report is a starting point and should be validated with real "
            "costs, local regulations, supplier information, and customer feedback."
        )
