import streamlit as st
import streamlit.components.v1 as components
import random

# --- Page Config ---
st.set_page_config(page_title="🚨 SYSTEM BREACH 🚨", layout="wide")

# --- THE JAVASCRIPT INJECTION (The "Actual" Troll) ---
# This script handles the movement in real-time without waiting for the server.
troll_js = """
<script>
    const doc = window.parent.document;
    
    function setupTroll() {
        const yesBtn = doc.querySelector('button[kind="primary"]');
        const noBtn = doc.querySelector('button[kind="secondary"]');
        
        if (noBtn) {
            noBtn.onmouseover = () => {
                noBtn.style.position = 'fixed';
                noBtn.style.left = Math.random() * 80 + 'vw';
                noBtn.style.top = Math.random() * 80 + 'vh';
                noBtn.innerText = "WRONG ANSWER 🐕";
                
                // Make Yes grow every time she misses No
                const currentScale = parseFloat(yesBtn.style.transform.replace('scale(', '')) || 1;
                yesBtn.style.transform = `scale(${currentScale + 0.3})`;
                yesBtn.style.transition = 'transform 0.1s';
            };
        }
    }

    // Run setup every second to catch Streamlit's rerenders
    setInterval(setupTroll, 1000);
</script>
"""

# --- GLOBAL STYLES ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000 !important;
        background-image: url("https://www.transparenttextures.com/patterns/carbon-fibre.png");
    }
    h1, h2, p {
        color: #00ff00 !important;
        font-family: 'Courier New', Courier, monospace !important;
        text-shadow: 2px 2px #ff0000;
    }
    /* Hide the annoying Streamlit bar */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* The Glitch Effect */
    .glitch {
        animation: glitch 1s linear infinite;
    }
    @keyframes glitch {
        2%, 64% { transform: translate(2px,0) skew(0deg); }
        4%, 60% { transform: translate(-2px,0) skew(0deg); }
        62% { transform: translate(0,0) skew(5deg); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'

if st.session_state.stage == 'start':
    st.markdown("<h1 class='glitch'>⚠️ ENKode SECURITY ALERT</h1>", unsafe_allow_html=True)
    st.write("Unidentified DNA detected. Please confirm lineage to proceed to the ENKode dashboard.")
    if st.button("RUN DNA SCAN"):
        st.session_state.stage = 'troll'
        st.rerun()

elif st.session_state.stage == 'troll':
    components.html(troll_js, height=0) # Inject the virus
    
    st.markdown("<h1 style='text-align:center;'>GENETIC MATCH FOUND:</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color: yellow !important;'>Are you the daughter of Patti Shibu (The Dog)?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES, I AM A SHIBU", type="primary", use_container_width=True):
            st.session_state.stage = 'win'
            st.rerun()
    with col2:
        st.button("NO", type="secondary", use_container_width=True)
        
    st.markdown("---")
    st.write("*(Note: Clicking 'NO' is a violation of ENKode policy #69)*")

elif st.session_state.stage == 'win':
    st.markdown("""
        <style>
        @keyframes bg { 
            0% {background: red;} 25% {background: blue;} 
            50% {background: green;} 75% {background: yellow;} 100% {background: red;} 
        }
        .stApp { animation: bg 0.1s infinite !important; }
        </style>
        <div style="background: white; padding: 50px; border: 20px solid black; text-align: center; color: black; border-radius: 50px;">
            <h1 style="font-size: 5rem; color: black !important;">DNA VERIFIED ✅</h1>
            <h2 style="color: red !important;">WELCOME HOME</h2>
            <h1 style="font-size: 4rem; color: blue !important;">PATTI SHIBU'S DAUGHTER</h1>
            <p style="font-size: 5rem;">🐕🐕🐕</p>
            <marquee scrollamount="30">YOU CANNOT ESCAPE THE SHIBU BLOODLINE</marquee>
            <marquee direction="right" scrollamount="40">WOOF WOOF WOOF WOOF</marquee>
        </div>
    """, unsafe_allow_html=True)

# Fake Error Popups that spawn randomly
if st.session_state.stage == 'troll' and random.random() > 0.7:
    st.toast("🚨 WARNING: LIES DETECTED", icon="🐕")
