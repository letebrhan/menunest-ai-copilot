"""Custom CSS styles for MenuNest UI improvements."""

def get_custom_css() -> str:
    """Return custom CSS for responsive design, visual polish, and animations."""
    return """
    <style>
    /* ============================================
       GLOBAL STYLES & ANIMATIONS
       ============================================ */
    
    /* Smooth fade-in animation for app launch */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Slide-in animation for tabs */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-10px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Pulse animation for metrics */
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.02);
        }
    }
    
    /* Fade-up animation for hero badges */
    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Overall page background - warm cream color */
    .stApp {
        background: linear-gradient(135deg, #faf8f3 0%, #f5f1e8 100%);
    }
    
    /* Main content area with fade-in animation - reduced padding */
    .main .block-container {
        animation: fadeIn 0.6s ease-out;
        background-color: transparent;
        padding: 1.5rem 1rem 2rem 1rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Reduce spacing after title */
    .main h1 {
        margin-bottom: 1rem !important;
    }
    
    /* ============================================
       RESPONSIVE TYPOGRAPHY
       ============================================ */
    
    /* Main title - responsive sizing */
    h1 {
        font-size: clamp(1.8rem, 4vw, 2.5rem) !important;
        line-height: 1.2 !important;
        margin-bottom: 1rem !important;
    }
    
    /* Section headers */
    h2 {
        font-size: clamp(1.4rem, 3vw, 1.8rem) !important;
        line-height: 1.3 !important;
        margin-top: 1.5rem !important;
    }
    
    /* Subsection headers */
    h3 {
        font-size: clamp(1.2rem, 2.5vw, 1.5rem) !important;
        line-height: 1.4 !important;
    }
    
    /* Body text */
    p, li, .stMarkdown {
        font-size: clamp(0.9rem, 1.5vw, 1rem) !important;
        line-height: 1.6 !important;
    }
    
    /* ============================================
       HERO SECTION STYLING - PRODUCT DEMO LAYOUT
       ============================================ */
    
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.2);
        animation: fadeIn 0.8s ease-out;
    }
    
    /* Two-column hero layout */
    .hero-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        align-items: center;
    }
    
    /* Left side - value proposition */
    .hero-left {
        color: white;
    }
    
    .hero-headline {
        font-size: clamp(1.6rem, 3.5vw, 2.2rem) !important;
        font-weight: 700 !important;
        color: white !important;
        margin: 0 0 1rem 0 !important;
        line-height: 1.2 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .hero-description {
        font-size: clamp(0.95rem, 1.8vw, 1.1rem) !important;
        color: rgba(255, 255, 255, 0.95) !important;
        line-height: 1.6 !important;
        margin: 0 0 1rem 0 !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    .hero-cta {
        font-size: clamp(0.9rem, 1.6vw, 1rem) !important;
        color: rgba(255, 255, 255, 0.9) !important;
        margin: 0 !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    .hero-cta strong {
        color: white;
        font-weight: 600;
    }
    
    /* Right side - feature card */
    .hero-right {
        display: flex;
        justify-content: center;
    }
    
    .hero-card {
        background: white;
        border-radius: 0.8rem;
        padding: 1.25rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        width: 100%;
        max-width: 400px;
    }
    
    .hero-card-title {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #2d3748 !important;
        margin: 0 0 1rem 0 !important;
        text-align: center;
    }
    
    /* Feature badges */
    .hero-badges {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }
    
    .hero-badge {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.65rem 0.85rem;
        background: linear-gradient(135deg, rgba(255, 152, 0, 0.08) 0%, rgba(255, 152, 0, 0.04) 100%);
        border-radius: 0.5rem;
        border-left: 3px solid #ff9800;
        transition: all 0.3s ease;
        opacity: 0;
        animation: fadeUp 0.6s ease-out forwards;
    }
    
    /* Staggered animation delays for each badge */
    .hero-badge:nth-child(1) { animation-delay: 0.1s; }
    .hero-badge:nth-child(2) { animation-delay: 0.2s; }
    .hero-badge:nth-child(3) { animation-delay: 0.3s; }
    .hero-badge:nth-child(4) { animation-delay: 0.4s; }
    .hero-badge:nth-child(5) { animation-delay: 0.5s; }
    
    .hero-badge:hover {
        transform: translateX(4px) translateY(-2px);
        background: linear-gradient(135deg, rgba(255, 152, 0, 0.12) 0%, rgba(255, 152, 0, 0.06) 100%);
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.2);
    }
    
    .hero-badge-icon {
        font-size: 1.3rem;
        flex-shrink: 0;
    }
    
    .hero-badge-text {
        font-size: 0.95rem;
        font-weight: 500;
        color: #2d3748;
    }
    
    /* Mobile responsive hero */
    @media (max-width: 768px) {
        .hero-content {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .hero-section {
            padding: 1.5rem;
            margin-bottom: 1rem;
        }
        
        .hero-card {
            max-width: 100%;
        }
        
        .hero-headline {
            font-size: 1.5rem !important;
        }
        
        .hero-description {
            font-size: 0.95rem !important;
        }
    }
    
    /* ============================================
       FORM SECTION STYLING
       ============================================ */
    
    /* Form container background with stronger contrast - reduced top margin */
    .stForm {
        background: white;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
        border: 2px solid rgba(255, 152, 0, 0.15);
        margin: 0.5rem 0 1rem 0;
    }
    
    /* Form section header with subtle orange accent */
    .main h2 {
        color: #2d3748;
        border-bottom: 3px solid rgba(255, 152, 0, 0.3);
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }
    
    /* Form subheaders - reduced orange */
    .stForm h4 {
        color: #2d3748;
        font-weight: 600;
        margin-bottom: 1rem;
        border-left: 3px solid #ff9800;
        padding-left: 0.75rem;
    }
    
    /* ============================================
       DASHBOARD SECTION STYLING
       ============================================ */
    
    /* Dashboard section background */
    .main h2:first-of-type {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem 1rem 0 0;
        margin-bottom: 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #ff9800;
    }
    
    /* ============================================
       DASHBOARD METRICS - SOFT MODERN CARDS
       ============================================ */
    
    /* Metric containers with soft cream/peach background */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #fff9f5 0%, #fef6f0 100%);
        padding: 1.5rem 1.25rem;
        border-radius: 1rem;
        box-shadow: 0 2px 12px rgba(255, 152, 0, 0.08);
        border-top: 3px solid #ff9800;
        border-left: 1px solid rgba(255, 152, 0, 0.15);
        border-right: 1px solid rgba(255, 152, 0, 0.15);
        border-bottom: 1px solid rgba(255, 152, 0, 0.15);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    /* Subtle accent line on left */
    [data-testid="stMetric"]::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(180deg, #ff9800 0%, #ff6f00 100%);
        opacity: 0.6;
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 152, 0, 0.15);
        border-top-color: #ff6f00;
    }
    
    [data-testid="stMetric"]:hover::before {
        opacity: 1;
    }
    
    /* Metric labels - small, clean, uppercase */
    [data-testid="stMetric"] label {
        font-size: clamp(0.7rem, 1.1vw, 0.8rem) !important;
        font-weight: 600 !important;
        color: #888 !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.4 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.5rem !important;
        display: block !important;
    }
    
    /* Metric values - large, readable, balanced */
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-size: clamp(1.5rem, 3vw, 2.2rem) !important;
        font-weight: 700 !important;
        color: #2d3748 !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.2 !important;
        margin: 0.25rem 0 !important;
    }
    
    /* Metric delta/description - clean wrap */
    [data-testid="stMetric"] > div:last-child {
        font-size: clamp(0.8rem, 1.2vw, 0.9rem) !important;
        margin-top: 0.5rem !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        color: #666 !important;
        line-height: 1.5 !important;
        font-weight: 500 !important;
    }
    
    /* ============================================
       TABS STYLING & ANIMATION - Modern Pill Style
       ============================================ */
    
    /* Tab container with warm background and better spacing */
    .stTabs {
        background-color: white;
        border-radius: 1rem;
        padding: 2rem 1.5rem;
        margin-top: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 152, 0, 0.1);
    }
    
    /* Tab list - modern pill container */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.75rem;
        background: linear-gradient(135deg, #fff9f5 0%, #fef6f0 100%);
        border-radius: 1rem;
        padding: 0.75rem;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.04);
        border: 1px solid #f5e6d3;
        margin-bottom: 2rem;
        flex-wrap: wrap;
        justify-content: flex-start;
    }
    
    /* Individual tab buttons - pill style */
    .stTabs [data-baseweb="tab"] {
        font-size: clamp(0.85rem, 1.4vw, 0.95rem) !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.25rem !important;
        border-radius: 2rem !important;
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
        border: 2px solid transparent !important;
        background-color: transparent !important;
        color: #666 !important;
        min-height: 42px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* Inactive tab hover state */
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #fff5eb 0%, #ffe8d6 100%) !important;
        color: #ff9800 !important;
        border-color: rgba(255, 152, 0, 0.2) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 2px 8px rgba(255, 152, 0, 0.15) !important;
    }
    
    /* Active/selected tab - warm orange gradient */
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #ff9800 0%, #ff6f00 100%) !important;
        color: white !important;
        border-color: #ff6f00 !important;
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.3) !important;
        font-weight: 700 !important;
    }
    
    /* Active tab hover - slightly enhanced */
    .stTabs [aria-selected="true"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(255, 152, 0, 0.4) !important;
    }
    
    /* Tab content with animation and better spacing */
    .stTabs [data-baseweb="tab-panel"] {
        animation: slideIn 0.4s ease-out;
        padding-top: 0.5rem;
        background-color: transparent;
    }
    
    /* Mobile responsive tabs */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
            padding: 0.5rem;
            overflow-x: auto;
            overflow-y: hidden;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: thin;
            scrollbar-color: #ff9800 #f5f1e8;
        }
        
        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
            height: 6px;
        }
        
        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar-track {
            background: #f5f1e8;
            border-radius: 3px;
        }
        
        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar-thumb {
            background: #ff9800;
            border-radius: 3px;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.85rem !important;
            padding: 0.6rem 1rem !important;
            min-width: fit-content !important;
        }
    }
    
    /* ============================================
       CONTAINERS & CARDS
       ============================================ */
    
    /* Bordered containers with warm styling */
    [data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        background-color: white;
        border-radius: 0.8rem;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border: 1px solid rgba(255, 152, 0, 0.1);
        transition: box-shadow 0.3s ease;
    }
    
    [data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"]:hover {
        box-shadow: 0 4px 16px rgba(255, 152, 0, 0.15);
        border-color: rgba(255, 152, 0, 0.2);
    }
    
    /* Expanders with warm accent */
    .streamlit-expanderHeader {
        background: white;
        border-radius: 0.6rem;
        padding: 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        border-left: 4px solid #ff9800;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(255, 152, 0, 0.05);
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.15);
    }
    
    /* ============================================
       BUTTONS & INTERACTIVE ELEMENTS
       ============================================ */
    
    /* Primary button with warm orange gradient */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ff9800 0%, #ff6f00 100%);
        border: none;
        border-radius: 0.6rem;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        color: white;
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #ff6f00 0%, #e65100 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 152, 0, 0.4);
    }
    
    /* Download buttons with orange accent */
    .stDownloadButton > button {
        border-radius: 0.6rem;
        transition: all 0.3s ease;
        border: 2px solid #ff9800;
        color: #ff9800;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.2);
        background-color: rgba(255, 152, 0, 0.05);
    }
    
    /* ============================================
       SIDEBAR STYLING - DIFFERENTIATED BACKGROUND
       ============================================ */
    
    /* Sidebar with distinct warm beige background */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f5f0e8 0%, #ede7dc 100%);
        padding: 1.5rem 1rem;
        border-right: 1px solid rgba(255, 152, 0, 0.15);
    }
    
    /* Sidebar content wrapper */
    [data-testid="stSidebar"] > div {
        background-color: transparent;
    }
    
    /* Sidebar text styling */
    [data-testid="stSidebar"] .stMarkdown {
        font-size: 0.95rem;
        color: #2d3748;
        line-height: 1.6;
    }
    
    /* Sidebar section headers with orange accent */
    [data-testid="stSidebar"] h3 {
        color: #ff9800;
        border-bottom: 2px solid rgba(255, 152, 0, 0.3);
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    /* Sidebar info/success boxes with card styling */
    [data-testid="stSidebar"] [data-testid="stAlert"] {
        background-color: white;
        border-radius: 0.6rem;
        padding: 1.2rem;
        margin: 0.75rem 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #ff9800;
    }
    
    /* Sidebar feature list container */
    .sidebar-feature-list {
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
        margin: 0.75rem 0;
    }
    
    /* Individual feature item - clean card style */
    .sidebar-feature-item {
        display: flex;
        align-items: flex-start;
        gap: 0.75rem;
        background: white;
        padding: 0.85rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
        border-left: 3px solid #ff9800;
        transition: all 0.3s ease;
    }
    
    .sidebar-feature-item:hover {
        transform: translateX(4px);
        box-shadow: 0 3px 10px rgba(255, 152, 0, 0.15);
        border-left-color: #ff6f00;
    }
    
    /* Feature icon box */
    .sidebar-feature-icon {
        flex-shrink: 0;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, rgba(255, 152, 0, 0.1) 0%, rgba(255, 152, 0, 0.05) 100%);
        border-radius: 0.4rem;
        font-size: 1.1rem;
    }
    
    /*Feature content area */
    .sidebar-feature-content {
        flex: 1;
        min-width: 0;
    }
    
    /* Feature title - bold and compact */
    .sidebar-feature-title {
        font-weight: 600;
        font-size: 0.9rem;
        color: #2d3748;
        line-height: 1.3;
        margin-bottom: 0.2rem;
    }
    
    /* Feature description - subtle and compact */
    .sidebar-feature-desc {
        font-size: 0.8rem;
        color: #666;
        line-height: 1.4;
        margin: 0;
    }
    
    /* Legacy markdown lists - hidden for clean look */
    [data-testid="stSidebar"] ul {
        display: none;
    }
    
    [data-testid="stSidebar"] li {
        display: none;
    }
    
    /* Sidebar dividers */
    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 152, 0, 0.2);
        margin: 1.5rem 0;
    }
    
    /* Sidebar toggle/checkbox with card styling */
    [data-testid="stSidebar"] .stCheckbox {
        background-color: white;
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
    }
    
    /* Sidebar captions */
    [data-testid="stSidebar"] .stCaption {
        color: #666;
        font-size: 0.85rem;
        line-height: 1.5;
    }
    
    /* ============================================
       DATAFRAMES & TABLES
       ============================================ */
    
    [data-testid="stDataFrame"] {
        border-radius: 0.6rem;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border: 1px solid rgba(255, 152, 0, 0.1);
    }
    
    /* ============================================
       ALERTS & MESSAGES
       ============================================ */
    
    .stAlert {
        border-radius: 0.6rem;
        border-left: 4px solid;
        animation: slideIn 0.4s ease-out;
        background-color: white;
    }
    
    /* Success messages */
    [data-baseweb="notification"][kind="success"] {
        background-color: #e8f5e9;
        border-left-color: #4caf50;
    }
    
    /* Info messages */
    [data-baseweb="notification"][kind="info"] {
        background-color: #e3f2fd;
        border-left-color: #2196f3;
    }
    
    /* Warning messages */
    [data-baseweb="notification"][kind="warning"] {
        background-color: #fff8e1;
        border-left-color: #ff9800;
    }
    
    /* ============================================
       PROGRESS BAR
       ============================================ */
    
    .stProgress > div > div {
        background: linear-gradient(90deg, #ff9800 0%, #ff6f00 100%);
        border-radius: 1rem;
    }
    
    /* ============================================
       INPUT FIELDS & FORMS - CONSISTENT & READABLE
       ============================================ */
    
    /* Consistent font size for all form inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div,
    .stMultiSelect > div > div {
        font-size: 0.95rem !important;
        line-height: 1.5 !important;
    }
    
    /* Text input fields with consistent styling */
    .stTextInput > div > div > input {
        border: 2px solid rgba(255, 152, 0, 0.25) !important;
        border-radius: 0.5rem !important;
        padding: 0.65rem 0.9rem !important;
        background-color: white !important;
        height: 42px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        font-size: 0.95rem !important;
        color: #999 !important;
    }
    
    .stTextInput > div > div > input:hover {
        border-color: rgba(255, 152, 0, 0.4) !important;
        box-shadow: 0 2px 6px rgba(255, 152, 0, 0.1) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ff9800 !important;
        box-shadow: 0 0 0 3px rgba(255, 152, 0, 0.15) !important;
        outline: none !important;
    }
    
    /* Text area fields with adequate height */
    .stTextArea > div > div > textarea {
        border: 2px solid rgba(255, 152, 0, 0.25) !important;
        border-radius: 0.5rem !important;
        padding: 0.65rem 0.9rem !important;
        background-color: white !important;
        min-height: 100px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        resize: vertical !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        font-size: 0.95rem !important;
        color: #999 !important;
    }
    
    .stTextArea > div > div > textarea:hover {
        border-color: rgba(255, 152, 0, 0.4) !important;
        box-shadow: 0 2px 6px rgba(255, 152, 0, 0.1) !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #ff9800 !important;
        box-shadow: 0 0 0 3px rgba(255, 152, 0, 0.15) !important;
        outline: none !important;
    }
    
    /* Select/dropdown fields - prevent text clipping */
    .stSelectbox > div > div {
        border: 2px solid rgba(255, 152, 0, 0.25) !important;
        border-radius: 0.5rem !important;
        background-color: white !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        min-height: 42px !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(255, 152, 0, 0.4) !important;
        box-shadow: 0 2px 6px rgba(255, 152, 0, 0.1) !important;
        cursor: pointer !important;
    }
    
    /* Dropdown selected value - prevent clipping */
    .stSelectbox > div > div > div {
        padding: 0.65rem 0.9rem !important;
        min-height: 38px !important;
        display: flex !important;
        align-items: center !important;
    }
    
    /* Dropdown text */
    .stSelectbox [data-baseweb="select"] > div {
        font-size: 0.95rem !important;
        line-height: 1.5 !important;
    }
    
    /* Multi-select fields with consistent height */
    .stMultiSelect > div > div {
        border: 2px solid rgba(255, 152, 0, 0.25) !important;
        border-radius: 0.5rem !important;
        background-color: white !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        min-height: 100px !important;
        padding: 0.5rem !important;
    }
    
    .stMultiSelect > div > div:hover {
        border-color: rgba(255, 152, 0, 0.4) !important;
        box-shadow: 0 2px 6px rgba(255, 152, 0, 0.1) !important;
    }
    
    /* Multi-select tags */
    .stMultiSelect [data-baseweb="tag"] {
        font-size: 0.9rem !important;
        padding: 0.25rem 0.5rem !important;
        margin: 0.25rem !important;
    }
    
    /* Form labels - consistent sizing */
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label,
    .stMultiSelect > label {
        color: #2d3748 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        margin-bottom: 0.4rem !important;
        display: block !important;
    }
    
    /* Form field containers with consistent spacing and bottom padding */
    .stTextInput,
    .stTextArea,
    .stSelectbox,
    .stMultiSelect {
        margin-bottom: 1.5rem !important;
    }
    
    /* Ensure all input wrappers have consistent width */
    .stTextInput > div,
    .stTextArea > div,
    .stSelectbox > div,
    .stMultiSelect > div {
        width: 100% !important;
    }
    
    /* Ensure all inner input containers are full width */
    .stTextInput > div > div,
    .stTextArea > div > div,
    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        width: 100% !important;
    }
    
    /* Ensure last field in each column has adequate bottom space */
    .stTextInput:last-of-type,
    .stTextArea:last-of-type,
    .stSelectbox:last-of-type,
    .stMultiSelect:last-of-type {
        margin-bottom: 2rem !important;
    }
    
    /* Form columns should have equal padding for alignment */
    .stForm [data-testid="column"] {
        padding: 0 0.75rem !important;
    }
    
    .stForm [data-testid="column"]:first-child {
        padding-left: 0 !important;
        padding-right: 0.75rem !important;
    }
    
    .stForm [data-testid="column"]:last-child {
        padding-left: 0.75rem !important;
        padding-right: 0 !important;
    }
    
    /* Help text / captions */
    .stTextInput + div,
    .stTextArea + div,
    .stSelectbox + div,
    .stMultiSelect + div {
        color: #666 !important;
        font-size: 0.85rem !important;
        margin-top: 0.25rem !important;
        line-height: 1.4 !important;
    }
    
    /* ============================================
       MOBILE RESPONSIVENESS
       ============================================ */
    
    @media (max-width: 768px) {
        /* Reduce padding on mobile */
        .main .block-container {
            padding: 1rem !important;
        }
        
        /* Stack metrics vertically on mobile */
        [data-testid="column"] {
            min-width: 100% !important;
            margin-bottom: 1rem;
        }
        
        /* Adjust hero section */
        .hero-section {
            padding: 1.5rem;
        }
        
        /* Smaller tab buttons on mobile */
        .stTabs [data-baseweb="tab"] {
            padding: 0.5rem 0.7rem;
            font-size: 0.85rem !important;
        }
        
        /* Adjust form columns */
        [data-testid="stHorizontalBlock"] {
            flex-direction: column;
        }
        
        /* Sidebar adjustments */
        [data-testid="stSidebar"] {
            padding: 0.5rem;
        }
    }
    
    @media (max-width: 480px) {
        /* Extra small screens */
        h1 {
            font-size: 1.5rem !important;
        }
        
        .hero-section {
            padding: 1rem;
        }
        
        [data-testid="stMetric"] {
            padding: 0.8rem;
        }
    }
    
    /* ============================================
       PRINT STYLES
       ============================================ */
    
    @media print {
        .stButton, .stDownloadButton, [data-testid="stSidebar"] {
            display: none !important;
        }
    }
    </style>
    """

# Made with Bob
