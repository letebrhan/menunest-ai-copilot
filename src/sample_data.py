"""Fallback demo data for MenuNest.

This module provides a realistic, validated sample launch plan for an Ethiopian
coffee and breakfast kiosk in Milan. The data is used in demo mode to ensure
reliable operation during presentations and when API access is unavailable.
"""

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
