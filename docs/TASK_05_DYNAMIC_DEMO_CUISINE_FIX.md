# Task 5: Dynamic Demo Mode & Cuisine Input Improvements

**Date:** 2026-05-16
**Status:** ✅ Completed
**Focus:** Make demo mode respond to user inputs, improve cuisine selection, and implement dynamic readiness scoring

## Problem Statement

### Issues Identified

1. **Static Demo Mode**: When Stable Demo Mode was ON, changing business type, budget, dietary focus, or other form inputs still produced the same overview text about "An Ethiopian coffee and breakfast kiosk targeting Milan's morning commuters..." This made the app look static and unresponsive during judging.

2. **Limited Cuisine Input**: The "Cuisine Type" field was a plain text input with "Ethiopian / East African" as the default, providing no guidance on available options.

3. **Fixed Readiness Score**: The Launch Readiness score always stayed at 72/100 regardless of user inputs, making the dashboard appear static and unrealistic.

## Solution Overview

### Root Cause

The original implementation used a single static `SAMPLE_LAUNCH_PLAN` dictionary that was returned regardless of user inputs. The `generate_launch_plan()` function never adapted content to reflect user choices.

### Implementation

1. **Dynamic Demo Generation**: Created `generate_dynamic_demo_plan()` function that analyzes user inputs and generates appropriate content
2. **Cuisine Dropdown**: Added `CUISINE_OPTIONS` list with 11 options including "Other / Custom"
3. **Conditional Custom Input**: Show text input only when "Other / Custom" is selected
4. **Content Templates**: Built cuisine-specific templates for menu items, positioning, and marketing
5. **Dynamic Readiness Scoring**: Implemented multi-factor scoring algorithm that considers budget, complexity, clarity, and specificity
6. **Adaptive Dashboard**: Updated readiness labels to match score ranges (50-64: Needs validation, 65-79: Moderate, 80-90: Strong)

## Changes Made

### 1. Configuration Updates (`src/config.py`)

Added cuisine options:
- Ethiopian / East African
- Italian
- Mediterranean
- Middle Eastern
- Mexican
- Indian
- Asian Fusion
- Vegan / Plant-based
- Bakery / Pastry
- Coffee / Breakfast
- Other / Custom

### 2. UI Improvements (`app.py`)

Changed from text input to selectbox with conditional custom input field when "Other / Custom" is selected.

### 3. Dynamic Demo Generator (`src/sample_data.py`)

Created `generate_dynamic_demo_plan()` with helper functions:
- `_generate_menu_items()` - Cuisine-specific menus (Italian, Mexican, Indian, Vegan, etc.)
- `_generate_customer_personas()` - Adaptive personas based on target audience
- `_generate_marketing_content()` - Cuisine and location-specific marketing
- `_generate_launch_checklist()` - Business-type specific action items

Features:
- Detects default Ethiopian example and returns original sample
- Generates business summary from user inputs
- Adapts positioning based on cuisine type
- **Calculates dynamic readiness scores (50-90 range) based on 7 factors**
- Maps complexity by business type (Low/Medium/High)
- Creates contextual recommendations
- Generates 4-6 menu items per cuisine
- Builds 3 customer personas
- Creates marketing content with hashtags
- Generates 5-section launch checklist

### 4. Dynamic Readiness Scoring (`src/sample_data.py`)

Created `_calculate_readiness_score()` function with multi-factor algorithm:

**Scoring Factors:**
1. **Budget adequacy** (±15 points): Higher budgets increase readiness
2. **Business type complexity** (±10 points): Simpler businesses score higher
3. **Business idea clarity** (±8 points): Detailed descriptions score better
4. **Target customer specificity** (±7 points): Clear audience definition helps
5. **Launch goal clarity** (±5 points): Specific goals increase confidence
6. **Dietary focus** (±3 points): Shows market understanding
7. **Budget-complexity mismatch** (±10 points): Penalizes high-risk combinations

**Score Ranges:**
- 50-64: Needs validation (high risk, unclear concept)
- 65-79: Moderate (reasonable clarity, manageable complexity)
- 80-90: Strong (clear concept, good resources, lower complexity)

**Examples:**
- Restaurant + Under 5K EUR = ~55 (penalized for mismatch)
- Coffee kiosk + detailed inputs + 50K+ EUR = ~85 (optimal)
- Vague idea + no target + low budget = ~52 (needs work)

