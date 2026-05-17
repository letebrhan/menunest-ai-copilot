"""Fallback demo data for MenuNest.

This module provides realistic, validated sample launch plans that adapt to user inputs.
The data is used in demo mode to ensure reliable operation during presentations
and when API access is unavailable.
"""

import re
from typing import Any

SAMPLE_LAUNCH_PLAN = {
    "business_summary": (
        "An Ethiopian coffee and breakfast kiosk targeting Milan's morning commuters, "
        "university students, and office workers seeking authentic, affordable, and "
        "culturally rich breakfast options. The concept focuses on 5-6 signature items "
        "that can be prepared efficiently during the morning rush while introducing "
        "customers to traditional East African flavors."
    ),
    "positioning": (
        "The only authentic Ethiopian breakfast experience in Milan's business districts, "
        "offering traditional coffee ceremony quality in a fast-casual format. Positioned "
        "between generic coffee chains (lacking authenticity) and sit-down restaurants "
        "(too slow for commuters), filling a gap for cultural food explorers and "
        "time-conscious professionals seeking something beyond the usual cornetto and cappuccino."
    ),
    "launch_readiness_score": 72,
    "estimated_complexity": "Medium",
    "best_customer_segment": "Morning commuters aged 25-45",
    "key_recommendation": (
        "Launch with a mobile cart or temporary kiosk near Porta Garibaldi or Centrale "
        "station for 4-6 weeks to validate demand and refine operations before committing "
        "to a fixed location lease. Focus on perfecting 3 core items (coffee, sambusa, "
        "and one breakfast bowl) before expanding the menu. This approach minimizes risk "
        "while building a customer base and gathering real pricing data."
    ),
    "main_risks": [
        "Limited brand awareness of Ethiopian breakfast culture in Milan may require significant customer education",
        "Morning rush operational pressure with complex prep work could lead to quality inconsistency or long wait times",
        "Ingredient sourcing challenges for authentic spices and teff flour may increase costs or require substitutions",
        "Seasonal demand fluctuations during summer holidays and August closures typical in Milan",
    ],
    "next_steps": [
        "Conduct taste tests with 30-50 potential customers near target locations to validate menu appeal and gather pricing feedback",
        "Source ingredients from African specialty stores in Milan (Via Padova area) and calculate exact cost per portion for each menu item",
        "Create a simple Instagram presence with 10-15 posts showing food preparation, cultural context, and customer testimonials before launch",
        "Develop a 2-hour morning prep checklist and test it for 3 days to identify bottlenecks and optimize workflow",
    ],
    "menu_items": [
        {
            "name": "Ethiopian Coffee (Buna)",
            "category": "Drink",
            "description": "Rich, aromatic coffee prepared using traditional Ethiopian methods with optional cardamom spice.",
            "complexity": "Low",
            "suggested_price": "2.50-3.50 EUR",
            "pricing_note": "Price competitively with specialty coffee shops (2.80-3.20 EUR range) while emphasizing authenticity and cultural experience.",
            "ingredients": ["Ethiopian coffee beans", "Water", "Cardamom (optional)", "Sugar (optional)"],
            "allergens": ["None common"],
            "preparation_note": "Roast beans fresh daily if possible, or source pre-roasted from African specialty stores. Brew in traditional jebena pot or use French press for speed.",
            "operational_tip": "Prepare in batches of 8-10 servings during morning rush (7-9 AM). Offer small tasting cups to curious customers to build interest.",
        },
        {
            "name": "Spiced Tea (Shai)",
            "category": "Drink",
            "description": "Warming black tea infused with cinnamon, ginger, and cloves, served with or without milk.",
            "complexity": "Low",
            "suggested_price": "2.50-3.00 EUR",
            "pricing_note": "Position as a premium alternative to standard tea, highlighting the spice blend as a unique selling point.",
            "ingredients": ["Black tea", "Water", "Cinnamon", "Ginger", "Cloves", "Milk (optional)", "Sugar (optional)"],
            "allergens": ["Milk (if added)"],
            "preparation_note": "Pre-mix dry spices in bulk to save time. Steep tea for 3-4 minutes for optimal flavor without bitterness.",
            "operational_tip": "Default to dairy-free unless requested. Keep oat milk as an alternative for lactose-intolerant customers.",
        },
        {
            "name": "Sambusa (Lentil)",
            "category": "Snack",
            "description": "Crispy triangular pastry filled with spiced lentils, onions, and jalapeño, served hot.",
            "complexity": "Medium",
            "suggested_price": "2.80-3.50 EUR",
            "pricing_note": "Price per piece or offer 2-for-5 EUR combo. Strong margin item if prep is efficient.",
            "ingredients": ["Wheat flour", "Lentils", "Onion", "Jalapeño", "Garlic", "Cumin", "Turmeric", "Vegetable oil"],
            "allergens": ["Gluten", "May contain traces of sesame"],
            "preparation_note": "Prepare filling the night before. Assemble and fry fresh each morning. Can be kept warm for 2-3 hours maximum.",
            "operational_tip": "Track waste carefully—fried items lose quality after 3 hours. Start with 20-30 pieces and adjust based on demand patterns.",
        },
        {
            "name": "Ful Medames Bowl",
            "category": "Breakfast",
            "description": "Hearty fava bean stew with tomatoes, onions, and olive oil, served with fresh bread for dipping.",
            "complexity": "Medium",
            "suggested_price": "6.50-8.00 EUR",
            "pricing_note": "Position as a filling, protein-rich breakfast alternative to pastries. Target students and budget-conscious workers.",
            "ingredients": ["Fava beans", "Tomatoes", "Onion", "Garlic", "Olive oil", "Lemon juice", "Cumin", "Fresh bread"],
            "allergens": ["Gluten (bread)", "May contain traces of sesame"],
            "preparation_note": "Cook beans in large batches (can be refrigerated for 3 days). Reheat individual portions and finish with fresh toppings.",
            "operational_tip": "Offer small (5 EUR) and regular (7 EUR) sizes. Small size has better margins and reduces waste for uncertain demand.",
        },
        {
            "name": "Firfir Breakfast",
            "category": "Breakfast",
            "description": "Torn pieces of injera mixed with spiced berbere sauce and scrambled eggs, a traditional morning dish.",
            "complexity": "Medium",
            "suggested_price": "7.00-8.50 EUR",
            "pricing_note": "Premium breakfast item. Requires customer education but has high perceived value for cultural food explorers.",
            "ingredients": ["Injera", "Eggs", "Berbere spice", "Onion", "Tomato", "Olive oil", "Fresh herbs"],
            "allergens": ["Eggs", "Gluten (injera)", "Spicy (berbere)"],
            "preparation_note": "Pre-tear injera and store in airtight container. Cook eggs fresh to order (2-3 minutes per portion).",
            "operational_tip": "Start offering this after week 2 once coffee and sambusa are running smoothly. Requires more explanation to customers.",
        },
        {
            "name": "Shiro Wat Bowl",
            "category": "Breakfast",
            "description": "Creamy chickpea flour stew with Ethiopian spices, served with injera or bread.",
            "complexity": "Medium",
            "suggested_price": "6.00-7.50 EUR",
            "pricing_note": "Excellent vegetarian/vegan option with good margins. Chickpea flour is affordable and shelf-stable.",
            "ingredients": ["Chickpea flour", "Onion", "Garlic", "Berbere spice", "Tomato", "Vegetable oil", "Injera or bread"],
            "allergens": ["Gluten (if served with injera/bread)", "Spicy (berbere)"],
            "preparation_note": "Can be prepared in large batches and reheated. Consistency should be thick but pourable.",
            "operational_tip": "Highlight as vegan and protein-rich. Popular with health-conscious customers and vegetarians.",
        },
    ],
    "customer_personas": [
        {
            "name": "Marco - The Daily Commuter",
            "profile": "35-year-old marketing manager who takes the metro from Porta Garibaldi to his office near Duomo. Arrives at station around 7:45 AM, needs breakfast before 8:15 AM. Values convenience and consistency.",
            "needs": "Fast service (under 3 minutes), portable packaging, familiar enough to trust but interesting enough to try, reasonable price for daily purchase (under 6 EUR).",
            "recommended_offer": "Coffee + Sambusa combo for 5.50 EUR. Quick, portable, and becomes a daily ritual.",
            "marketing_angle": "Skip the usual cornetto—try something bold and authentic that fits your morning routine. Same speed, better story.",
        },
        {
            "name": "Sofia - The University Student",
            "profile": "22-year-old economics student at Bocconi University. Budget-conscious but interested in healthy, filling food. Often skips breakfast due to cost or lack of appealing options near campus.",
            "needs": "Affordable (under 7 EUR), filling enough to last until lunch, vegetarian-friendly, Instagram-worthy for social sharing.",
            "recommended_offer": "Ful Medames Bowl (small size) for 6.50 EUR or Shiro Wat Bowl for 6.00 EUR. Both are filling, affordable, and photogenic.",
            "marketing_angle": "Real breakfast that keeps you full through morning lectures. Vegan, protein-rich, and under 7 EUR. Your wallet and your body will thank you.",
        },
        {
            "name": "Alessandro & Chiara - The Cultural Explorers",
            "profile": "28 and 30-year-old couple who actively seek authentic international food experiences. Follow food bloggers, try new restaurants monthly, and share discoveries on social media. Willing to pay premium for authenticity.",
            "needs": "Authentic story and cultural context, unique flavors they can't find elsewhere, photo opportunities, friendly staff who can explain the food.",
            "recommended_offer": "Coffee ceremony experience + Firfir breakfast for 10-12 EUR. Premium positioning with cultural education.",
            "marketing_angle": "Experience Ethiopian breakfast culture without flying to Addis Ababa. Traditional recipes, authentic ingredients, and a story worth sharing.",
        },
    ],
    "marketing": {
        "slogan": "Ethiopian mornings, Milan style—authentic breakfast for your daily routine.",
        "instagram_bio": (
            "🇪🇹 Authentic Ethiopian breakfast in Milan | Traditional coffee, warm sambusa & cultural flavors | "
            "📍 Porta Garibaldi (coming soon) | DM for catering"
        ),
        "captions": [
            "That moment when you realize Milan's been missing authentic Ethiopian breakfast. We're fixing that. 🇪🇹☕ #EthiopianCoffee #MilanFood #BreakfastGoals",
            "Forget the usual cornetto. Try sambusa—crispy, spiced, and ready to change your morning routine. Available soon near Porta Garibaldi. 🥟✨",
            "Ethiopian coffee isn't just a drink, it's a ceremony. We're bringing that tradition to your Milan mornings. Who's ready? ☕🇪🇹 #CoffeeCulture #MilanBreakfast",
        ],
        "launch_announcement": (
            "Launch strategy: Start with a 4-week mobile cart test near Porta Garibaldi station (high foot traffic, "
            "morning commuters). Focus on 3 core items: coffee, sambusa, and one breakfast bowl. Offer a 'First Week Special' "
            "combo (coffee + sambusa for 5 EUR) to drive trial. Collect customer feedback daily and adjust menu/pricing "
            "based on real data before committing to a permanent location. Use Instagram stories to build anticipation "
            "and announce daily location/hours."
        ),
    },
    "launch_checklist": {
        "before_launch": [
            "Finalize 3-5 core menu items based on ingredient availability and prep complexity",
            "Calculate exact ingredient cost per item using prices from African specialty stores in Via Padova area",
            "Create clear allergen labels in Italian and English for all menu items",
            "Test packaging solutions for portability and heat retention (critical for morning commuters)",
            "Secure necessary permits for mobile cart operation in target area",
        ],
        "menu_validation": [
            "Conduct taste tests with 30-50 people near target location (mix of commuters, students, and food enthusiasts)",
            "Test 2-3 price points for each item to find optimal balance between affordability and margin",
            "Identify top 3 items based on taste feedback, preparation speed, and ingredient cost",
            "Validate that prep time for all items fits within 2-hour morning setup window",
        ],
        "marketing_setup": [
            "Create Instagram account with 10-15 pre-launch posts showing food prep, cultural context, and behind-the-scenes",
            "Design simple menu board with photos, prices, and allergen symbols (visual communication is key for international customers)",
            "Prepare 3-5 key phrases in Italian to explain menu items to curious customers",
            "Create Google Business profile once location is confirmed (critical for local search visibility)",
        ],
        "operations": [
            "Develop detailed 2-hour morning prep checklist with time estimates for each task",
            "Test complete workflow for 3 consecutive days to identify bottlenecks and optimize sequence",
            "Set daily ingredient purchase limits based on realistic sales projections (start conservative to minimize waste)",
            "Create simple point-of-sale system (even if just a phone calculator and notebook) to track sales by item",
            "Establish backup plan for equipment failure (know where to get emergency supplies)",
        ],
        "first_week_testing": [
            "Track sales by item, hour, and day to identify demand patterns and peak times",
            "Collect structured feedback from at least 50 customers (what they liked, what confused them, price perception)",
            "Monitor prep time vs. service time to identify operational inefficiencies",
            "Calculate actual food cost percentage for each item and compare to projections",
            "Adjust menu, pricing, or operations based on real data before week 2",
        ],
    },
}


