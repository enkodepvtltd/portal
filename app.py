import streamlit as st
import streamlit.components.v1 as components
import random

# --- Hardcore Page Config ---
st.set_page_config(page_title="⚠️ CRITICAL SYSTEM FAILURE ⚠️", layout="wide", initial_sidebar_state="collapsed")

# --- THE "VIRUS" JAVASCRIPT ---
# This is the engine of the troll. It overrides Streamlit's CSS.
troll_engine = """
<script>
    const d = window.parent.document;
    
    function injectChaos() {
        const buttons = d.querySelectorAll('button');
        let yesBtn, noBtn;
        
        buttons.forEach(b => {
            if (b.innerText.includes('YES')) yesBtn = b;
            if (b.innerText.includes('NO')) noBtn = b;
        });

        if (yesBtn && noBtn) {
            // 1. THE NO BUTTON ESCAPE ENGINE
            d.onmousemove = (e) => {
                const bx = noBtn.getBoundingClientRect();
                const distance = Math.sqrt(Math.pow(e.clientX - (bx.left + bx.width/2), 2) + Math.pow(e.clientY - (bx.top + bx.height/2), 2));
                
                // If mouse gets within 150px, teleport the No button
                if (distance < 150) {
                    noBtn.style.position = 'fixed';
                    noBtn.style.transition = 'none';
                    noBtn.style.left = Math.random() * 80 + 'vw';
                    noBtn.style.top = Math.random() * 80 + 'vh';
                    noBtn.style.zIndex = '9999';
                    noBtn.style.background = 'red';
                    noBtn.innerText = "CAN'T TOUCH THIS 🐕";
                    
                    // 2. THE YES BUTTON GROWTH ENGINE
                    const currentScale = parseFloat(yesBtn.style.transform.replace('scale(', '')) || 1;
                    yesBtn.style.transform = `scale(${currentScale + 0.15})`;
                    yesBtn.style.position = 'fixed';
                    yesBtn.style.zIndex = '9998';
                }
            };
        }
    }
    setInterval(injectChaos, 100);
</script>
"""

# --- STYLING THE NIGHTMARE ---
st.markdown("""
    <style>
    /* Hide all Streamlit branding */
    header, footer, #MainMenu {visibility: hidden !important;}
    
    .stApp {
        background: #000 !important;
    }

    /* Screen Shaking Effect */
    @keyframes earthquake {
        0% { transform: translate(0,0); }
        10% { transform: translate(-5px,-5px); }
        20% { transform: translate(5px,5px); }
        100% { transform: translate(0,0); }
    }
    .shake-screen {
        animation: earthquake 0.1s infinite;
    }

    .shibu-text {
        font-family: "Comic Sans MS", cursive !important;
        color: #ff00ff !important;
        text-shadow: 5px 5px #00ffff;
        font-size: 5rem !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP FLOW ---
if 'stage' not in st.session_state:
    st.session_state.stage = 'auth'

if st.session_state.stage == 'auth':
    st.markdown("<h1 class='shibu-text'>🚨 PATTI SHIBU FIREWALL 🚨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white;'>Unauthorized access to ENKode files. Identify yourself.</p>", unsafe_allow_html=True)
    if st.button("I AM PATTI SHIBU'S DAUGHTER (Click to Enter)"):
        st.session_state.stage = 'chaos'
        st.rerun()

elif st.session_state.stage == 'chaos':
    # Inject the JavaScript Engine
    components.html(troll_engine, height=0)
    
    st.markdown("<div class='shake-screen'>", unsafe_allow_html=True)
    st.markdown("<h1 class='shibu-text'>GENETIC LOCK DETECTED</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:yellow;'>Confirm your identity as the daughter of the Dog (Patti Shibu)</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES (I ACCEPT MY SHIBU BLOOD)", key="yes_btn"):
            st.session_state.stage = 'ultimate'
            st.rerun()
    with col2:
        st.button("NO", key="no_btn")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Fake browser alerts
    if random.random() > 0.8:
        st.toast("🐕 WOOF! WOOF! WOOF!", icon="🚨")

elif st.session_state.stage == 'ultimate':
    st.markdown("""
        <style>
        @keyframes strobe {
            0% {background: #ff0000;} 10% {background: #00ff00;} 
            20% {background: #0000ff;} 30% {background: #ffff00;} 
            40% {background: #ff00ff;} 100% {background: #00ffff;}
        }
        .stApp { animation: strobe 0.05s infinite !important; }
        </style>
        <div style="background: white; border: 30px double black; padding: 50px; text-align: center; transform: rotate(-5deg);">
            <h1 style="color: black !important; font-size: 6rem;">SHIBU STATUS: ACTIVE ✅</h1>
            <h2 style="color: red !important; font-size: 3rem;">OFFICIALLY PATTI SHIBU'S DAUGHTER</h2>
            <marquee scrollamount="100" style="font-size: 10rem;">🐕🦴🐕🦴🐕🦴🐕🦴🐕</marquee>
            <marquee direction="right" scrollamount="80" style="font-size: 10rem;">🦴🐕🦴🐕🦴🐕🦴🐕🦴</marquee>
            <h1 style="color: blue !important;">(Confirmed by ENKode DNA Labs)</h1>
        </div>
    """, unsafe_allow_html=True)
