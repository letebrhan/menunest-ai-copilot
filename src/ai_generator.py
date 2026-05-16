"""AI generation layer for MenuNest.

The MVP runs in demo mode by default to ensure reliability during presentations.
Real LLM providers can be integrated by implementing provider-specific logic
in the generate_launch_plan function.

Security: API keys are loaded from environment variables and never exposed in
generated output or logs.
"""

from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv

from src.prompt_builder import build_launch_plan_prompt
from src.sample_data import SAMPLE_LAUNCH_PLAN, generate_dynamic_demo_plan
from src.validators import coerce_launch_plan, safe_parse_json

# Load environment variables from .env file
# API keys should NEVER be hardcoded or committed to version control
load_dotenv()


def generate_launch_plan(
    user_inputs: dict[str, Any],
    use_demo: bool = True,
) -> dict[str, Any]:
    """Generate a launch plan for a food business concept.
    
    This function supports multiple modes:
    1. Demo mode (default): Returns validated sample data with optional localization
    2. Live AI mode: Calls external LLM provider (requires API credentials)
    
    Args:
        user_inputs: Dictionary containing business concept details
        use_demo: If True, use stable demo data instead of calling external APIs
        
    Returns:
        Validated launch plan dictionary with all required sections
        
    Security:
        - API keys are read from environment variables only
        - No API keys are included in generated output
        - All responses are validated before returning
    """
    # Determine which provider to use
    provider = os.getenv("LLM_PROVIDER", "demo").lower().strip()
    output_language = user_inputs.get("output_language", "English")

    # Demo mode: Generate dynamic demo data based on user inputs
    if use_demo or provider == "demo":
        # Generate plan adapted to user inputs
        plan = generate_dynamic_demo_plan(user_inputs)
        plan = coerce_launch_plan(plan)
        
        # Apply language localization if requested
        if output_language == "Italian":
            plan = localize_demo_plan_to_italian(plan)
        elif output_language == "English":
            # English is the default, no transformation needed
            pass
        
        return plan

    # Live AI mode: Build prompt and call external provider
    # Note: This is a placeholder for future LLM integration
    prompt = build_launch_plan_prompt(user_inputs)
    
    # TODO: Implement actual LLM provider calls here
    # Example structure:
    # if provider == "openai":
    #     response = call_openai_api(prompt)
    # elif provider == "anthropic":
    #     response = call_anthropic_api(prompt)
    # elif provider == "watsonx":
    #     response = call_watsonx_api(prompt)
    
    # For now, fall back to demo data even in "live" mode
    # This ensures the app never fails during demos
    plan = coerce_launch_plan(SAMPLE_LAUNCH_PLAN)
    
    if output_language == "Italian":
        plan = localize_demo_plan_to_italian(plan)
    
    return plan