def clean_business_idea(business_idea: str) -> str:
    """Clean and normalize business idea text for professional output.
    
    This function:
    1. Removes common greetings (Hi, Hello, Hey, etc.)
    2. Removes personal introductions (I am [Name], My name is [Name])
    3. Removes request fillers (please help me, could you help me, etc.)
    4. Normalizes common typos (resturan->restaurant, barkery->bakery)
    5. Normalizes whitespace and newlines
    6. Removes filler phrases like "I want to", "I would like to"
    7. Returns a clean, professional concept description
    
    Args:
        business_idea: Raw business idea text from user input
        
    Returns:
        Cleaned business idea text suitable for professional output
    """
    if not business_idea:
        return ""
    
    # Normalize whitespace and newlines to single spaces
    cleaned = re.sub(r'\s+', ' ', business_idea.strip())
    
    # Remove common greetings at the start (case-insensitive)
    greetings = [
        r'^hi[,\s]+',
        r'^hello[,\s]+',
        r'^hey[,\s]+',
        r'^greetings[,\s]+',
        r'^good\s+(morning|afternoon|evening)[,\s]+',
        r'^dear[,\s]+',
    ]
    for greeting in greetings:
        cleaned = re.sub(greeting, '', cleaned, flags=re.IGNORECASE)
    
    # Remove personal introductions (I am [Name], My name is [Name])
    personal_intros = [
        r'^i\s+am\s+[a-zA-Z]+[,.\s]+',
        r'^my\s+name\s+is\s+[a-zA-Z]+[,.\s]+',
        r'^this\s+is\s+[a-zA-Z]+[,.\s]+',
    ]
    for intro in personal_intros:
        cleaned = re.sub(intro, '', cleaned, flags=re.IGNORECASE)
    
    # Remove request fillers (please help me, could you help me, etc.)
    request_fillers = [
        r'^please\s+could\s+you\s+help\s+me\s+(to\s+)?',
        r'^could\s+you\s+(please\s+)?help\s+me\s+(to\s+)?',
        r'^please\s+help\s+me\s+(to\s+)?',
        r'^can\s+you\s+(please\s+)?help\s+me\s+(to\s+)?',
        r'^i\s+need\s+help\s+(to\s+)?',
        r'^i\s+want\s+you\s+to\s+',
        r'^please\s+',
    ]
    for filler in request_fillers:
        cleaned = re.sub(filler, '', cleaned, flags=re.IGNORECASE)
    
    # Remove action filler phrases that don't add value
    filler_phrases = [
        r'^i\s+want\s+to\s+',
        r'^i\s+would\s+like\s+to\s+',
        r'^i\s+am\s+planning\s+to\s+',
        r'^i\s+plan\s+to\s+',
        r'^i\s+wish\s+to\s+',
        r'^my\s+idea\s+is\s+to\s+',
        r'^the\s+idea\s+is\s+to\s+',
        r'^i\s+am\s+thinking\s+(of|about)\s+',
        r'^i\s+am\s+considering\s+',
        r'^launch\s+an?\s+',  # Remove "Launch a" or "Launch an"
        r'^start\s+an?\s+',   # Remove "Start a" or "Start an"
        r'^open\s+an?\s+',    # Remove "Open a" or "Open an"
        r'^create\s+an?\s+',  # Remove "Create a" or "Create an"
    ]
    for phrase in filler_phrases:
        cleaned = re.sub(phrase, '', cleaned, flags=re.IGNORECASE)
    
    # Normalize common typos (case-insensitive word boundary matching)
    typo_corrections = {
        r'\bresturan\b': 'restaurant',
        r'\bresturant\b': 'restaurant',
        r'\brestaurant\b': 'restaurant',  # Keep correct spelling
        r'\bbarkery\b': 'bakery',
        r'\bbakery\b': 'bakery',  # Keep correct spelling
        r'\bbussiness\b': 'business',
        r'\bbusines\b': 'business',
        r'\bbusiness\b': 'business',  # Keep correct spelling
        r'\bcafe\b': 'cafe',  # Normalize
        r'\bcaffe\b': 'cafe',
        r'\bcoffe\b': 'coffee',
        r'\bcoffee\b': 'coffee',  # Keep correct spelling
    }
    for typo, correction in typo_corrections.items():
        cleaned = re.sub(typo, correction, cleaned, flags=re.IGNORECASE)
    
    # Remove any remaining leading/trailing punctuation or whitespace
    cleaned = cleaned.strip(' .,;:')
    
    # Capitalize first letter if needed
    if cleaned and cleaned[0].islower():
        cleaned = cleaned[0].upper() + cleaned[1:]
    
    # Ensure it ends with proper punctuation
    if cleaned and cleaned[-1] not in '.!?':
        cleaned += '.'
    
    return cleaned.strip()


