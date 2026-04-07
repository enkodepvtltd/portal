import streamlit as st
import random

# --- Page Setup ---
st.set_page_config(page_title="Lineage Portal", layout="centered")

# Initialize Session State variables
if 'stage' not in st.session_state:
    st.session_state.stage = 'auth'
if 'errors' not in st.session_state:
    st.session_state.errors = []
if 'yes_scale' not in st.session_state:
    st.session_state.yes_scale = 1.0
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = {"top": 70, "left": 60}

# --- Global CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: white; font-family: "Comic Sans MS", cursive; }
    @keyframes flash {
        0% { background: #ff00ff; }
        50% { background: #00ffff; }
        100% { background: #ffff00; }
    }
    .ultimate-container {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        animation: flash 0.1s infinite; z-index: 10; display: flex;
        align-items: center; justify-content: center;
    }
    .popup {
        position: fixed; width: 220px; background: #ccc; border: 3px outset white;
        padding: 10px; color: black; z-index: 500; font-family: Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Logic Functions ---
def move_no_button():
    st.session_state.no_pos = {"top": random.randint(20, 80), "left": random.randint(10, 80)}
    st.session_state.yes_scale += 0.4
    new_err = {
        "id": random.random(),
        "top": random.randint(20, 70),
        "left": random.randint(10, 70),
        "msg": random.choice(["ERROR: DNA MISMATCH", "WARNING: SHIBU DETECTED", "UNAUTHORIZED DENIAL"])
    }
    st.session_state.errors.append(new_err)
    if len(st.session_state.errors) > 8:
        st.session_state.stage = 'virus'

# --- Stage 1: Auth ---
if st.session_state.stage == 'auth':
    st.markdown("<div style='border: 2px solid lime; padding: 30px; text-align: center; background: #111;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: lime;'>🔐 SECURE LINEAGE PORTAL</h1>", unsafe_allow_html=True)
    st.write("Accessing records for: **PATTI SHIBU CLAN**")
    if st.button("ENTER PORTAL"):
        st.session_state.stage = 'question'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- Stage 2: The Question ---
elif st.session_state.stage == 'question':
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>Final Confirmation: <br/> Is Patti Shibu your father?</h1>", unsafe_allow_html=True)
    
    # Yes Button (using a standard button that grows)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("YES (I ACCEPT MY FATE)", use_container_width=True):
            st.session_state.stage = 'ultimate'
            st.rerun()
    
    # The "No" Button (Moving using HTML injection)
    st.markdown(f"""
        <div style="position: fixed; top: {st.session_state.no_pos['top']}%; left: {st.session_state.no_pos['left']}%; z-index: 1000;">
            <button style="padding: 10px 30px; background: red; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: not-allowed;">
                NO
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Secretly trigger the "No" logic when they try to click anywhere or use this helper
    if st.button("No? Click here to confirm denial"):
        move_no_button()
        st.rerun()

    # Error Popups
    for err in st.session_state.errors:
        st.markdown(f"""
            <div class="popup" style="top: {err['top']}%; left: {err['left']}%">
                <div style="background: darkblue; color: white; font-size: 0.7rem; padding: 2px;">System Message</div>
                <p style="font-size: 0.9rem; font-weight: bold;">{err['msg']}</p>
                <button>OK</button>
            </div>
            """, unsafe_allow_html=True)

# --- Stage 3: Virus ---
elif st.session_state.stage == 'virus':
    st.markdown("<div style='position:fixed; top:0; left:0; width:100vw; height:100vh; background:red; text-align:center; padding-top:100px; z-index:9999;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 5rem;'>SYSTEM CRASH!!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 2rem;'>Too many lies detected. Lineage auto-confirmed.</p>", unsafe_allow_html=True)
    if st.button("FIX SYSTEM"):
        st.session_state.stage = 'ultimate'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- Stage 4: Ultimate ---
elif st.session_state.stage == 'ultimate':
    st.markdown("""
        <div class="ultimate-container">
            <div style="background: yellow; padding: 50px; border: 15px solid white; border-radius: 20px; text-align: center; color: black; box-shadow: 0 0 100px black;">
                <h1 style="font-size: 3.5rem;">CONFIRMED! ✅</h1>
                <p style="font-size: 1.5rem; color: red; font-weight: 900;">HAPPY TO BE A FRIEND OF <br/> PATTI SHIBU'S DAUGHTER</p>
                <h2 style="color: blue;">(adhava Dog Shibu's daughter)</h2>
                <p style="font-size: 3rem;">🐕🦴🐕🦴🐕</p>
            </div>
            <marquee style="font-size: 6rem; position: absolute; top: 10%;">🐕🐕🐕🐕🐕🐕🐕🐕🐕</marquee>
            <marquee direction="right" style="font-size: 6rem; position: absolute; bottom: 10%;">🦴🦴🦴🦴🦴🦴🦴🦴🦴</marquee>
        </div>
        """, unsafe_allow_html=True)
