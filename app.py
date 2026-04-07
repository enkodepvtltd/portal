import streamlit as st
import random

# --- Total Page Takeover ---
st.set_page_config(page_title="🚨 SYSTEM CRITICAL 🚨", layout="wide", initial_sidebar_state="collapsed")

# Initialize State
if 'stage' not in st.session_state:
    st.session_state.stage = 'auth'
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'yes_scale' not in st.session_state:
    st.session_state.yes_scale = 1.0

# --- THE CHAOS CSS ---
st.markdown(f"""
    <style>
    /* Hide Streamlit UI elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    .stApp {{
        background-color: #000;
        cursor: url('https://cur.cursors-4u.net/ani/ani-1/ani1.ani'), auto;
    }}

    /* Vibrating text effect */
    @keyframes shake {{
        0% {{ transform: translate(1px, 1px) rotate(0deg); }}
        10% {{ transform: translate(-1px, -2px) rotate(-1deg); }}
        20% {{ transform: translate(-3px, 0px) rotate(1deg); }}
        100% {{ transform: translate(1px, -2px) rotate(-1deg); }}
    }}

    .troll-text {{
        color: #ff0000;
        font-family: "Comic Sans MS", cursive;
        animation: shake 0.5s infinite;
        text-shadow: 2px 2px #fff;
    }}

    /* Floating No Button */
    .no-button {{
        position: fixed;
        transition: all 0.1s ease-in-out;
        z-index: 9999;
    }}

    /* Ultimate Flash */
    @keyframes party {{
        0% {{ background: #ff00ff; }}
        33% {{ background: #00ffff; }}
        66% {{ background: #ffff00; }}
        100% {{ background: #ff00ff; }}
    }}
    .party-bg {{
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        animation: party 0.05s infinite; z-index: 10000;
        display: flex; align-items: center; justify-content: center;
        flex-direction: column;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Stage 1: The Trap ---
if st.session_state.stage == 'auth':
    st.markdown("<h1 class='troll-text' style='text-align:center; font-size: 4rem;'>🛑 DNA ACCESS RESTRICTED 🛑</h1>", unsafe_allow_html=True)
    st.write("### Detecting 'Patti Shibu' genetics in your browser cache...")
    if st.button("PROVE YOU ARE NOT A DOG"):
        st.session_state.stage = 'question'
        st.rerun()

# --- Stage 2: The Impossible Question ---
elif st.session_state.stage == 'question':
    st.markdown("<h1 class='troll-text' style='text-align:center;'>IS PATTI SHIBU YOUR REAL FATHER?</h1>", unsafe_allow_html=True)
    
    # The Yes Button grows based on how many times she tries to click No
    yes_size = 15 + (st.session_state.clicks * 20)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # Actual Streamlit button to trigger the win
        if st.button("YES (I SURRENDER)", key="win_btn"):
            st.session_state.stage = 'ultimate'
            st.rerun()
        # Visual overlay for the growing Yes button
        st.markdown(f"""
            <div style="position: fixed; top: 40%; left: 10%; z-index: 1000;">
                <button style="font-size: {yes_size}px; padding: 20px; background: lime; border: 5px solid white; cursor: pointer;">
                    YES
                </button>
            </div>
        """, unsafe_allow_html=True)

    # The "No" Button - Moves randomly every time the page refreshes
    no_x = random.randint(10, 80)
    no_y = random.randint(10, 80)
    
    st.markdown(f"""
        <div style="position: fixed; top: {no_y}%; left: {no_x}%; z-index: 9999;">
            <button style="padding: 15px 40px; background: red; color: white; font-weight: bold; transform: rotate({random.randint(-20, 20)}deg);">
                NO
            </button>
        </div>
    """, unsafe_allow_html=True)

    # Invisible "Ghost" buttons that cover the screen to trigger reruns
    if st.button("Try to click NO", use_container_width=True):
        st.session_state.clicks += 1
        if st.session_state.clicks > 10:
            st.session_state.stage = 'bsod'
        st.rerun()

# --- Stage 3: Fake Blue Screen ---
elif st.session_state.stage == 'bsod':
    st.markdown("""
        <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #0000aa; color: white; padding: 50px; font-family: monospace; z-index: 99999;">
            <h1>:(</h1>
            <h2>Your PC ran into a Shibu problem and needs to restart.</h2>
            <p>If you call support, give them this info: ERROR_Patti_Daughter_Detected</p>
            <p>Completeing DNA Acceptance: 69%...</p>
        </div>
    """, unsafe_allow_html=True)
    import time
    # This automatically pushes her to the final stage after 3 seconds
    if st.button("RESTART SYSTEM (CLICK HERE)"):
        st.session_state.stage = 'ultimate'
        st.rerun()

# --- Stage 4: THE PEAK SHIBU ---
elif st.session_state.stage == 'ultimate':
    st.markdown("""
        <div class="party-bg">
            <div style="background: white; padding: 40px; border: 20px solid black; text-align: center; transform: scale(1.5);">
                <h1 style="color: black; font-size: 5rem;">CERTIFIED ✅</h1>
                <h2 style="color: red;">OFFICIAL DAUGHTER OF</h2>
                <h1 style="color: blue; font-size: 4rem;">PATTI SHIBU</h1>
                <p style="font-size: 1rem;">(Woof Woof! 🐕)</p>
            </div>
            <div style="font-size: 10rem;">🐕🦴🐕🦴🐕</div>
            <marquee scrollamount="50" style="font-size: 8rem;">🐕🐕🐕🐕🐕🐕🐕🐕🐕🐕🐕🐕</marquee>
            <marquee direction="right" scrollamount="40" style="font-size: 8rem;">🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴</marquee>
        </div>
    """, unsafe_allow_html=True)
