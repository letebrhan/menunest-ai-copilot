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
    
    /* Apply fade-in to main content */
    .main .block-container {
        animation: fadeIn 0.6s ease-out;
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
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
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
       DASHBOARD METRICS - RESPONSIVE
       ============================================ */
    
    /* Metric containers */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.2rem;
        border-radius: 0.8rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        animation: pulse 2s ease-in-out infinite;
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
        animation: none;
    }
    
    /* Metric labels - responsive */
    [data-testid="stMetric"] label {
        font-size: clamp(0.75rem, 1.2vw, 0.9rem) !important;
        font-weight: 600 !important;
        color: #4a5568 !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
    }
    
    /* Metric values - responsive */
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
    }
    
    /* ============================================
       TABS STYLING & ANIMATION
       ============================================ */
    
    /* Tab container */
    .stTabs {
        background-color: #f8f9fa;
        border-radius: 0.8rem;
        padding: 1rem;
        margin-top: 1rem;
    }
    
    /* Tab buttons */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background-color: white;
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
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #f0f2f6;
        transform: translateY(-2px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    /* Tab content with animation */
    .stTabs [data-baseweb="tab-panel"] {
        animation: slideIn 0.4s ease-out;
        padding-top: 1.5rem;
    }
    
    /* ============================================
       CONTAINERS & CARDS
       ============================================ */
    
    /* Bordered containers */
    [data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        background-color: white;
        border-radius: 0.8rem;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        transition: box-shadow 0.3s ease;
    }
    
    [data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"]:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
        border-radius: 0.6rem;
        padding: 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #e8eef5 0%, #d9e2ec 100%);
        transform: translateX(4px);
    }
    
    /* ============================================
       BUTTONS & INTERACTIVE ELEMENTS
       ============================================ */
    
    /* Primary button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 0.6rem;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Download buttons */
    .stDownloadButton > button {
        border-radius: 0.6rem;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* ============================================
       SIDEBAR STYLING
       ============================================ */
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        font-size: 0.95rem;
    }
    
    /* ============================================
       DATAFRAMES & TABLES
       ============================================ */
    
    [data-testid="stDataFrame"] {
        border-radius: 0.6rem;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }
    
    /* ============================================
       ALERTS & MESSAGES
       ============================================ */
    
    .stAlert {
        border-radius: 0.6rem;
        border-left: 4px solid;
        animation: slideIn 0.4s ease-out;
    }
    
    /* Success messages */
    [data-baseweb="notification"][kind="success"] {
        background-color: #d4edda;
        border-left-color: #28a745;
    }
    
    /* Info messages */
    [data-baseweb="notification"][kind="info"] {
        background-color: #d1ecf1;
        border-left-color: #17a2b8;
    }
    
    /* Warning messages */
    [data-baseweb="notification"][kind="warning"] {
        background-color: #fff3cd;
        border-left-color: #ffc107;
    }
    
    /* ============================================
       PROGRESS BAR
       ============================================ */
    
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 1rem;
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
