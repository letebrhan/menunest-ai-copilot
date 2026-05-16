"""Streamlit rendering helpers for MenuNest."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.export_utils import launch_plan_to_json, launch_plan_to_markdown


def render_dashboard(plan: dict) -> None:
    """Render top-level launch dashboard cards with responsive design."""
    st.header("📊 Launch Dashboard")
    st.caption("Key metrics for your food business concept")
    
    # Use responsive columns that stack on mobile
    m1, m2, m3, m4 = st.columns(4)
    
    readiness_score = plan['launch_readiness_score']
    
    # Determine readiness label and color based on score
    if readiness_score >= 80:
        readiness_label = "Strong"
        readiness_color = "🟢"
    elif readiness_score >= 65:
        readiness_label = "Moderate"
        readiness_color = "🟡"
    else:
        readiness_label = "Needs validation"
        readiness_color = "🔴"
    
    # Metrics with improved responsive text handling
    m1.metric(
        "Launch Readiness",
        f"{readiness_score}/100",
        help="Overall readiness score based on budget, business complexity, concept clarity, and market understanding"
    )
    m1.markdown(f"<div style='text-align: center; font-weight: 600;'>{readiness_color} {readiness_label}</div>", unsafe_allow_html=True)
    
    m2.metric(
        "Menu Items",
        str(len(plan["menu_items"])),
        help="Number of suggested menu items for your launch"
    )
    
    m3.metric(
        "Complexity",
        plan["estimated_complexity"],
        help="Operational complexity level for your concept"
    )
    
    # Best segment with text wrapping support
    best_segment = plan["best_customer_segment"]
    # Truncate if too long for better mobile display
    display_segment = best_segment if len(best_segment) <= 25 else best_segment[:22] + "..."
    m4.metric(
        "Best Segment",
        display_segment,
        help=f"Primary target customer segment: {best_segment}"
    )


def render_tabs(plan: dict) -> None:
    """Render all launch-plan result tabs with animations."""
    # Add a subtle animation trigger for tab content
    st.markdown(
        """
        <script>
        // Trigger animation when tabs change
        const observer = new MutationObserver(() => {
            const panels = document.querySelectorAll('[data-baseweb="tab-panel"]');
            panels.forEach(panel => {
                if (panel.style.display !== 'none') {
                    panel.style.animation = 'slideIn 0.4s ease-out';
                }
            });
        });
        observer.observe(document.body, { childList: true, subtree: true });
        </script>
        """,
        unsafe_allow_html=True,
    )
    
    tabs = st.tabs(
        [
            "📋 Overview",
            "🍽️ Menu & Pricing",
            "🥗 Ingredients & Allergens",
            "👥 Customers",
            "📱 Marketing",
            "📋 Launch Checklist",
            "📥 Export",
        ]
    )

    # Tab 0: Overview
    with tabs[0]:
        st.subheader("📋 Business Overview")
        
        with st.container(border=True):
            st.markdown("#### Business Summary")
            st.write(plan["business_summary"])

        with st.container(border=True):
            st.markdown("#### Concept Positioning")
            st.write(plan["positioning"])

        st.markdown("#### 💡 Key Recommendation")
        st.info(plan["key_recommendation"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### ⚠️ Main Risks")
            for risk in plan["main_risks"]:
                st.markdown(f"- {risk}")
        with col2:
            st.markdown("#### 🎯 Next Steps")
            for step in plan["next_steps"]:
                st.markdown(f"- {step}")

    # Tab 1: Menu & Pricing
    with tabs[1]:
        st.subheader("🍽️ Menu and Pricing Strategy")
        st.caption(f"Suggested menu with {len(plan['menu_items'])} items tailored to your concept")
        
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
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        
        st.info(
            "💡 **Pricing Guidance:** These are approximate starting ranges. "
            "Validate with real ingredient costs, competitor pricing, and customer testing before launch."
        )

    # Tab 2: Ingredients & Allergens
    with tabs[2]:
        st.subheader("🥗 Ingredients and Allergen Information")
        st.caption("Detailed preparation notes and allergen warnings for each menu item")
        
        for item in plan["menu_items"]:
            with st.expander(f"🍴 {item['name']}", expanded=False):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Main Ingredients:**")
                    for ingredient in item["ingredients"]:
                        st.markdown(f"- {ingredient}")
                    
                    st.markdown("**Common Allergens:**")
                    for allergen in item["allergens"]:
                        st.markdown(f"- ⚠️ {allergen}")
                
                with col2:
                    st.markdown("**Preparation Note:**")
                    st.write(item["preparation_note"])
                    
                    st.markdown("**Operational Tip:**")
                    st.write(item["operational_tip"])

    # Tab 3: Customer Personas
    with tabs[3]:
        st.subheader("👥 Customer Personas")
        st.caption("Target customer segments and how to reach them")
        
        for persona in plan["customer_personas"]:
            with st.container(border=True):
                st.markdown(f"### {persona['name']}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Profile:** {persona['profile']}")
                    st.markdown(f"**Needs:** {persona['needs']}")
                with col2:
                    st.markdown(f"**Recommended Offer:** {persona['recommended_offer']}")
                    st.markdown(f"**Marketing Angle:** {persona['marketing_angle']}")

    # Tab 4: Marketing Content
    with tabs[4]:
        st.subheader("📱 Marketing Content")
        st.caption("Ready-to-use marketing copy for social media and launch campaigns")
        
        marketing = plan["marketing"]

        st.markdown("### 🎯 Brand Slogan")
        st.code(marketing["slogan"], language=None)

        st.markdown("### 📸 Instagram Bio")
        st.text_area(
            "Copy and paste this bio to your Instagram profile:",
            marketing["instagram_bio"],
            height=100,
            key="instagram_bio",
        )

        st.markdown("### 📝 Social Media Captions")
        st.caption("Use these captions for your launch posts")
        for index, caption in enumerate(marketing["captions"], start=1):
            st.text_area(
                f"Caption {index}",
                caption,
                height=80,
                key=f"caption_{index}",
            )

        st.markdown("### 📢 Launch Announcement")
        st.text_area(
            "Copy this launch announcement:",
            marketing["launch_announcement"],
            height=120,
            key="launch_announcement",
        )

    # Tab 5: Launch Checklist
    with tabs[5]:
        st.subheader("📋 Launch Checklist")
        st.caption("Step-by-step action items to prepare for your launch")
        
        checklist = plan["launch_checklist"]
        sections = [
            ("🚀 Before Launch", "before_launch"),
            ("🍽️ Menu Validation", "menu_validation"),
            ("📱 Marketing Setup", "marketing_setup"),
            ("⚙️ Operations", "operations"),
            ("📊 First-Week Testing", "first_week_testing"),
        ]
        
        for title, key in sections:
            with st.expander(title, expanded=True):
                for idx, task in enumerate(checklist[key]):
                    st.checkbox(task, value=False, key=f"{key}_{idx}")

    # Tab 6: Export
    with tabs[6]:
        st.subheader("📥 Export Your Launch Plan")
        st.caption("Download your complete launch plan in different formats")
        
        markdown_report = launch_plan_to_markdown(plan)
        json_report = launch_plan_to_json(plan)

        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📄 Markdown Report")
            st.write("Human-readable format, perfect for documentation and sharing")
            st.download_button(
                label="📥 Download Markdown Report",
                data=markdown_report,
                file_name="menunest_launch_report.md",
                mime="text/markdown",
                use_container_width=True,
            )
        
        with col2:
            st.markdown("#### 📊 JSON Data")
            st.write("Structured data format for integration with other tools")
            st.download_button(
                label="📥 Download JSON Data",
                data=json_report,
                file_name="menunest_launch_plan.json",
                mime="application/json",
                use_container_width=True,
            )

        st.warning(
            "⚠️ **Important Disclaimer:** This launch plan is a starting point generated by AI. "
            "Always validate with real costs, local regulations, supplier information, and customer feedback "
            "before making business decisions."
        )
