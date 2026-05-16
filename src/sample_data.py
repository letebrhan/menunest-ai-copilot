"""Fallback demo data for MenuNest."""

SAMPLE_LAUNCH_PLAN = {
    "business_summary": (
        "A focused Ethiopian coffee and breakfast kiosk for Milan commuters, "
        "students, office workers, and cultural food explorers."
    ),
    "positioning": (
        "Authentic East African breakfast with simple, warm, affordable menu "
        "items designed for busy Milan mornings."
    ),
    "launch_readiness_score": 78,
    "estimated_complexity": "Medium",
    "best_customer_segment": "Morning commuters",
    "key_recommendation": (
        "Start with 5 to 6 core menu items and test demand near offices, "
        "universities, and metro areas before investing in a fixed location."
    ),
    "main_risks": [
        "Ingredient cost uncertainty",
        "Limited customer awareness of Ethiopian breakfast",
        "Need for clear allergen communication",
        "Morning rush operational pressure",
    ],
    "next_steps": [
        "Validate the top 5 menu items with at least 20 potential customers.",
        "Calculate ingredient cost per item before final pricing.",
        "Prepare simple product photos for Instagram and local flyers.",
        "Test one coffee and snack combo during the first week.",
    ],
    "menu_items": [
        {
            "name": "Ethiopian Coffee",
            "category": "Drink",
            "description": "Traditional hot coffee served fresh for morning customers.",
            "complexity": "Low",
            "suggested_price": "2.00-2.80 EUR",
            "pricing_note": "Keep affordable for daily commuters.",
            "ingredients": ["Coffee beans", "Water", "Optional spices"],
            "allergens": ["None common"],
            "preparation_note": "Prepare fresh batches during the morning rush.",
            "operational_tip": "Use a consistent cup size and offer a simple takeaway option.",
        },
        {
            "name": "Spiced Tea",
            "category": "Drink",
            "description": "Warm tea with East African spice notes.",
            "complexity": "Low",
            "suggested_price": "2.00-3.00 EUR",
            "pricing_note": "Good alternative for non-coffee customers.",
            "ingredients": ["Black tea", "Water", "Milk optional", "Spices"],
            "allergens": ["Milk if added"],
            "preparation_note": "Prepare spice mix in advance for speed.",
            "operational_tip": "Offer dairy-free service by default unless milk is requested.",
        },
        {
            "name": "Sambusa",
            "category": "Snack",
            "description": "Crispy lentil-filled pastry served warm.",
            "complexity": "Medium",
            "suggested_price": "2.50-3.50 EUR",
            "pricing_note": "Strong item for combo pricing.",
            "ingredients": ["Flour", "Lentils", "Onion", "Garlic", "Spices", "Oil"],
            "allergens": ["Gluten"],
            "preparation_note": "Prepare filling in batches and serve warm.",
            "operational_tip": "Track waste carefully because fried items lose quality over time.",
        },
        {
            "name": "Ful Breakfast Bowl",
            "category": "Breakfast",
            "description": "Warm fava bean bowl with herbs, spices, and bread on the side.",
            "complexity": "Medium",
            "suggested_price": "5.50-7.50 EUR",
            "pricing_note": "Good filling breakfast option for students and workers.",
            "ingredients": ["Fava beans", "Tomato", "Onion", "Olive oil", "Bread", "Spices"],
            "allergens": ["Gluten if served with bread"],
            "preparation_note": "Cook beans in advance and finish portions quickly during service.",
            "operational_tip": "Offer small and regular sizes to control portion cost.",
        },
        {
            "name": "Injera Breakfast Wrap",
            "category": "Breakfast",
            "description": "Soft injera-style wrap with lentils or vegetables.",
            "complexity": "Medium",
            "suggested_price": "5.00-7.00 EUR",
            "pricing_note": "Use as a signature cultural item after testing demand.",
            "ingredients": ["Injera", "Lentils", "Vegetables", "Spices"],
            "allergens": ["Check flour source for gluten risk"],
            "preparation_note": "Standardize filling quantity to keep margins stable.",
            "operational_tip": "Start with one filling option before adding more variants.",
        },
        {
            "name": "Lentil Bowl",
            "category": "Lunch-light",
            "description": "Simple lentil bowl for vegetarian-friendly customers.",
            "complexity": "Medium",
            "suggested_price": "6.00-8.00 EUR",
            "pricing_note": "Good for customers who want an affordable healthy meal.",
            "ingredients": ["Lentils", "Rice or bread", "Vegetables", "Spices"],
            "allergens": ["Gluten if served with bread"],
            "preparation_note": "Prepare lentils in batches and reheat safely.",
            "operational_tip": "Use this as a lunch extension only if breakfast demand is stable.",
        },
    ],
    "customer_personas": [
        {
            "name": "Morning Commuter",
            "profile": "Office worker or metro commuter looking for a fast breakfast.",
            "needs": "Quick service, warm drink, affordable snack.",
            "recommended_offer": "Coffee plus sambusa combo.",
            "marketing_angle": "Fast cultural breakfast for busy Milan mornings.",
        },
        {
            "name": "Student Budget Buyer",
            "profile": "Student looking for something filling and affordable.",
            "needs": "Low price, filling portions, clear menu.",
            "recommended_offer": "Ful bowl or lentil bowl student combo.",
            "marketing_angle": "Warm breakfast with good value.",
        },
        {
            "name": "Cultural Food Explorer",
            "profile": "Customer interested in authentic international food experiences.",
            "needs": "Story, authenticity, visual menu, friendly explanation.",
            "recommended_offer": "Coffee tasting plus sambusa.",
            "marketing_angle": "Discover East African breakfast in Milan.",
        },
    ],
    "marketing": {
        "slogan": "Authentic East African breakfast for Milan mornings.",
        "instagram_bio": (
            "Ethiopian coffee, warm breakfast, and cultural flavors in Milan. "
            "Simple, affordable, and made for your morning routine."
        ),
        "captions": [
            "Start your morning with bold Ethiopian coffee and fresh sambusa.",
            "A new breakfast experience is coming to Milan.",
            "Simple, warm, authentic flavors for your daily routine.",
        ],
        "launch_announcement": (
            "MenuNest recommends launching with a small test menu, simple combo "
            "pricing, and a first-week feedback campaign near offices, universities, "
            "and metro areas."
        ),
    },
    "launch_checklist": {
        "before_launch": [
            "Choose 5 core menu items",
            "Calculate ingredient cost per item",
            "Prepare allergen notes",
            "Test packaging",
        ],
        "menu_validation": [
            "Ask 20 people for feedback",
            "Test 2 price points",
            "Identify top 3 best items",
        ],
        "marketing_setup": [
            "Create Instagram page",
            "Create Google Business profile if location is confirmed",
            "Prepare launch photos",
        ],
        "operations": [
            "Create a prep checklist",
            "Define morning rush workflow",
            "Set daily ingredient purchase limits",
        ],
        "first_week_testing": [
            "Track best-selling items",
            "Collect customer feedback",
            "Remove low-demand items",
            "Adjust prices if needed",
        ],
    },
}
