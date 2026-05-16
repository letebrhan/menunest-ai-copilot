"""Fallback demo data for MenuNest.

This module provides realistic, validated sample launch plans that adapt to user inputs.
The data is used in demo mode to ensure reliable operation during presentations
and when API access is unavailable.
"""

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



def generate_dynamic_demo_plan(user_inputs: dict[str, Any]) -> dict[str, Any]:
    """Generate a demo launch plan that adapts to user inputs.
    
    This function creates realistic demo data based on the user's form inputs,
    making the demo mode feel responsive and personalized while maintaining
    reliability without requiring API calls.
    
    Args:
        user_inputs: Dictionary containing business concept details
        
    Returns:
        Launch plan dictionary adapted to user inputs
    """
    business_idea = user_inputs.get("business_idea", "")
    business_type = user_inputs.get("business_type", "Coffee kiosk")
    cuisine = user_inputs.get("cuisine", "Ethiopian / East African")
    location = user_inputs.get("location", "Milan, Italy")
    budget = user_inputs.get("budget", "5,000-10,000 EUR")
    target_customers = user_inputs.get("target_customers", "")
    dietary_focus = user_inputs.get("dietary_focus", [])
    launch_goal = user_inputs.get("launch_goal", "")
    
    # Determine if this is the default Ethiopian example
    is_default = (
        "ethiopian" in business_idea.lower() and
        "ethiopian" in cuisine.lower() and
        "milan" in location.lower()
    )
    
    # If default inputs, return the original sample plan
    if is_default:
        return SAMPLE_LAUNCH_PLAN
    
    # Generate adapted content based on inputs
    cuisine_lower = cuisine.lower()
    location_city = location.split(",")[0].strip()
    
    # Adapt business summary
    business_summary = (
        f"A {cuisine} {business_type.lower()} targeting {target_customers.lower() if target_customers else 'local customers'} "
        f"in {location}. The concept focuses on delivering authentic flavors with efficient operations, "
        f"offering a curated menu that balances quality, speed, and profitability."
    )
    
    # Adapt positioning based on cuisine and business type
    positioning_templates = {
        "italian": f"Authentic Italian cuisine in {location_city}, bringing traditional recipes and fresh ingredients to create a memorable dining experience.",
        "mediterranean": f"Fresh Mediterranean flavors in {location_city}, offering healthy, flavorful dishes inspired by coastal traditions.",
        "middle eastern": f"Authentic Middle Eastern cuisine in {location_city}, featuring traditional spices, fresh ingredients, and time-honored recipes.",
        "mexican": f"Vibrant Mexican flavors in {location_city}, serving authentic dishes with fresh ingredients and bold, traditional seasonings.",
        "indian": f"Traditional Indian cuisine in {location_city}, offering aromatic spices, authentic recipes, and diverse regional flavors.",
        "asian fusion": f"Creative Asian fusion in {location_city}, blending traditional techniques with modern innovation for unique flavor experiences.",
        "vegan": f"Plant-based excellence in {location_city}, proving that vegan food can be delicious, satisfying, and accessible to everyone.",
        "bakery": f"Artisan bakery in {location_city}, crafting fresh breads, pastries, and baked goods using traditional methods and quality ingredients.",
        "coffee": f"Specialty coffee experience in {location_city}, serving expertly crafted beverages with premium beans and skilled preparation.",
    }
    
    positioning = positioning_templates.get(
        next((k for k in positioning_templates if k in cuisine_lower), ""),
        f"Unique {cuisine} experience in {location_city}, offering authentic flavors and quality service to discerning customers."
    )
    
    # Adapt readiness score based on budget
    budget_scores = {
        "Under 5,000 EUR": 65,
        "5,000-10,000 EUR": 72,
        "10,000-25,000 EUR": 78,
        "25,000-50,000 EUR": 82,
        "50,000+ EUR": 85,
    }
    launch_readiness_score = budget_scores.get(budget, 70)
    
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
    
    # Adapt key recommendation based on business type and budget
    if "under 5,000" in budget.lower():
        key_recommendation = (
            f"Start with a minimal viable product approach—focus on 3-5 signature items that can be prepared "
            f"efficiently with limited equipment. Test your concept at local markets or pop-up events before "
            f"committing to a permanent location. This minimizes risk while validating demand and gathering "
            f"customer feedback to refine your offering."
        )
    elif business_type in ["Food truck", "Market stall"]:
        key_recommendation = (
            f"Launch with a mobile operation to test multiple locations and identify your best customer base. "
            f"Focus on 5-7 core menu items that travel well and can be prepared quickly. Track sales by location "
            f"and time to optimize your schedule before considering a fixed location."
        )
    else:
        key_recommendation = (
            f"Begin with a soft launch period of 2-4 weeks to refine operations and gather customer feedback. "
            f"Start with a focused menu of 6-8 items that showcase your concept while keeping prep manageable. "
            f"Use this period to optimize pricing, portions, and service flow before your official grand opening."
        )
    
    # Generate adapted menu items based on cuisine
    menu_items = _generate_menu_items(cuisine, dietary_focus)
    
    # Generate adapted risks
    main_risks = [
        f"Market awareness of {cuisine} cuisine in {location_city} may require customer education and marketing investment",
        f"Operational challenges during peak hours could impact service quality and customer satisfaction",
        f"Ingredient sourcing for authentic {cuisine} items may affect costs or require supplier relationships",
        f"Seasonal demand fluctuations typical in {location_city} may impact revenue consistency",
    ]
    
    # Generate next steps
    next_steps = [
        f"Conduct market research with 30-50 potential customers in {location_city} to validate menu appeal and pricing",
        f"Source ingredients from local suppliers and calculate exact cost per portion for each menu item",
        f"Create social media presence with 10-15 posts showcasing your {cuisine} concept before launch",
        f"Develop operational workflows and test them for 3-5 days to identify and resolve bottlenecks",
    ]
    
    # Generate customer personas
    customer_personas = _generate_customer_personas(target_customers, location_city, cuisine)
    
    # Generate marketing content
    marketing = _generate_marketing_content(cuisine, location_city, business_type)
    
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
    
    return items[:6]  # Return up to 6 items


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


def _generate_marketing_content(cuisine: str, location: str, business_type: str) -> dict[str, Any]:
    """Generate marketing content based on concept."""
    cuisine_hashtag = cuisine.replace(" / ", "").replace(" ", "")
    location_hashtag = location.split(",")[0].replace(" ", "")
    
    return {
        "slogan": f"Authentic {cuisine} in {location}—where tradition meets taste.",
        "instagram_bio": (
            f"🍽️ Authentic {cuisine} in {location} | Fresh ingredients, traditional recipes | "
            f"📍 {location} | DM for reservations & catering"
        ),
        "captions": [
            f"Bringing authentic {cuisine} flavors to {location}. Who's ready to taste tradition? 🍽️✨ #{cuisine_hashtag} #{location_hashtag}Food",
            f"Every dish tells a story. Come experience {cuisine} the way it's meant to be. 🌟 #Authentic{cuisine_hashtag} #FoodLovers",
            f"Fresh ingredients, traditional recipes, unforgettable flavors. This is {cuisine} in {location}. 🔥 #{location_hashtag}Eats #{cuisine_hashtag}Cuisine",
        ],
        "launch_announcement": (
            f"Launch strategy: Start with a soft opening to test operations and gather feedback. "
            f"Focus on 5-7 signature {cuisine} dishes that showcase your concept. Use social media "
            f"to build anticipation with behind-the-scenes content and teasers. Offer a special "
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
