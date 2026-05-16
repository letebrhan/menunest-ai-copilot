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
    
    /* Overall page background - warm cream color */
    .stApp {
        background: linear-gradient(135deg, #faf8f3 0%, #f5f1e8 100%);
    }
    
    /* Main content area with fade-in animation */
    .main .block-container {
        animation: fadeIn 0.6s ease-out;
        background-color: transparent;
        padding: 2rem 1rem;
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
       HERO SECTION STYLING
       ============================================ */
    
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.2);
        animation: fadeIn 0.8s ease-out;
    }
    
    .hero-section h3 {
        color: white !important;
        margin-top: 0 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .hero-section p {
        color: rgba(255, 255, 255, 0.95) !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    /* ============================================
       FORM SECTION STYLING
       ============================================ */
    
    /* Form container background */
    .stForm {
        background: white;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 152, 0, 0.1);
    }
    
    /* Form section header */
    .main h2 {
        color: #2d3748;
        border-bottom: 3px solid #ff9800;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }
    
    /* Form subheaders */
    .stForm h4 {
        color: #ff9800;
        font-weight: 600;
        margin-bottom: 1rem;
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
       DASHBOARD METRICS - RESPONSIVE
       ============================================ */
    
    /* Metric containers with warm orange accent */
    [data-testid="stMetric"] {
        background: white;
        padding: 1.2rem;
        border-radius: 0.8rem;
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.1);
        border: 2px solid rgba(255, 152, 0, 0.2);
        transition: all 0.3s ease;
        animation: pulse 2s ease-in-out infinite;
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(255, 152, 0, 0.25);
        border-color: #ff9800;
        animation: none;
    }
    
    /* Metric labels - responsive with warm color */
    [data-testid="stMetric"] label {
        font-size: clamp(0.75rem, 1.2vw, 0.9rem) !important;
        font-weight: 600 !important;
        color: #ff9800 !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Metric values - responsive with dark text */
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important;
        font-weight: 700 !important;
        color: #2d3748 !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.2 !important;
    }
    
    /* Metric delta/description */
    [data-testid="stMetric"] > div:last-child {
        font-size: clamp(0.8rem, 1.3vw, 0.95rem) !important;
        margin-top: 0.5rem !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        color: #666 !important;
    }
    
    /* ============================================
       TABS STYLING & ANIMATION
       ============================================ */
    
    /* Tab container with warm background */
    .stTabs {
        background-color: white;
        border-radius: 0.8rem;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 152, 0, 0.1);
    }
    
    /* Tab buttons */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background-color: #faf8f3;
        border-radius: 0.6rem;
        padding: 0.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        font-size: clamp(0.85rem, 1.4vw, 1rem) !important;
        font-weight: 500;
        padding: 0.6rem 1rem;
        border-radius: 0.4rem;
        transition: all 0.3s ease;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        color: #666;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(255, 152, 0, 0.1);
        transform: translateY(-2px);
        color: #ff9800;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #ff9800 0%, #ff6f00 100%) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.3);
    }
    
    /* Tab content with animation */
    .stTabs [data-baseweb="tab-panel"] {
        animation: slideIn 0.4s ease-out;
        padding-top: 1.5rem;
        background-color: white;
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
       SIDEBAR STYLING
       ============================================ */
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #faf8f3 0%, #f5f1e8 100%);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        font-size: 0.95rem;
        color: #2d3748;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #ff9800;
        border-bottom: 2px solid #ff9800;
        padding-bottom: 0.5rem;
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
       INPUT FIELDS & FORMS
       ============================================ */
    
    /* Text inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div {
        border-color: rgba(255, 152, 0, 0.2);
        border-radius: 0.5rem;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > div:focus {
        border-color: #ff9800;
        box-shadow: 0 0 0 2px rgba(255, 152, 0, 0.1);
    }
    
    /* Form labels */
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label,
    .stMultiSelect > label {
        color: #2d3748;
        font-weight: 600;
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