def localize_demo_plan_to_italian(plan: dict[str, Any]) -> dict[str, Any]:
    """Return an Italian version of the demo launch plan.

    This function provides comprehensive Italian localization while maintaining
    the same data structure for validation, rendering, and export compatibility.
    
    Args:
        plan: English version of the launch plan
        
    Returns:
        Italian-localized version of the launch plan
    """
    localized = dict(plan)

    # Overview section
    localized["business_summary"] = (
        "Un chiosco di caffè e colazione etiope rivolto ai pendolari milanesi, "
        "studenti universitari e lavoratori d'ufficio che cercano opzioni di colazione "
        "autentiche, convenienti e culturalmente ricche. Il concept si concentra su 5-6 "
        "prodotti distintivi che possono essere preparati efficientemente durante la "
        "fascia mattutina, introducendo i clienti ai sapori tradizionali dell'Africa orientale."
    )
    localized["positioning"] = (
        "L'unica esperienza autentica di colazione etiope nei distretti business di Milano, "
        "che offre la qualità della cerimonia del caffè tradizionale in formato fast-casual. "
        "Posizionato tra le catene di caffè generiche (prive di autenticità) e i ristoranti "
        "con servizio al tavolo (troppo lenti per i pendolari), colmando un vuoto per gli "
        "esploratori di cibo culturale e i professionisti attenti al tempo che cercano "
        "qualcosa oltre il solito cornetto e cappuccino."
    )
    localized["estimated_complexity"] = "Medium"
    localized["best_customer_segment"] = "Pendolari mattutini 25-45 anni"
    localized["key_recommendation"] = (
        "Lancia con un carretto mobile o chiosco temporaneo vicino a Porta Garibaldi o "
        "Stazione Centrale per 4-6 settimane per validare la domanda e perfezionare le "
        "operazioni prima di impegnarsi in un contratto di locazione fissa. Concentrati "
        "sul perfezionare 3 prodotti principali (caffè, sambusa e una ciotola per colazione) "
        "prima di espandere il menu. Questo approccio minimizza il rischio costruendo una "
        "base clienti e raccogliendo dati reali sui prezzi."
    )
    localized["main_risks"] = [
        "Limitata consapevolezza del marchio sulla cultura della colazione etiope a Milano potrebbe richiedere significativa educazione del cliente",
        "Pressione operativa durante la fascia mattutina con preparazioni complesse potrebbe portare a inconsistenza qualitativa o lunghi tempi di attesa",
        "Sfide nell'approvvigionamento di ingredienti per spezie autentiche e farina di teff potrebbero aumentare i costi o richiedere sostituzioni",
        "Fluttuazioni stagionali della domanda durante le vacanze estive e le chiusure di agosto tipiche di Milano",
    ]
    localized["next_steps"] = [
        "Conduci test di assaggio con 30-50 potenziali clienti vicino alle location target per validare l'appeal del menu e raccogliere feedback sui prezzi",
        "Procura ingredienti da negozi specializzati africani a Milano (zona Via Padova) e calcola il costo esatto per porzione di ogni voce del menu",
        "Crea una presenza Instagram semplice con 10-15 post che mostrano la preparazione del cibo, il contesto culturale e testimonianze dei clienti prima del lancio",
        "Sviluppa una checklist di preparazione mattutina di 2 ore e testala per 3 giorni per identificare colli di bottiglia e ottimizzare il flusso di lavoro",
    ]

    # Menu items localization
    # NOTE: Keep complexity values in English ("Low", "Medium", "High") for validation
    # Only translate user-facing text fields
    localized["menu_items"] = [
        {
            "name": "Caffè Etiope (Buna)",
            "category": "Bevanda",
            "description": "Caffè ricco e aromatico preparato con metodi tradizionali etiopi con cardamomo opzionale.",
            "complexity": "Low",
            "suggested_price": "2.50-3.50 EUR",
            "pricing_note": "Prezzo competitivo con caffetterie specializzate (fascia 2.80-3.20 EUR) enfatizzando autenticità ed esperienza culturale.",
            "ingredients": ["Chicchi di caffè etiope", "Acqua", "Cardamomo (opzionale)", "Zucchero (opzionale)"],
            "allergens": ["Nessuno comune"],
            "preparation_note": "Tosta i chicchi freschi ogni giorno se possibile, o procura pre-tostati da negozi specializzati africani. Prepara in jebena tradizionale o usa French press per velocità.",
            "operational_tip": "Prepara in lotti di 8-10 porzioni durante la fascia mattutina (7-9). Offri tazzine di assaggio ai clienti curiosi per costruire interesse.",
        },
        {
            "name": "Tè Speziato (Shai)",
            "category": "Bevanda",
            "description": "Tè nero riscaldante infuso con cannella, zenzero e chiodi di garofano, servito con o senza latte.",
            "complexity": "Low",
            "suggested_price": "2.50-3.00 EUR",
            "pricing_note": "Posiziona come alternativa premium al tè standard, evidenziando la miscela di spezie come punto di vendita unico.",
            "ingredients": ["Tè nero", "Acqua", "Cannella", "Zenzero", "Chiodi di garofano", "Latte (opzionale)", "Zucchero (opzionale)"],
            "allergens": ["Latte (se aggiunto)"],
            "preparation_note": "Pre-miscela le spezie secche in grandi quantità per risparmiare tempo. Lascia in infusione per 3-4 minuti per sapore ottimale senza amarezza.",
            "operational_tip": "Default senza latticini a meno che non sia richiesto. Tieni latte d'avena come alternativa per clienti intolleranti al lattosio.",
        },
        {
            "name": "Sambusa (Lenticchie)",
            "category": "Snack",
            "description": "Pasta triangolare croccante ripiena di lenticchie speziate, cipolle e jalapeño, servita calda.",
            "complexity": "Medium",
            "suggested_price": "2.80-3.50 EUR",
            "pricing_note": "Prezzo per pezzo o offri combo 2-per-5 EUR. Prodotto con buon margine se la preparazione è efficiente.",
            "ingredients": ["Farina di grano", "Lenticchie", "Cipolla", "Jalapeño", "Aglio", "Cumino", "Curcuma", "Olio vegetale"],
            "allergens": ["Glutine", "Può contenere tracce di sesamo"],
            "preparation_note": "Prepara il ripieno la sera prima. Assembla e friggi fresco ogni mattina. Può essere mantenuto caldo per massimo 2-3 ore.",
            "operational_tip": "Monitora attentamente gli sprechi—i fritti perdono qualità dopo 3 ore. Inizia con 20-30 pezzi e aggiusta in base ai pattern di domanda.",
        },
        {
            "name": "Ciotola Ful Medames",
            "category": "Colazione",
            "description": "Sostanzioso stufato di fave con pomodori, cipolle e olio d'oliva, servito con pane fresco per intingere.",
            "complexity": "Medium",
            "suggested_price": "6.50-8.00 EUR",
            "pricing_note": "Posiziona come alternativa di colazione sostanziosa e ricca di proteine ai dolci. Target studenti e lavoratori attenti al budget.",
            "ingredients": ["Fave", "Pomodori", "Cipolla", "Aglio", "Olio d'oliva", "Succo di limone", "Cumino", "Pane fresco"],
            "allergens": ["Glutine (pane)", "Può contenere tracce di sesamo"],
            "preparation_note": "Cuoci le fave in grandi lotti (possono essere refrigerate per 3 giorni). Riscalda porzioni individuali e finisci con condimenti freschi.",
            "operational_tip": "Offri dimensioni piccola (5 EUR) e regolare (7 EUR). La dimensione piccola ha margini migliori e riduce gli sprechi per domanda incerta.",
        },
        {
            "name": "Colazione Firfir",
            "category": "Colazione",
            "description": "Pezzi di injera strappati mescolati con salsa berbere speziata e uova strapazzate, un piatto mattutino tradizionale.",
            "complexity": "Medium",
            "suggested_price": "7.00-8.50 EUR",
            "pricing_note": "Prodotto colazione premium. Richiede educazione del cliente ma ha alto valore percepito per esploratori di cibo culturale.",
            "ingredients": ["Injera", "Uova", "Spezia berbere", "Cipolla", "Pomodoro", "Olio d'oliva", "Erbe fresche"],
            "allergens": ["Uova", "Glutine (injera)", "Piccante (berbere)"],
            "preparation_note": "Pre-strappa l'injera e conserva in contenitore ermetico. Cuoci le uova fresche su ordinazione (2-3 minuti per porzione).",
            "operational_tip": "Inizia a offrire questo dopo la settimana 2 una volta che caffè e sambusa funzionano bene. Richiede più spiegazione ai clienti.",
        },
        {
            "name": "Ciotola Shiro Wat",
            "category": "Colazione",
            "description": "Cremoso stufato di farina di ceci con spezie etiopi, servito con injera o pane.",
            "complexity": "Medium",
            "suggested_price": "6.00-7.50 EUR",
            "pricing_note": "Eccellente opzione vegetariana/vegana con buoni margini. La farina di ceci è conveniente e stabile a scaffale.",
            "ingredients": ["Farina di ceci", "Cipolla", "Aglio", "Spezia berbere", "Pomodoro", "Olio vegetale", "Injera o pane"],
            "allergens": ["Glutine (se servito con injera/pane)", "Piccante (berbere)"],
            "preparation_note": "Può essere preparato in grandi lotti e riscaldato. La consistenza dovrebbe essere densa ma versabile.",
            "operational_tip": "Evidenzia come vegano e ricco di proteine. Popolare con clienti attenti alla salute e vegetariani.",
        },
    ]

    # Customer personas localization
    localized["customer_personas"] = [
        {
            "name": "Marco - Il Pendolare Quotidiano",
            "profile": "Manager marketing 35enne che prende la metro da Porta Garibaldi al suo ufficio vicino al Duomo. Arriva alla stazione verso le 7:45, ha bisogno di colazione prima delle 8:15. Valorizza convenienza e coerenza.",
            "needs": "Servizio veloce (sotto 3 minuti), packaging portatile, abbastanza familiare da fidarsi ma abbastanza interessante da provare, prezzo ragionevole per acquisto quotidiano (sotto 6 EUR).",
            "recommended_offer": "Combo Caffè + Sambusa per 5.50 EUR. Veloce, portatile e diventa un rituale quotidiano.",
            "marketing_angle": "Salta il solito cornetto—prova qualcosa di audace e autentico che si adatta alla tua routine mattutina. Stessa velocità, storia migliore.",
        },
        {
            "name": "Sofia - La Studentessa Universitaria",
            "profile": "Studentessa di economia 22enne alla Bocconi. Attenta al budget ma interessata a cibo sano e sostanzioso. Spesso salta la colazione per costo o mancanza di opzioni appetibili vicino al campus.",
            "needs": "Conveniente (sotto 7 EUR), abbastanza sostanzioso da durare fino a pranzo, vegetariano-friendly, degno di Instagram per condivisione social.",
            "recommended_offer": "Ciotola Ful Medames (dimensione piccola) per 6.50 EUR o Ciotola Shiro Wat per 6.00 EUR. Entrambe sostanziose, convenienti e fotogeniche.",
            "marketing_angle": "Vera colazione che ti mantiene sazio durante le lezioni mattutine. Vegana, ricca di proteine e sotto 7 EUR. Il tuo portafoglio e il tuo corpo ti ringrazieranno.",
        },
        {
            "name": "Alessandro & Chiara - Gli Esploratori Culturali",
            "profile": "Coppia 28 e 30 anni che cerca attivamente esperienze culinarie internazionali autentiche. Seguono food blogger, provano nuovi ristoranti mensilmente e condividono scoperte sui social. Disposti a pagare premium per autenticità.",
            "needs": "Storia autentica e contesto culturale, sapori unici che non possono trovare altrove, opportunità fotografiche, staff amichevole che può spiegare il cibo.",
            "recommended_offer": "Esperienza cerimonia del caffè + colazione Firfir per 10-12 EUR. Posizionamento premium con educazione culturale.",
            "marketing_angle": "Vivi la cultura della colazione etiope senza volare ad Addis Abeba. Ricette tradizionali, ingredienti autentici e una storia che vale la pena condividere.",
        },
    ]

    # Marketing content localization
    localized["marketing"] = {
        "slogan": "Mattine etiopi, stile Milano—colazione autentica per la tua routine quotidiana.",
        "instagram_bio": (
            "🇪🇹 Colazione etiope autentica a Milano | Caffè tradizionale, sambusa calda e sapori culturali | "
            "📍 Porta Garibaldi (prossimamente) | DM per catering"
        ),
        "captions": [
            "Quel momento in cui realizzi che a Milano mancava la vera colazione etiope. Stiamo rimediando. 🇪🇹☕ #CaffèEtiope #MilanoFood #ColazioneGoals",
            "Dimentica il solito cornetto. Prova la sambusa—croccante, speziata e pronta a cambiare la tua routine mattutina. Disponibile presto vicino a Porta Garibaldi. 🥟✨",
            "Il caffè etiope non è solo una bevanda, è una cerimonia. Portiamo quella tradizione alle tue mattine milanesi. Chi è pronto? ☕🇪🇹 #CulturaCaffè #ColazioneMilano",
        ],
        "launch_announcement": (
            "Strategia di lancio: Inizia con un test di 4 settimane con carretto mobile vicino alla stazione di Porta Garibaldi "
            "(alto traffico pedonale, pendolari mattutini). Concentrati su 3 prodotti principali: caffè, sambusa e una ciotola per colazione. "
            "Offri uno 'Speciale Prima Settimana' combo (caffè + sambusa per 5 EUR) per incentivare la prova. Raccogli feedback "
            "dei clienti quotidianamente e aggiusta menu/prezzi basandoti su dati reali prima di impegnarti in una location permanente. "
            "Usa le storie Instagram per costruire anticipazione e annunciare location/orari giornalieri."
        ),
    }

    # Launch checklist localization
    localized["launch_checklist"] = {
        "before_launch": [
            "Finalizza 3-5 voci del menu principali basandoti su disponibilità ingredienti e complessità di preparazione",
            "Calcola il costo esatto degli ingredienti per voce usando prezzi da negozi specializzati africani nella zona Via Padova",
            "Crea etichette allergeni chiare in italiano e inglese per tutte le voci del menu",
            "Testa soluzioni di packaging per portabilità e ritenzione del calore (critico per pendolari mattutini)",
            "Assicura i permessi necessari per operazione carretto mobile nell'area target",
        ],
        "menu_validation": [
            "Conduci test di assaggio con 30-50 persone vicino alla location target (mix di pendolari, studenti ed entusiasti del cibo)",
            "Testa 2-3 punti di prezzo per ogni voce per trovare equilibrio ottimale tra convenienza e margine",
            "Identifica le 3 voci principali basandoti su feedback gusto, velocità di preparazione e costo ingredienti",
            "Valida che il tempo di preparazione per tutte le voci rientri nella finestra di setup mattutino di 2 ore",
        ],
        "marketing_setup": [
            "Crea account Instagram con 10-15 post pre-lancio che mostrano preparazione cibo, contesto culturale e dietro le quinte",
            "Progetta menu board semplice con foto, prezzi e simboli allergeni (comunicazione visiva è chiave per clienti internazionali)",
            "Prepara 3-5 frasi chiave in italiano per spiegare le voci del menu ai clienti curiosi",
            "Crea profilo Google Business una volta confermata la location (critico per visibilità ricerca locale)",
        ],
        "operations": [
            "Sviluppa checklist dettagliata di preparazione mattutina di 2 ore con stime temporali per ogni compito",
            "Testa il flusso di lavoro completo per 3 giorni consecutivi per identificare colli di bottiglia e ottimizzare la sequenza",
            "Imposta limiti di acquisto ingredienti giornalieri basati su proiezioni di vendita realistiche (inizia conservativo per minimizzare sprechi)",
            "Crea sistema punto vendita semplice (anche solo calcolatrice telefono e quaderno) per tracciare vendite per voce",
            "Stabilisci piano di backup per guasto attrezzatura (sapere dove ottenere forniture di emergenza)",
        ],
        "first_week_testing": [
            "Traccia vendite per voce, ora e giorno per identificare pattern di domanda e orari di punta",
            "Raccogli feedback strutturato da almeno 50 clienti (cosa è piaciuto, cosa ha confuso, percezione prezzo)",
            "Monitora tempo preparazione vs. tempo servizio per identificare inefficienze operative",
            "Calcola percentuale costo cibo effettivo per ogni voce e confronta con proiezioni",
            "Aggiusta menu, prezzi o operazioni basandoti su dati reali prima della settimana 2",
        ],
    }

    return localized