### 4. AI Generator Integration (`src/ai_generator.py`)

Updated to call `generate_dynamic_demo_plan(user_inputs)` instead of returning static `SAMPLE_LAUNCH_PLAN`.

### 5. Comprehensive Testing (`tests/test_dynamic_demo.py`)

Created 12 new tests:
- Default Ethiopian inputs return original sample
- Italian cuisine generates adapted content
- Mexican food truck generates appropriate recommendations
- Vegan cafe generates plant-based menu items
- Budget affects readiness scores
- Business type affects complexity
- Customer personas adapt to target audience
- Marketing content includes cuisine and location
- Launch checklist includes business specifics
- Integration with full generation pipeline
- Italian language output compatibility
- All required sections present and valid
- **Detailed inputs increase readiness score**
- **Restaurant with low budget gets penalized**
- **Simple businesses with low budget remain viable**
- **Scores stay within 50-90 bounds**
- **Dietary focus affects scoring**

## Test Results

All 53 tests pass (36 existing + 17 new):

```bash
$ python3 -m pytest tests/ -v
============================== 53 passed in 0.17s ==============================
```

**Readiness Score Tests:**
```bash
$ python3 -m pytest tests/test_dynamic_demo.py::TestReadinessScoreCalculation -v
============================== 5 passed in 0.03s ==============================
```

## Example Scenarios

### Italian Restaurant in Rome
- Readiness Score: 82 (higher budget + moderate complexity)
- Complexity: High (restaurant)
- Menu: Margherita Pizza, Pasta Carbonara
- Positioning: "Authentic Italian cuisine in Rome..."

### Mexican Food Truck in Barcelona
- Readiness Score: 75-78 (depends on input detail)
- Complexity: Medium (food truck)
- Menu: Tacos al Pastor, Guacamole & Chips
- Recommendation: "Launch with mobile operation to test locations..."

### Vegan Cafe in Berlin
- Menu: Buddha Bowl, Vegan Burger
- Positioning: "Plant-based excellence in Berlin..."
- Marketing: Emphasizes health and sustainability

## Benefits

### For Judges
- Interactive demo that responds to input changes
- Can test various business types and cuisines
- Professional, intelligent appearance
- No API keys required

### For Users
- Guided input with dropdown options
- Flexibility with custom cuisine option
- Relevant content matching their business idea
- Better UX than free-form text

### For Development
- Template-based approach is maintainable
- Comprehensive test coverage
- Easy to add new cuisines or business types
- All outputs pass validation

## Language Support

- Dynamic generation creates English content first
- Italian localization applied via `localize_demo_plan_to_italian()`
- JSON keys remain in English (for validation)
- User-facing text is translated
- Complexity values stay in English

## Validation

All generated plans pass validation:
- ✅ All 7 required sections present
- ✅ Menu items have required fields
- ✅ Complexity values are valid
- ✅ Readiness scores in range 0-100
- ✅ Descriptions meet minimum length
- ✅ Export to Markdown and JSON works
- ✅ Language localization preserves structure

## How to Test

### Test Dynamic Demo Mode
1. Start app: `streamlit run app.py`
2. Ensure "Use Stable Demo Mode" is ON
3. Change cuisine to "Italian", location to "Rome", business type to "Restaurant"
4. Generate plan and verify Italian-specific content

### Test Cuisine Dropdown
1. Click "Cuisine Type" dropdown
2. Select "Other / Custom"
3. Verify custom text input appears
4. Type "Korean BBQ" and generate plan

### Test Language Support
1. Change "Output Language" to "Italian"
2. Generate plan and verify Italian text
3. Switch to English and verify English text

## Security

- No API keys exposed or required
- All data generated locally
- No external API calls in demo mode
- User inputs sanitized through Streamlit

## Conclusion

This fix transforms demo mode from a static showcase into an interactive, responsive tool. The cuisine dropdown provides better UX, while dynamic generation ensures the app feels intelligent and personalized.

**Key Achievement:** Demo mode now generates different, contextually appropriate launch plans based on user inputs while maintaining 100% reliability without API keys.

**Test Coverage:** 53 tests passing, including 17 new tests for dynamic demo and readiness scoring.

**User Experience:** Judges can explore different business concepts and see the app adapt in real-time, making MenuNest feel like a true AI copilot.