def extract_concept_snippet(business_idea: str, max_words: int = 8) -> str:
    """Extract a short snippet from business idea for use in text.
    
    This avoids showing Python list syntax or overly long text in generated content.
    
    Args:
        business_idea: Cleaned business idea text
        max_words: Maximum number of words to include
        
    Returns:
        Short, professional snippet of the concept
    """
    if not business_idea:
        return "this concept"
    
    # Clean the idea first
    cleaned = clean_business_idea(business_idea)
    
    # Split into words and take first N words
    words = cleaned.split()
    if len(words) <= max_words:
        return cleaned.rstrip('.')
    
    # Take first max_words and add ellipsis
    snippet = ' '.join(words[:max_words])
    return snippet.rstrip('.') + '...'


def create_display_concept(business_idea: str) -> str:
    """Create a natural display concept from the business idea.
    
    This function converts raw business ideas into professional display text
    suitable for use in sentences like "For your [display concept]:" or
    "This [display concept] targets..."
    
    Examples:
        "I want to launch an Ethiopian coffee kiosk" → "Ethiopian coffee kiosk"
        "Launch a vegan bakery in Rome" → "vegan bakery in Rome"
        "Open an Italian restaurant" → "Italian restaurant"
    
    Args:
        business_idea: Raw or cleaned business idea text
        
    Returns:
        Natural display concept without awkward prefixes
    """
    if not business_idea:
        return "concept"
    
    # Clean the idea first (removes "I want to", "Launch a", etc.)
    cleaned = clean_business_idea(business_idea)
    
    # Remove trailing period for use in sentences
    display = cleaned.rstrip('.')
    
    # Ensure it starts with lowercase unless it's a proper noun
    # Check if first word looks like a proper noun (capitalized and not at sentence start)
    words = display.split()
    if words and len(words) > 1:
        # If first word is capitalized but second word isn't, it might be a proper noun
        # Keep it capitalized. Otherwise, lowercase it for natural flow.
        if words[0][0].isupper() and (len(words) < 2 or not words[1][0].isupper()):
            # Looks like a proper noun (e.g., "Ethiopian coffee kiosk")
            pass
        else:
            # Generic concept, lowercase first word
            display = display[0].lower() + display[1:] if len(display) > 1 else display.lower()
    elif words:
        # Single word, lowercase it unless it's clearly a proper noun
        # For simplicity, keep single words as-is
        pass
    
    return display



