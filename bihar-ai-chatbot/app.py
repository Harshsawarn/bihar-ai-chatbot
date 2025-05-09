import streamlit as st
from PIL import Image
import base64
import json
import os

# Custom CSS with Bihar theme
def local_css():
    st.markdown(f"""
    <style>
        /* Main container */
        .stApp {{
            background: linear-gradient(135deg, #f8f4e9 0%, #fff9e6 100%);
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><path fill="%23FF993310" d="M30,10L50,30L70,10L90,30L70,50L90,70L70,90L50,70L30,90L10,70L30,50L10,30L30,10Z"/></svg>');
            background-size: 40px 40px;
        }}
        
        /* Header area */
        .header {{
            background: linear-gradient(90deg, #FF9933 0%, #138808 100%);
            padding: 2rem;
            border-radius: 0 0 20px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }}
        .header::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><path fill="%23ffffff20" d="M20,20L80,20L80,80L20,80Z" transform="rotate(45 50 50)"/></svg>');
            background-size: 60px 60px;
            opacity: 0.3;
        }}
        .header h1 {{
            color: white;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
            position: relative;
            font-size: 2.5rem;
        }}
        .header .logo {{
            height: 80px;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));
        }}
        
        /* Chat containers */
        .stChatMessage {{
            border-radius: 15px !important;
            padding: 1rem 1.5rem !important;
            margin: 0.5rem 0 !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        }}
        .stChatMessage[data-testid="user"] {{
            background-color: #13880810 !important;
            border-left: 4px solid #138808 !important;
        }}
        .stChatMessage[data-testid="assistant"] {{
            background-color: #FF993310 !important;
            border-left: 4px solid #FF9933 !important;
        }}
        
        /* Input area */
        .stTextInput>div>div>input {{
            border-radius: 20px !important;
            padding: 12px 20px !important;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.1) !important;
            border: 1px solid #FF9933 !important;
        }}
        .stButton button {{
            background: linear-gradient(90deg, #FF9933 0%, #e67300 100%) !important;
            color: white !important;
            border-radius: 20px !important;
            padding: 8px 20px !important;
            font-weight: 500 !important;
            border: none !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
            transition: all 0.3s !important;
        }}
        .stButton button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
        }}
        
        /* Sidebar */
        .sidebar .sidebar-content {{
            background: linear-gradient(180deg, #ffffff 0%, #f8f4e9 100%) !important;
            border-right: 1px solid #FF993330 !important;
            box-shadow: 2px 0 10px rgba(0,0,0,0.05) !important;
        }}
        .sidebar .sidebar-content .block-container {{
            padding-top: 1rem !important;
        }}
        
        /* Timeline cards */
        .timeline-card {{
            background: white;
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
            border-left: 4px solid #FF9933;
        }}
        .timeline-card h4 {{
            color: #138808;
            margin-top: 0;
        }}
        
        /* Responsive adjustments */
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8rem !important;
            }}
        }}
    </style>
    """, unsafe_allow_html=True)

# Bihar-themed header component
def bihar_header():
    header_html = f"""
    <div class="header">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <img src="data:image/png;base64,{get_image_base64('images/bihar_logo.png')}" class="logo">
            <div>
                <h1>बिहार विरासत AI</h1>
                <p style="color: white; margin: 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3)">Explore Bihar's Rich Heritage</p>
            </div>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

# Helper function for image handling
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    return ""

# Initialize session state
def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant",
            "content": "नमस्ते! मैं बिहार विरासत AI हूँ। आप बिहार के इतिहास, संस्कृति, अर्थव्यवस्था या किसी भी विषय के बारे में पूछ सकते हैं।"
        })

# Main app function
def main():
    # Configure page
    st.set_page_config(
        page_title="Bihar Heritage AI",
        page_icon="🇮🇳",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load custom CSS
    local_css()
    
    # Display Bihar-themed header
    bihar_header()
    
    # Initialize session
    init_session()
    
    # Sidebar with enhanced UI
    with st.sidebar:
        
        st.markdown("""
        <div style="background: #FF993310; padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem;">
            <h3 style="color: #138808; margin-top: 0;">Quick Facts</h3>
            <p>• Birthplace of Buddhism</p>
            <p>• Home to ancient Nalanda</p>
            <p>• 60% of India's lychee production</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Language selector
        selected_lang = st.selectbox(
            "भाषा चुनें / Select Language",
            ["Hindi", "English", "Maithili", "Bhojpuri"],
            index=0,
            key="lang_select"
        )
        
        # Voice controls
        st.markdown("### Voice Controls")
        col1, col2 = st.columns(2)
        with col1:
            voice_input = st.toggle("Mic Input", True)
        with col2:
            voice_output = st.toggle("Voice Output", True)
        
        # Historical timeline
        st.markdown("### Bihar Timeline")
        with open('data/historical_timeline.json', 'r') as f:
            timeline = json.load(f)
        for era in timeline[:3]:  # Show first 3 by default
            with st.expander(f"{era['period']}"):
                st.markdown(f"""
                <div class="timeline-card">
                    <h4>{era['title']}</h4>
                    <p>{era['description']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Main chat area
    chat_container = st.container()
    with chat_container:
        # Display chat messages
        for message in st.session_state.messages:
            avatar = "🧑💻" if message["role"] == "user" else "🤖"
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])
        
        # Chat input with Bihar-themed design
        input_col, button_col = st.columns([5, 1])
        with input_col:
            prompt = st.chat_input("बिहार के बारे में अपना प्रश्न पूछें...")
        with button_col:
            if st.button("भेजें", use_container_width=True):  # "Send" in Hindi
                pass  # Handled by chat_input
    
    # Handle chat interaction
    if prompt:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Generate response (simplified for UI demo)
        response = f"यह {prompt} के बारे में एक नमूना प्रतिक्रिया है। वास्तविक AI एकीकरण के लिए मॉडल हैंडलर को जोड़ें।"
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update chat
        st.rerun()

if __name__ == "__main__":
    main()
