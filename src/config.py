"""Central configuration for MenuNest."""

APP_TITLE = "MenuNest"
APP_SUBTITLE = "AI Copilot for Food Entrepreneurs"

BUSINESS_TYPES = [
    "Cafe",
    "Coffee kiosk",
    "Restaurant",
    "Catering service",
    "Food truck",
    "Home chef",
    "Bakery",
    "Food product",
    "Market stall",
    "Other",
]

BUDGET_RANGES = [
    "Under 5,000 EUR",
    "5,000-10,000 EUR",
    "10,000-25,000 EUR",
    "25,000-50,000 EUR",
    "50,000+ EUR",
]

DIETARY_OPTIONS = [
    "Vegetarian-friendly",
    "Vegan-friendly",
    "Gluten-free options",
    "Halal-friendly",
    "Healthy meals",
    "Affordable meals",
    "Premium experience",
    "No specific focus",
]

OUTPUT_LANGUAGES = ["English", "Italian"]

DEFAULT_INPUTS = {
    "business_idea": "I want to launch an Ethiopian coffee and breakfast kiosk in Milan.",
    "business_type": "Coffee kiosk",
    "cuisine": "Ethiopian / East African",
    "location": "Milan, Italy",
    "budget": "5,000-10,000 EUR",
    "target_customers": (
        "Office workers, students, commuters, and people interested in cultural food"
    ),
    "dietary_focus": ["Vegetarian-friendly", "Affordable meals"],
    "launch_goal": (
        "Start with a simple breakfast menu, test customer interest, "
        "and keep operations easy for the first month."
    ),
    "output_language": "English",
}