def generate_dynamic_demo_plan(user_inputs: dict[str, Any]) -> dict[str, Any]:
    """Generate a demo launch plan that adapts to user inputs.
    
    This function creates realistic demo data based on the user's form inputs,
    with the Business Idea field as the PRIMARY driver of the generated content.
    The other fields (cuisine, location, etc.) provide supporting context.
    
    Args:
        user_inputs: Dictionary containing business concept details
        
    Returns:
        Launch plan dictionary adapted to user inputs
    """
    business_idea_raw = user_inputs.get("business_idea", "")
    business_type = user_inputs.get("business_type", "Coffee kiosk")
    cuisine = user_inputs.get("cuisine", "Ethiopian / East African")
    location = user_inputs.get("location", "Milan, Italy")
    budget = user_inputs.get("budget", "5,000-10,000 EUR")
    target_customers = user_inputs.get("target_customers", "")
    dietary_focus = user_inputs.get("dietary_focus", [])
    launch_goal = user_inputs.get("launch_goal", "")
    
    # Clean the business idea to remove greetings, normalize whitespace, etc.
    business_idea = clean_business_idea(business_idea_raw)
    
    # Extract key concepts from the Business Idea text
    # This is the PRIMARY source of truth for the plan
    idea_lower = business_idea.lower()
    idea_words = set(business_idea.lower().split())
    
    # Determine if this is the exact default Ethiopian example
    # Only return static plan if ALL fields match the default exactly
    is_exact_default = (
        "ethiopian coffee and breakfast kiosk" in idea_lower and
        "ethiopian" in cuisine.lower() and
        "milan" in location.lower() and
        business_type == "Coffee kiosk" and
        "morning commuters" in target_customers.lower()
    )
    
    # If exact default inputs, return the original sample plan
    if is_exact_default:
        return SAMPLE_LAUNCH_PLAN
    
    # Generate adapted content based on Business Idea as PRIMARY source
    # The Business Idea text should drive the narrative, with other fields as context
    cuisine_lower = cuisine.lower()
    location_city = location.split(",")[0].strip()
    
    # Build business summary that REFLECTS the Business Idea text
    # Extract key themes from the business idea
    dietary_text = _get_dietary_focus_text(dietary_focus)
    
    # Create a natural display concept from the business idea
    display_concept = create_display_concept(business_idea)
    
    # Build professional summary using the display concept
    business_summary = (
        f"A {display_concept} targeting {target_customers if target_customers else 'local customers'} "
        f"in {location}. This {business_type.lower()} focuses on delivering a curated menu "
        f"that balances quality, speed, and profitability{dietary_text}."
    )
    
    # Build positioning that reflects the BUSINESS IDEA, not just cuisine templates
    # Extract unique value proposition from the business idea
    positioning_base = f"This {business_type.lower()} in {location_city} "
    
    # Try to extract what makes this concept unique from the business idea
    if "authentic" in idea_lower or "traditional" in idea_lower:
        positioning_base += f"offers authentic {cuisine} flavors and traditional preparation methods. "
    elif "modern" in idea_lower or "innovative" in idea_lower or "fusion" in idea_lower:
        positioning_base += f"brings a modern twist to {cuisine} cuisine with innovative approaches. "
    elif "healthy" in idea_lower or "nutritious" in idea_lower or "wellness" in idea_lower:
        positioning_base += f"focuses on healthy, nutritious {cuisine} options for health-conscious customers. "
    elif "quick" in idea_lower or "fast" in idea_lower or "convenient" in idea_lower:
        positioning_base += f"provides quick, convenient {cuisine} options for busy customers. "
    elif "premium" in idea_lower or "luxury" in idea_lower or "high-end" in idea_lower:
        positioning_base += f"delivers premium {cuisine} experiences with high-quality ingredients and service. "
    elif "affordable" in idea_lower or "budget" in idea_lower or "cheap" in idea_lower:
        positioning_base += f"makes {cuisine} cuisine accessible with affordable pricing and good value. "
    else:
        # Generic but still based on the concept
        positioning_base += f"brings {cuisine} flavors to {location_city} with a focus on quality and customer satisfaction. "
    
    # Add what makes it different from competitors
    positioning = positioning_base + f"Positioned to serve {target_customers if target_customers else 'local customers'} "
    # Use a clean snippet instead of Python list syntax
    concept_snippet = extract_concept_snippet(business_idea, max_words=6)
    if concept_snippet and concept_snippet != "this concept":
        positioning += f"seeking {concept_snippet} "
    positioning += f"in the {location_city} market."
    
    # Add dietary focus to positioning if specified
    if dietary_focus:
        positioning += " " + _get_dietary_positioning_addition(dietary_focus)
    
    # Calculate dynamic readiness score based on multiple factors
    launch_readiness_score = _calculate_readiness_score(
        business_idea=business_idea,
        business_type=business_type,
        budget=budget,
        target_customers=target_customers,
        launch_goal=launch_goal,
        dietary_focus=dietary_focus,
    )
    
    # Adapt complexity based on business type
    complexity_map = {
        "Coffee kiosk": "Low",
        "Market stall": "Low",
        "Food truck": "Medium",
        "Cafe": "Medium",
        "Bakery": "Medium",
        "Restaurant": "High",
        "Catering service": "Medium",
        "Home chef": "Low",
        "Food product": "Medium",
    }
    estimated_complexity = complexity_map.get(business_type, "Medium")
    
    # Adapt customer segment
    best_customer_segment = target_customers.split(",")[0].strip() if target_customers else "Local food enthusiasts"
    
    # Build key recommendation that addresses the SPECIFIC business idea
    # Consider the business idea's unique challenges and opportunities
    concept_snippet = extract_concept_snippet(business_idea, max_words=10)
    key_recommendation = f"For your {concept_snippet}: "
    
    # Tailor recommendation based on budget AND business idea complexity
    if "under 5,000" in budget.lower():
        key_recommendation += (
            f"Start with a minimal viable product approach—focus on 3-5 signature items that align with your concept "
            f"and can be prepared efficiently with limited equipment. Test at local markets or pop-up events before "
            f"committing to a permanent location. This minimizes risk while validating demand."
        )
    elif business_type in ["Food truck", "Market stall"]:
        key_recommendation += (
            f"Launch with a mobile operation to test multiple locations and identify your best customer base. "
            f"Focus on 5-7 core menu items that reflect your unique concept and can be prepared quickly. "
            f"Track sales by location and time to optimize your schedule."
        )
    else:
        key_recommendation += (
            f"Begin with a soft launch period of 2-4 weeks to refine operations and gather customer feedback. "
            f"Start with a focused menu of 6-8 items that showcase what makes your concept unique. "
            f"Use this period to optimize pricing, portions, and service flow."
        )
    
    # Add dietary-specific recommendation if applicable
    dietary_recommendation = _get_dietary_recommendation(dietary_focus)
    if dietary_recommendation:
        key_recommendation += " " + dietary_recommendation
    
    # Generate adapted menu items based on cuisine
    menu_items = _generate_menu_items(cuisine, dietary_focus)
    
    # Generate risks that are SPECIFIC to the business idea
    main_risks = []
    
    # Risk 1: Market awareness (tailored to the specific concept)
    if "new" in idea_lower or "innovative" in idea_lower or "unique" in idea_lower:
        main_risks.append(
            f"As a new concept ({business_idea.strip()}), customer education and marketing will be critical to build awareness in {location_city}"
        )
    else:
        main_risks.append(
            f"Market awareness of this specific concept in {location_city} may require customer education and marketing investment"
        )
    
    # Risk 2: Operational challenges (specific to business type and idea)
    if business_type in ["Food truck", "Market stall", "Coffee kiosk"]:
        main_risks.append(
            f"Mobile/kiosk operations face weather dependency, location permits, and limited prep space challenges"
        )
    else:
        main_risks.append(
            f"Operational challenges during peak hours could impact service quality and customer satisfaction"
        )
    
    # Risk 3: Ingredient/supply chain (based on cuisine and concept)
    if "authentic" in idea_lower or "traditional" in idea_lower:
        main_risks.append(
            f"Sourcing authentic ingredients for {cuisine} items may increase costs or require specialized supplier relationships"
        )
    else:
        main_risks.append(
            f"Ingredient sourcing and supply chain management may affect costs and menu consistency"
        )
    
    # Risk 4: Market-specific risk
    main_risks.append(
        f"Seasonal demand fluctuations and local market conditions in {location_city} may impact revenue consistency"
    )
    
    # Add dietary-specific risks
    dietary_risks = _get_dietary_risks(dietary_focus)
    if dietary_risks:
        main_risks.extend(dietary_risks[:1])  # Add only 1 dietary risk to keep list manageable
    
    # Generate next steps that are ACTIONABLE and SPECIFIC to the business idea
    concept_snippet = extract_concept_snippet(business_idea, max_words=10)
    next_steps = [
        f"Conduct market research with 30-50 potential customers in {location_city} to validate the appeal of your concept ({concept_snippet})",
        f"Source ingredients needed for your {cuisine} menu and calculate exact cost per portion for each item",
        f"Create social media presence with 10-15 posts showcasing what makes your concept unique before launch",
        f"Develop and test operational workflows for 3-5 days to ensure you can deliver on your concept efficiently",
    ]
    
    # Generate customer personas
    customer_personas = _generate_customer_personas(target_customers, location_city, cuisine)
    
    # Generate marketing content (pass business_idea for personalization)
    marketing = _generate_marketing_content(cuisine, location_city, business_type, business_idea)
    
    # Generate launch checklist
    launch_checklist = _generate_launch_checklist(business_type, cuisine, location_city)
    
    return {
        "business_summary": business_summary,
        "positioning": positioning,
        "launch_readiness_score": launch_readiness_score,
        "estimated_complexity": estimated_complexity,
        "best_customer_segment": best_customer_segment,
        "key_recommendation": key_recommendation,
        "main_risks": main_risks,
        "next_steps": next_steps,
        "menu_items": menu_items,
        "customer_personas": customer_personas,
        "marketing": marketing,
        "launch_checklist": launch_checklist,
    }


