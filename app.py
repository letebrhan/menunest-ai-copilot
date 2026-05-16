"""MenuNest: AI Copilot for Food Entrepreneurs - Streamlit App."""

from __future__ import annotations

import time

import streamlit as st

from src.ai_generator import generate_launch_plan
from src.config import (
    APP_SUBTITLE,
    APP_TITLE,
    BUDGET_RANGES,
    BUSINESS_TYPES,
    CUISINE_OPTIONS,
    DEFAULT_INPUTS,
    DIETARY_OPTIONS,
    OUTPUT_LANGUAGES,
)
from src.report_renderer import render_dashboard, render_tabs
from src.styles import get_custom_css
from src.validators import validate_launch_plan


# Page configuration
st.set_page_config(
    page_title="MenuNest: AI Copilot for Food Entrepreneurs",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject custom CSS for responsive design and animations
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Header section with improved styling and animation
st.title("🍽️ MenuNest: AI Copilot for Food Entrepreneurs")
st.markdown(
    """
    <div class='hero-section'>
        <h3 style='margin-top: 0;'>Transform Your Food Business Idea Into a Launch Plan</h3>
        <p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>
            MenuNest helps food entrepreneurs turn a rough concept into a practical first launch plan
            with menu ideas, pricing guidance, customer personas, marketing content, and action checklists.
        </p>
        <p style='margin-bottom: 0;'>
            <strong>Perfect for:</strong> founders who want to validate a food concept before spending
            heavily on rent, equipment, inventory, or marketing.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar with hackathon context and demo controls
with st.sidebar:
    st.markdown("### 🏆 IBM Bob Hackathon Project")
    st.info(
        "**MenuNest** was built with **IBM Bob** as the AI-powered development partner, "
        "demonstrating how AI can accelerate product development from concept to demo."
    )

    st.markdown("### 🤖 How IBM Bob Helped")
    st.markdown("""
    <div class='sidebar-feature-list'>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>🎯</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Product Workflow Design</div>
                <div class='sidebar-feature-desc'>End-to-end planning and architecture</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>📁</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Repository Cleanup</div>
                <div class='sidebar-feature-desc'>Structure and organization</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>🎨</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Streamlit UI Prototype</div>
                <div class='sidebar-feature-desc'>Interactive interface design</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>⚙️</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Prompt Schema Design</div>
                <div class='sidebar-feature-desc'>AI prompt engineering</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>🐛</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Debugging & Optimization</div>
                <div class='sidebar-feature-desc'>Code quality improvements</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>📝</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Tests & Documentation</div>
                <div class='sidebar-feature-desc'>Quality assurance and guides</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📋 What MenuNest Generates")
    st.markdown("""
    <div class='sidebar-feature-list'>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>📊</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Overview</div>
                <div class='sidebar-feature-desc'>Summary and readiness score</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>🍽️</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Menu & Pricing</div>
                <div class='sidebar-feature-desc'>Items with price ranges</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>🥗</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Ingredients & Allergens</div>
                <div class='sidebar-feature-desc'>Preparation notes</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>👥</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Customers</div>
                <div class='sidebar-feature-desc'>Target personas</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>📱</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Marketing</div>
                <div class='sidebar-feature-desc'>Social media content</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>✅</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Launch Checklist</div>
                <div class='sidebar-feature-desc'>Action items</div>
            </div>
        </div>
        <div class='sidebar-feature-item'>
            <div class='sidebar-feature-icon'>📥</div>
            <div class='sidebar-feature-content'>
                <div class='sidebar-feature-title'>Export</div>
                <div class='sidebar-feature-desc'>Markdown or JSON</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ Demo Settings")
    use_demo = st.toggle("🔒 Use Stable Demo Mode", value=True)
    st.caption(
        "✅ **Recommended for live judging**\n\n"
        "Demo mode uses pre-validated sample data, ensuring reliable results "
        "without requiring external API keys or network access."
    )
    
    if not use_demo:
        st.warning(
            "⚠️ Live AI mode requires valid API credentials. "
            "Demo mode is recommended for hackathon presentations."
        )

    st.markdown("---")
    st.markdown("### 🎯 Demo Scenario")
    st.success(
        "**Ethiopian coffee & breakfast kiosk in Milan**\n\n"
        "A focused concept targeting morning commuters, students, and cultural food explorers."
    )

# Main input form
st.markdown("---")
st.header("📝 Describe Your Food Business Idea")
st.caption(
    "Fill in the details below to generate your personalized launch plan. "
    "The demo scenario is pre-filled—feel free to modify or use as-is."
)

with st.form("business_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🎯 Core Concept")
        business_idea = st.text_area(
            "Business Idea",
            value=DEFAULT_INPUTS["business_idea"],
            height=120,
            help="Describe your food business concept in 1-2 sentences",
        )
        business_type = st.selectbox(
            "Business Type",
            BUSINESS_TYPES,
            index=BUSINESS_TYPES.index(DEFAULT_INPUTS["business_type"]),
            help="Select the format that best matches your concept",
        )
        cuisine_selection = st.selectbox(
            "Cuisine Type",
            CUISINE_OPTIONS,
            index=CUISINE_OPTIONS.index(DEFAULT_INPUTS["cuisine"]),
            help="Select your cuisine type or choose 'Other / Custom' to specify your own",
        )
        
        # Show custom input field if "Other / Custom" is selected
        if cuisine_selection == "Other / Custom":
            cuisine = st.text_input(
                "Custom Cuisine Type",
                value="",
                placeholder="e.g., Korean BBQ, French Bistro, etc.",
                help="Specify your custom cuisine type",
            )
            if not cuisine or not cuisine.strip():
                cuisine = "Other / Custom"
        else:
            cuisine = cuisine_selection
        location = st.text_input(
            "Location",
            value=DEFAULT_INPUTS["location"],
            help="City or neighborhood where you plan to launch",
        )

    with col2:
        st.markdown("#### 💰 Budget & Goals")
        budget = st.selectbox(
            "Budget Range",
            BUDGET_RANGES,
            index=BUDGET_RANGES.index(DEFAULT_INPUTS["budget"]),
            help="Estimated startup budget for your first phase",
        )
        target_customers = st.text_area(
            "Target Customers",
            value=DEFAULT_INPUTS["target_customers"],
            height=90,
            help="Who are your ideal customers?",
        )
        dietary_focus = st.multiselect(
            "Dietary Focus",
            DIETARY_OPTIONS,
            default=DEFAULT_INPUTS["dietary_focus"],
            help="Select all that apply to your menu concept",
        )
        launch_goal = st.text_area(
            "Launch Goal",
            value=DEFAULT_INPUTS["launch_goal"],
            height=90,
            help="What do you want to achieve in the first month?",
        )
        output_language = st.selectbox(
            "Output Language",
            OUTPUT_LANGUAGES,
            index=OUTPUT_LANGUAGES.index(DEFAULT_INPUTS["output_language"]),
            help="Language for the generated launch plan",
        )

    st.markdown("---")
    submitted = st.form_submit_button(
        "🚀 Generate Launch Plan",
        use_container_width=True,
        type="primary",
    )

# Handle form submission and plan generation
if submitted:
    # Validate required fields
    if not business_idea or not business_idea.strip():
        st.error("❌ Please provide a business idea before generating the launch plan.")
    elif not cuisine or not cuisine.strip():
        st.error("❌ Please specify a cuisine type.")
    elif not location or not location.strip():
        st.error("❌ Please provide a location for your business.")
    else:
        # Collect user inputs
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

        # Show generation progress
        st.markdown("---")
        st.subheader("🔄 Generating Your Launch Plan...")
        
        progress_messages = [
            "🔍 Analyzing your business concept...",
            "🍽️ Creating menu suggestions...",
            "🥗 Building ingredient and allergen notes...",
            "💰 Estimating pricing ranges...",
            "👥 Creating customer personas...",
            "📱 Preparing marketing content...",
            "✅ Generating launch checklist...",
        ]

        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, message in enumerate(progress_messages, start=1):
            status_text.markdown(f"**{message}**")
            progress_bar.progress(i / len(progress_messages))
            time.sleep(0.2)

        # Generate the launch plan
        try:
            plan = generate_launch_plan(user_inputs, use_demo=use_demo)
            is_valid, validation_message = validate_launch_plan(plan)

            if not is_valid:
                st.error(
                    "❌ **Generation Error**\n\n"
                    "The generated launch plan did not pass validation. "
                    "Please try again or contact support."
                )
                with st.expander("🔍 View validation details"):
                    st.code(validation_message)
            else:
                # Clear progress indicators
                status_text.empty()
                progress_bar.empty()
                
                # Show success message
                st.success(
                    "✅ **Launch Plan Generated Successfully!**\n\n"
                    f"Your personalized plan is ready. Scroll down to explore the results."
                )
                
                # Render the dashboard and tabs
                st.markdown("---")
                render_dashboard(plan)
                st.markdown("---")
                render_tabs(plan)
                
        except Exception as e:
            st.error(
                f"❌ **Unexpected Error**\n\n"
                f"An error occurred during generation: {str(e)}\n\n"
                f"Please try again or enable Demo Mode in the sidebar."
            )

else:
    # Initial state - show helpful message
    st.info(
        "👆 **Ready to start?**\n\n"
        "Fill in your business details above and click **Generate Launch Plan** "
        "to receive your personalized food business strategy."
    )
    
    # Show a preview of what to expect
    with st.expander("📖 What will I receive?"):
        st.markdown("""
        Your generated launch plan will include:
        
        1. **📊 Launch Dashboard** - Key metrics and readiness score
        2. **📋 Business Overview** - Summary, positioning, and recommendations
        3. **🍽️ Menu & Pricing** - Suggested items with price ranges
        4. **🥗 Ingredients & Allergens** - Detailed preparation notes
        5. **👥 Customer Personas** - Target segments and marketing angles
        6. **📱 Marketing Content** - Ready-to-use social media copy
        7. **✅ Launch Checklist** - Step-by-step action items
        8. **📥 Export Options** - Download as Markdown or JSON
        
        All content is tailored to your specific business concept, location, and budget.
        """)
