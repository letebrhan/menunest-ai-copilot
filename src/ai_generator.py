"""AI generation layer.

The MVP runs in demo mode by default so it remains reliable during the hackathon
demo. Real LLM providers can be added later by implementing another provider
branch in generate_launch_plan.
"""

from __future__ import annotations

import json
import os
from typing import Any

from dotenv import load_dotenv

from src.prompt_builder import build_launch_plan_prompt
from src.sample_data import SAMPLE_LAUNCH_PLAN
from src.validators import coerce_launch_plan

load_dotenv()


def generate_launch_plan(
    user_inputs: dict[str, Any],
    use_demo: bool = True,
) -> dict[str, Any]:
    """Generate a launch plan.

    In demo mode, return a stable sample response. This prevents demo failure
    when API credentials or network access are unavailable.
    """
    provider = os.getenv("LLM_PROVIDER", "demo").lower().strip()
    output_language = user_inputs.get("output_language", "English")

    if use_demo or provider == "demo":
        plan = coerce_launch_plan(SAMPLE_LAUNCH_PLAN)

        if output_language == "Italian":
            plan = localize_demo_plan_to_italian(plan)

        return plan

    _prompt = build_launch_plan_prompt(user_inputs)

    return coerce_launch_plan(SAMPLE_LAUNCH_PLAN)

def parse_json_response(raw_text: str) -> dict[str, Any]:
    """Parse a JSON string returned by an LLM."""
    parsed = json.loads(raw_text)
    if not isinstance(parsed, dict):
        raise ValueError("Expected a JSON object from the model.")
    return parsed


def localize_demo_plan_to_italian(plan: dict[str, Any]) -> dict[str, Any]:
    """Return an Italian version of the stable demo plan.

    This is a lightweight demo localization layer. It keeps the same structure
    so validation, rendering, and export still work.
    """
    localized = dict(plan)

    localized["business_summary"] = (
        "Un chiosco specializzato in caffe etiope e colazione per pendolari, "
        "studenti, lavoratori e persone interessate a sapori culturali a Milano."
    )
    localized["positioning"] = (
        "Una colazione autentica dell'Africa orientale con prodotti semplici, "
        "caldi e accessibili per le mattine milanesi."
    )
    localized["estimated_complexity"] = "Media"
    localized["best_customer_segment"] = "Pendolari del mattino"
    localized["key_recommendation"] = (
        "Inizia con 5 o 6 prodotti principali e testa la domanda vicino a uffici, "
        "universita e fermate della metro prima di investire in una sede fissa."
    )
    localized["main_risks"] = [
        "Incertezza sui costi degli ingredienti",
        "Bassa conoscenza della colazione etiope da parte dei clienti",
        "Necessita di comunicare chiaramente gli allergeni",
        "Pressione operativa durante la fascia mattutina",
    ]
    localized["next_steps"] = [
        "Valida i 5 prodotti principali con almeno 20 potenziali clienti.",
        "Calcola il costo ingredienti per ogni prodotto prima di fissare i prezzi.",
        "Prepara foto semplici per Instagram e volantini locali.",
        "Testa una combinazione caffe e snack durante la prima settimana.",
    ]

    localized["marketing"] = {
        "slogan": "Autentica colazione dell'Africa orientale per le mattine milanesi.",
        "instagram_bio": (
            "Caffe etiope, colazione calda e sapori culturali a Milano. "
            "Semplice, accessibile e pensato per la tua routine del mattino."
        ),
        "captions": [
            "Inizia la mattina con caffe etiope intenso e sambusa calda.",
            "Una nuova esperienza di colazione sta arrivando a Milano.",
            "Sapori semplici, caldi e autentici per la tua routine quotidiana.",
        ],
        "launch_announcement": (
            "MenuNest consiglia di partire con un menu piccolo, prezzi combo "
            "semplici e una raccolta feedback nella prima settimana vicino a "
            "uffici, universita e metro."
        ),
    }

    localized["launch_checklist"] = {
        "before_launch": [
            "Scegli 5 prodotti principali",
            "Calcola il costo ingredienti per prodotto",
            "Prepara note sugli allergeni",
            "Testa il packaging",
        ],
        "menu_validation": [
            "Chiedi feedback a 20 persone",
            "Testa 2 livelli di prezzo",
            "Identifica i 3 prodotti migliori",
        ],
        "marketing_setup": [
            "Crea una pagina Instagram",
            "Crea un profilo Google Business se la posizione e confermata",
            "Prepara foto per il lancio",
        ],
        "operations": [
            "Crea una checklist di preparazione",
            "Definisci il flusso di lavoro per la mattina",
            "Imposta limiti giornalieri di acquisto ingredienti",
        ],
        "first_week_testing": [
            "Monitora i prodotti piu venduti",
            "Raccogli feedback dai clienti",
            "Rimuovi i prodotti con bassa domanda",
            "Modifica i prezzi se necessario",
        ],
    }

    return localized