def _get_dietary_focus_text(dietary_focus: list) -> str:
    """Generate text snippet for dietary focus in business summary."""
    if not dietary_focus:
        return ""
    
    focus_map = {
        "Vegetarian-friendly": ", with vegetarian options",
        "Vegan-friendly": ", with plant-based options",
        "Gluten-free options": ", including gluten-free choices",
        "Halal-friendly": ", following halal standards",
        "Healthy meals": ", emphasizing nutritious ingredients",
        "Affordable meals": ", at accessible price points",
        "Premium experience": ", with premium quality focus",
    }
    
    # Get first 2 dietary focuses for summary
    focuses = [focus_map.get(f, "") for f in dietary_focus[:2] if f in focus_map]
    if focuses:
        return "".join(focuses)
    return ""


def _get_dietary_positioning_addition(dietary_focus: list) -> str:
    """Generate positioning addition based on dietary focus."""
    if not dietary_focus:
        return ""
    
    # Check for specific dietary requirements
    if any("vegan" in f.lower() for f in dietary_focus):
        return "Committed to 100% plant-based ingredients, proving that vegan food can be both delicious and satisfying."
    elif any("vegetarian" in f.lower() for f in dietary_focus):
        return "Offering extensive vegetarian options that celebrate vegetables, grains, and dairy without compromising on flavor."
    elif any("gluten-free" in f.lower() for f in dietary_focus):
        return "Providing safe gluten-free options with dedicated preparation areas to prevent cross-contamination."
    elif any("halal" in f.lower() for f in dietary_focus):
        return "Ensuring all ingredients meet halal standards with certified suppliers and proper handling procedures."
    elif any("healthy" in f.lower() for f in dietary_focus):
        return "Focusing on nutritious, wholesome ingredients that support a healthy lifestyle without sacrificing taste."
    
    return ""


def _get_dietary_recommendation(dietary_focus: list) -> str:
    """Generate dietary-specific recommendation."""
    if not dietary_focus:
        return ""
    
    if any("vegan" in f.lower() for f in dietary_focus):
        return "Clearly label all menu items as vegan and train staff to answer questions about ingredients and preparation methods."
    elif any("vegetarian" in f.lower() for f in dietary_focus):
        return "Ensure vegetarian items are clearly marked and prepared separately from meat products to avoid cross-contamination."
    elif any("gluten-free" in f.lower() for f in dietary_focus):
        return "Implement strict gluten-free protocols including separate prep areas, utensils, and storage to ensure safety for celiac customers."
    elif any("halal" in f.lower() for f in dietary_focus):
        return "Establish relationships with certified halal suppliers and maintain documentation to verify compliance with halal standards."
    
    return ""


def _get_dietary_risks(dietary_focus: list) -> list[str]:
    """Generate dietary-specific risks."""
    risks = []
    
    if any("vegan" in f.lower() for f in dietary_focus):
        risks.append("Sourcing high-quality plant-based ingredients may be more expensive or require specialized suppliers")
        risks.append("Customer education may be needed to overcome misconceptions about vegan food being bland or unsatisfying")
    
    if any("vegetarian" in f.lower() for f in dietary_focus):
        risks.append("Ensuring clear separation between vegetarian and non-vegetarian prep areas requires careful kitchen workflow design")
    
    if any("gluten-free" in f.lower() for f in dietary_focus):
        risks.append("Maintaining gluten-free standards requires rigorous staff training and may increase operational complexity")
        risks.append("Cross-contamination risks require dedicated equipment and storage, increasing startup costs")
    
    if any("halal" in f.lower() for f in dietary_focus):
        risks.append("Halal certification and supplier verification may add costs and limit ingredient sourcing options")
        risks.append("Staff training on halal requirements is essential to maintain compliance and customer trust")
    
    # Limit to 2 additional risks to avoid overwhelming the list
    return risks[:2]

def _calculate_readiness_score(
    business_idea: str,
    business_type: str,
    budget: str,
    target_customers: str,
    launch_goal: str,
    dietary_focus: list,
) -> int:
    """Calculate dynamic readiness score based on multiple input factors.
    
    Score ranges:
    - 50-64: Needs validation (high risk, unclear concept)
    - 65-79: Moderate (reasonable clarity, manageable complexity)
    - 80-90: Strong (clear concept, good resources, lower complexity)
    
    Args:
        business_idea: Description of the business concept
        business_type: Type of food business
        budget: Budget range
        target_customers: Description of target audience
        launch_goal: Launch objectives
        dietary_focus: List of dietary considerations
        
    Returns:
        Readiness score between 50 and 90
    """
    score = 70  # Base score
    
    # Factor 1: Budget adequacy (±15 points)
    budget_adjustments = {
        "Under 5,000 EUR": -5,
        "5,000-10,000 EUR": 0,
        "10,000-25,000 EUR": +5,
        "25,000-50,000 EUR": +10,
        "50,000+ EUR": +15,
    }
    score += budget_adjustments.get(budget, 0)
    
    # Factor 2: Business type complexity (±10 points)
    # Lower complexity = higher readiness
    complexity_adjustments = {
        "Coffee kiosk": +8,
        "Market stall": +8,
        "Home chef": +10,
        "Food product": +5,
        "Cafe": +3,
        "Bakery": +3,
        "Food truck": 0,
        "Catering service": 0,
        "Restaurant": -8,
        "Other": 0,
    }
    score += complexity_adjustments.get(business_type, 0)
    
    # Factor 3: Business idea clarity (±8 points)
    # Longer, more detailed ideas score higher
    idea_length = len(business_idea.strip())
    if idea_length > 100:
        score += 8
    elif idea_length > 50:
        score += 5
    elif idea_length > 20:
        score += 2
    else:
        score -= 5  # Very vague idea
    
    # Factor 4: Target customer specificity (±7 points)
    customer_length = len(target_customers.strip())
    if customer_length > 80:
        score += 7
    elif customer_length > 40:
        score += 4
    elif customer_length > 15:
        score += 2
    else:
        score -= 3  # Unclear target
    
    # Factor 5: Launch goal clarity (±5 points)
    goal_length = len(launch_goal.strip())
    if goal_length > 60:
        score += 5
    elif goal_length > 30:
        score += 3
    elif goal_length > 10:
        score += 1
    else:
        score -= 2  # No clear goal
    
    # Factor 6: Dietary focus specificity (±3 points)
    # Having specific dietary focus shows market understanding
    if len(dietary_focus) >= 3:
        score += 3
    elif len(dietary_focus) >= 2:
        score += 2
    elif len(dietary_focus) == 1:
        score += 1
    
    # Factor 7: Budget-complexity mismatch penalty (±10 points)
    # High complexity with low budget is risky
    high_complexity_types = ["Restaurant", "Catering service"]
    low_budgets = ["Under 5,000 EUR", "5,000-10,000 EUR"]
    
    if business_type in high_complexity_types and budget in low_budgets:
        score -= 10  # Significant risk
    elif business_type in high_complexity_types and budget == "10,000-25,000 EUR":
        score -= 5  # Moderate risk
    
    # Ensure score stays within realistic bounds (50-90)
    score = max(50, min(90, score))
    
    return score

def _generate_menu_items(cuisine: str, dietary_focus: list) -> list[dict[str, Any]]:
    """Generate menu items based on cuisine type and dietary focus."""
    cuisine_lower = cuisine.lower()
    is_vegan = any("vegan" in d.lower() for d in dietary_focus)
    is_vegetarian = any("vegetarian" in d.lower() for d in dietary_focus)
    
    # Base menu templates by cuisine
    if "italian" in cuisine_lower:
        items = [
            {
                "name": "Margherita Pizza",
                "category": "Main",
                "description": "Classic pizza with tomato sauce, fresh mozzarella, and basil.",
                "complexity": "Medium",
                "suggested_price": "8.00-12.00 EUR",
                "pricing_note": "Price based on size and quality of ingredients.",
                "ingredients": ["Pizza dough", "Tomato sauce", "Mozzarella", "Fresh basil", "Olive oil"],
                "allergens": ["Gluten", "Dairy"],
                "preparation_note": "Prepare dough 24 hours in advance for best results.",
                "operational_tip": "Pre-portion toppings for consistent quality and speed.",
            },
            {
                "name": "Pasta Carbonara",
                "category": "Main",
                "description": "Traditional Roman pasta with eggs, pecorino cheese, and guanciale.",
                "complexity": "Medium",
                "suggested_price": "10.00-14.00 EUR",
                "pricing_note": "Premium pricing for authentic preparation.",
                "ingredients": ["Pasta", "Eggs", "Pecorino Romano", "Guanciale", "Black pepper"],
                "allergens": ["Gluten", "Eggs", "Dairy"],
                "preparation_note": "Cook pasta al dente and combine with egg mixture off heat.",
                "operational_tip": "Prep guanciale in advance but cook pasta fresh to order.",
            },
        ]
    elif "mexican" in cuisine_lower:
        items = [
            {
                "name": "Tacos al Pastor",
                "category": "Main",
                "description": "Marinated pork tacos with pineapple, cilantro, and onions.",
                "complexity": "Medium",
                "suggested_price": "3.50-5.00 EUR per taco",
                "pricing_note": "Offer 2-3 taco combos for better value perception.",
                "ingredients": ["Corn tortillas", "Pork", "Pineapple", "Cilantro", "Onion", "Spices"],
                "allergens": ["None common"],
                "preparation_note": "Marinate pork overnight for best flavor.",
                "operational_tip": "Pre-cook meat and reheat to order for speed.",
            },
            {
                "name": "Guacamole & Chips",
                "category": "Appetizer",
                "description": "Fresh avocado dip with lime, cilantro, and tortilla chips.",
                "complexity": "Low",
                "suggested_price": "5.00-7.00 EUR",
                "pricing_note": "High margin item, prepare fresh throughout service.",
                "ingredients": ["Avocados", "Lime", "Cilantro", "Onion", "Tomato", "Tortilla chips"],
                "allergens": ["None common"],
                "preparation_note": "Make in small batches to prevent browning.",
                "operational_tip": "Excellent upsell item with main dishes.",
            },
        ]
    elif "indian" in cuisine_lower:
        items = [
            {
                "name": "Butter Chicken",
                "category": "Main",
                "description": "Tender chicken in creamy tomato-based curry sauce.",
                "complexity": "Medium",
                "suggested_price": "11.00-15.00 EUR",
                "pricing_note": "Popular dish with good margins if prep is efficient.",
                "ingredients": ["Chicken", "Tomatoes", "Cream", "Butter", "Spices", "Rice or naan"],
                "allergens": ["Dairy"],
                "preparation_note": "Marinate chicken for at least 2 hours.",
                "operational_tip": "Sauce can be prepared in large batches and frozen.",
            },
            {
                "name": "Vegetable Samosas",
                "category": "Appetizer",
                "description": "Crispy pastry filled with spiced potatoes and peas.",
                "complexity": "Medium",
                "suggested_price": "2.50-4.00 EUR per piece",
                "pricing_note": "Offer 2-for-6 EUR combo for better value.",
                "ingredients": ["Pastry dough", "Potatoes", "Peas", "Spices", "Oil"],
                "allergens": ["Gluten"],
                "preparation_note": "Can be prepared ahead and fried to order.",
                "operational_tip": "Track waste—fried items lose quality after 3 hours.",
            },
        ]
    elif "vegan" in cuisine_lower or "plant" in cuisine_lower:
        items = [
            {
                "name": "Buddha Bowl",
                "category": "Main",
                "description": "Colorful bowl with quinoa, roasted vegetables, and tahini dressing.",
                "complexity": "Low",
                "suggested_price": "9.00-12.00 EUR",
                "pricing_note": "Highlight nutritional value and Instagram appeal.",
                "ingredients": ["Quinoa", "Mixed vegetables", "Chickpeas", "Tahini", "Lemon"],
                "allergens": ["Sesame (tahini)"],
                "preparation_note": "Prep components in advance, assemble to order.",
                "operational_tip": "Offer customization options for dietary preferences.",
            },
            {
                "name": "Vegan Burger",
                "category": "Main",
                "description": "Plant-based patty with fresh vegetables and special sauce.",
                "complexity": "Medium",
                "suggested_price": "10.00-13.00 EUR",
                "pricing_note": "Premium pricing for quality plant-based protein.",
                "ingredients": ["Plant-based patty", "Bun", "Lettuce", "Tomato", "Sauce"],
                "allergens": ["Gluten", "May contain soy"],
                "preparation_note": "Cook patties fresh to order for best texture.",
                "operational_tip": "Pair with fries for combo deals.",
            },
        ]
    elif "coffee" in cuisine_lower or "bakery" in cuisine_lower:
        items = [
            {
                "name": "Specialty Coffee",
                "category": "Drink",
                "description": "Expertly crafted espresso-based beverages.",
                "complexity": "Low",
                "suggested_price": "2.50-4.50 EUR",
                "pricing_note": "Price based on size and milk alternatives.",
                "ingredients": ["Coffee beans", "Milk or alternatives", "Optional syrups"],
                "allergens": ["Dairy (if using milk)"],
                "preparation_note": "Use fresh beans and calibrate grinder daily.",
                "operational_tip": "Offer loyalty cards for repeat customers.",
            },
            {
                "name": "Fresh Pastries",
                "category": "Bakery",
                "description": "Daily selection of croissants, muffins, and sweet treats.",
                "complexity": "Medium",
                "suggested_price": "2.50-5.00 EUR",
                "pricing_note": "Higher margins on specialty items.",
                "ingredients": ["Flour", "Butter", "Sugar", "Eggs", "Various fillings"],
                "allergens": ["Gluten", "Dairy", "Eggs"],
                "preparation_note": "Bake fresh daily, ideally in morning batches.",
                "operational_tip": "Display prominently to encourage impulse purchases.",
            },
        ]
    else:
        # Generic menu for other cuisines
        items = [
            {
                "name": "Signature Dish",
                "category": "Main",
                "description": f"Authentic {cuisine} specialty showcasing traditional flavors.",
                "complexity": "Medium",
                "suggested_price": "10.00-15.00 EUR",
                "pricing_note": "Price based on ingredient costs and preparation time.",
                "ingredients": ["Main protein or base", "Vegetables", "Spices", "Accompaniments"],
                "allergens": ["Varies by preparation"],
                "preparation_note": "Prepare components in advance for efficient service.",
                "operational_tip": "Feature as your hero item in marketing materials.",
            },
            {
                "name": "Appetizer Platter",
                "category": "Appetizer",
                "description": f"Selection of {cuisine} starters perfect for sharing.",
                "complexity": "Low",
                "suggested_price": "7.00-10.00 EUR",
                "pricing_note": "Good margins and encourages larger orders.",
                "ingredients": ["Various small bites", "Dips", "Garnishes"],
                "allergens": ["Varies by items"],
                "preparation_note": "Prep components ahead, assemble fresh.",
                "operational_tip": "Excellent for groups and social dining.",
            },
        ]
    
    # Add a beverage if not already included
    if not any("drink" in item["category"].lower() for item in items):
        items.append({
            "name": "House Beverage",
            "category": "Drink",
            "description": "Refreshing drink complementing your meal.",
            "complexity": "Low",
            "suggested_price": "2.50-4.00 EUR",
            "pricing_note": "High margin item, encourage as add-on.",
            "ingredients": ["Base liquid", "Flavorings", "Ice"],
            "allergens": ["None common"],
            "preparation_note": "Prepare in batches for efficiency.",
            "operational_tip": "Offer combo deals with main dishes.",
        })
    
    # Adapt menu items based on dietary focus
    items = _adapt_menu_for_dietary_focus(items, dietary_focus)
    
    return items[:6]  # Return up to 6 items


def _adapt_menu_for_dietary_focus(items: list[dict[str, Any]], dietary_focus: list) -> list[dict[str, Any]]:
    """Adapt menu items based on dietary focus requirements."""
    if not dietary_focus:
        return items
    
    is_vegan = any("vegan" in d.lower() for d in dietary_focus)
    is_vegetarian = any("vegetarian" in d.lower() for d in dietary_focus)
    is_gluten_free = any("gluten-free" in d.lower() or "gluten free" in d.lower() for d in dietary_focus)
    is_halal = any("halal" in d.lower() for d in dietary_focus)
    
    adapted_items = []
    
    for item in items:
        adapted_item = dict(item)
        
        # For vegan focus, modify non-vegan items
        if is_vegan:
            # Replace dairy and animal products
            if "Mozzarella" in adapted_item.get("ingredients", []):
                adapted_item["name"] = adapted_item["name"].replace("Margherita", "Vegan Margherita")
                adapted_item["description"] = adapted_item["description"].replace("mozzarella", "vegan mozzarella")
                adapted_item["ingredients"] = [ing.replace("Mozzarella", "Vegan mozzarella") for ing in adapted_item["ingredients"]]
                adapted_item["allergens"] = [a for a in adapted_item.get("allergens", []) if "dairy" not in a.lower()]
                adapted_item["preparation_note"] += " Use plant-based cheese alternative."
            
            if "Eggs" in adapted_item.get("ingredients", []) or "Butter" in adapted_item.get("ingredients", []):
                # Skip non-veganizable items or adapt them
                if "Carbonara" in adapted_item["name"]:
                    adapted_item["name"] = "Vegan Pasta"
                    adapted_item["description"] = "Pasta with creamy cashew sauce, vegetables, and nutritional yeast."
                    adapted_item["ingredients"] = ["Pasta", "Cashews", "Nutritional yeast", "Vegetables", "Olive oil"]
                    adapted_item["allergens"] = ["Gluten", "Tree nuts (cashews)"]
                elif "Chicken" in adapted_item["name"]:
                    adapted_item["name"] = "Chickpea Curry"
                    adapted_item["description"] = "Hearty chickpea curry in rich tomato-based sauce."
                    adapted_item["ingredients"] = ["Chickpeas", "Tomatoes", "Coconut milk", "Spices", "Rice or naan"]
                    adapted_item["allergens"] = ["Gluten (if served with naan)"]
                    adapted_item["preparation_note"] = "Use coconut milk for creamy texture."
        
        # For vegetarian focus, remove meat items
        elif is_vegetarian:
            meat_keywords = ["pork", "chicken", "beef", "fish", "meat", "guanciale"]
            if any(keyword in adapted_item["name"].lower() or
                   any(keyword in ing.lower() for ing in adapted_item.get("ingredients", []))
                   for keyword in meat_keywords):
                # Replace with vegetarian alternative
                if "Tacos" in adapted_item["name"]:
                    adapted_item["name"] = "Vegetarian Tacos"
                    adapted_item["description"] = "Seasoned black beans and vegetables with fresh toppings."
                    adapted_item["ingredients"] = ["Corn tortillas", "Black beans", "Vegetables", "Cilantro", "Onion", "Spices"]
                elif "Carbonara" in adapted_item["name"]:
                    adapted_item["name"] = "Vegetarian Pasta"
                    adapted_item["description"] = "Pasta with creamy sauce, mushrooms, and parmesan."
                    adapted_item["ingredients"] = ["Pasta", "Mushrooms", "Cream", "Parmesan", "Black pepper"]
                elif "Chicken" in adapted_item["name"]:
                    adapted_item["name"] = "Paneer Tikka Masala"
                    adapted_item["description"] = "Indian cottage cheese in creamy tomato-based curry sauce."
                    adapted_item["ingredients"] = ["Paneer", "Tomatoes", "Cream", "Butter", "Spices", "Rice or naan"]
        
        # For gluten-free focus, add notes about gluten-free options
        if is_gluten_free:
            if "Gluten" in adapted_item.get("allergens", []):
                adapted_item["name"] += " (GF option available)"
                adapted_item["preparation_note"] += " Gluten-free version available with dedicated prep area to prevent cross-contamination."
                adapted_item["allergens"].append("Prepared in facility that handles gluten")
        
        # For halal focus, add halal certification notes
        if is_halal:
            if any(meat in adapted_item["name"].lower() for meat in ["chicken", "beef", "lamb", "meat"]):
                adapted_item["preparation_note"] += " All meat sourced from halal-certified suppliers."
                adapted_item["operational_tip"] += " Maintain halal certification documentation."
        
        adapted_items.append(adapted_item)
    
    return adapted_items


def _generate_customer_personas(target_customers: str, location: str, cuisine: str) -> list[dict[str, Any]]:
    """Generate customer personas based on target audience."""
    personas = []
    
    # Parse target customers
    customer_types = target_customers.lower() if target_customers else "local customers"
    
    # Persona 1: Based on primary target
    if "student" in customer_types or "young" in customer_types:
        personas.append({
            "name": "Alex - The Budget-Conscious Student",
            "profile": f"22-year-old university student in {location}. Looking for affordable, filling meals that fit a tight budget.",
            "needs": "Value for money (under 10 EUR), filling portions, quick service, shareable on social media.",
            "recommended_offer": f"Student special combo featuring {cuisine} favorites at a discounted price.",
            "marketing_angle": "Great food doesn't have to break the bank. Authentic flavors, student-friendly prices.",
        })
    elif "professional" in customer_types or "office" in customer_types or "worker" in customer_types:
        personas.append({
            "name": "Maria - The Busy Professional",
            "profile": f"32-year-old professional working in {location}. Values quality and convenience during lunch breaks.",
            "needs": "Fast service (under 10 minutes), healthy options, consistent quality, reasonable prices for daily visits.",
            "recommended_offer": f"Express lunch menu with {cuisine} dishes ready in under 10 minutes.",
            "marketing_angle": "Elevate your lunch break with authentic flavors that fit your schedule.",
        })
    else:
        personas.append({
            "name": "Local Food Enthusiast",
            "profile": f"35-year-old resident of {location} who enjoys exploring new cuisines and supporting local businesses.",
            "needs": "Authentic flavors, quality ingredients, unique experience, good value.",
            "recommended_offer": f"Tasting menu featuring signature {cuisine} dishes.",
            "marketing_angle": f"Discover authentic {cuisine} right in your neighborhood.",
        })
    
    # Persona 2: Cultural explorer
    personas.append({
        "name": "The Cultural Explorer",
        "profile": f"28-year-old food enthusiast in {location} who actively seeks authentic international dining experiences.",
        "needs": "Authenticity, story behind the food, Instagram-worthy presentation, willing to pay premium.",
        "recommended_offer": f"Chef's special featuring traditional {cuisine} preparation methods.",
        "marketing_angle": f"Experience {cuisine} culture through food—authentic recipes, traditional techniques.",
    })
    
    # Persona 3: Family/group
    if "family" in customer_types or "group" in customer_types:
        personas.append({
            "name": "The Family Organizer",
            "profile": f"40-year-old parent in {location} looking for family-friendly dining options that please everyone.",
            "needs": "Variety on menu, kid-friendly options, good portions, reasonable prices for groups.",
            "recommended_offer": f"Family meal deal with selection of {cuisine} favorites for sharing.",
            "marketing_angle": "Bring the family together over delicious food everyone will love.",
        })
    else:
        personas.append({
            "name": "Weekend Adventurer",
            "profile": f"30-year-old local in {location} who explores new restaurants and cafes on weekends.",
            "needs": "Relaxed atmosphere, interesting menu, good for socializing, worth the visit.",
            "recommended_offer": f"Weekend brunch or dinner special featuring {cuisine} highlights.",
            "marketing_angle": "Make your weekend special with flavors worth traveling for.",
        })
    
    return personas[:3]


def _generate_marketing_content(cuisine: str, location: str, business_type: str, business_idea: str = "") -> dict[str, Any]:
    """Generate marketing content based on concept and business idea."""
    cuisine_hashtag = cuisine.replace(" / ", "").replace(" ", "")
    location_hashtag = location.split(",")[0].replace(" ", "")
    
    # Extract key selling points from business idea if provided
    idea_lower = business_idea.lower() if business_idea else ""
    
    # Get clean concept snippet for marketing
    concept_snippet = extract_concept_snippet(business_idea, max_words=8) if business_idea else ""
    
    # Create slogan that reflects the unique concept
    if "authentic" in idea_lower or "traditional" in idea_lower:
        slogan = f"Authentic {cuisine} in {location}—where tradition meets taste."
    elif "modern" in idea_lower or "innovative" in idea_lower:
        slogan = f"Modern {cuisine} in {location}—tradition reimagined."
    elif "healthy" in idea_lower or "wellness" in idea_lower:
        slogan = f"Healthy {cuisine} in {location}—nourish your body and soul."
    elif "quick" in idea_lower or "fast" in idea_lower:
        slogan = f"Quick {cuisine} in {location}—great food, no wait."
    else:
        slogan = f"{cuisine} in {location}—{concept_snippet if concept_snippet else 'where flavor meets passion'}."
    
    return {
        "slogan": slogan[:100],  # Keep it concise
        "instagram_bio": (
            f"🍽️ {concept_snippet if concept_snippet else f'{cuisine} in {location}'} | "
            f"📍 {location} | DM for reservations & catering"
        )[:150],  # Instagram bio limit
        "captions": [
            f"Bringing {concept_snippet.lower() if concept_snippet else f'{cuisine} flavors'} to {location}. Who's ready? 🍽️✨ #{cuisine_hashtag} #{location_hashtag}Food",
            f"Every dish tells a story. Come experience what makes us unique. 🌟 #{cuisine_hashtag} #FoodLovers",
            f"Fresh ingredients, passion, and flavor. This is {cuisine} in {location}. 🔥 #{location_hashtag}Eats #{cuisine_hashtag}Cuisine",
        ],
        "launch_announcement": (
            f"Launch strategy: Start with a soft opening to test operations and gather feedback on your unique concept. "
            f"Focus on 5-7 signature dishes that showcase what makes your {business_type.lower()} different. Use social media "
            f"to build anticipation with behind-the-scenes content highlighting your concept. Offer a special "
            f"promotion for the first week to drive trial and word-of-mouth. Collect customer "
            f"feedback and adjust based on real data before the grand opening."
        ),
    }


def _generate_launch_checklist(business_type: str, cuisine: str, location: str) -> dict[str, list[str]]:
    """Generate launch checklist based on business type."""
    return {
        "before_launch": [
            f"Finalize menu with 5-8 core {cuisine} items based on ingredient availability",
            f"Calculate exact food costs and set prices for {location} market",
            "Create allergen labels and nutritional information for all menu items",
            f"Test packaging and presentation for {business_type.lower()} format",
            f"Secure all necessary permits and licenses for operating in {location}",
        ],
        "menu_validation": [
            f"Conduct taste tests with 30-50 people in {location} to validate menu appeal",
            "Test 2-3 price points for each item to optimize pricing strategy",
            "Identify top 3-5 items based on feedback, cost, and preparation time",
            "Validate that prep workflow fits within your operational capacity",
        ],
        "marketing_setup": [
            "Create social media accounts with 10-15 pre-launch posts",
            f"Design menu boards and signage appropriate for {business_type.lower()}",
            f"Prepare key phrases to explain {cuisine} dishes to curious customers",
            f"Set up Google Business profile for {location} visibility",
        ],
        "operations": [
            "Develop detailed prep checklist with time estimates for each task",
            "Test complete workflow for 3-5 days to identify bottlenecks",
            "Set daily ingredient purchase limits based on realistic projections",
            "Create simple POS system to track sales by item and time",
            "Establish backup suppliers for critical ingredients",
        ],
        "first_week_testing": [
            "Track sales by item, time, and day to identify patterns",
            "Collect structured feedback from at least 50 customers",
            "Monitor prep time vs. service time for efficiency improvements",
            "Calculate actual food cost percentage and compare to projections",
            "Adjust menu, pricing, or operations based on real data",
        ],
    }
