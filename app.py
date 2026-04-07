import streamlit as st
import streamlit.components.v1 as components

# --- Forced Mobile Optimization ---
st.set_page_config(
    page_title="⚠️ SYSTEM CRITICAL ⚠️", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- THE ULTIMATE ANDROID TROLL ENGINE ---
# Features: Haptic feedback, Fullscreen lock, and Escaping buttons
troll_code = """
<div id="virus-screen" style="
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: #000; color: #0f0; z-index: 999999; 
    font-family: 'Courier New', monospace; overflow: hidden;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 20px; box-sizing: border-box; text-align: center;">

    <div id="setup">
        <h1 style="font-size: 2.5rem; color: red;">🛑 SECURITY BREACH 🛑</h1>
        <p style="font-size: 1.2rem;">DNA Mismatch: 'Patti Shibu' Strain Detected.</p>
        <button onclick="startTroll()" style="
            background: #0f0; color: black; padding: 20px; 
            border: none; font-weight: bold; font-size: 1.5rem; margin-top: 20px;">
            CLEAN SYSTEM
        </button>
    </div>

    <div id="main-troll" style="display: none; width: 100%;">
        <h2 id="msg" style="font-size: 1.8rem; color: yellow;">ARE YOU PATTI SHIBU'S DAUGHTER?</h2>
        
        <div style="height: 300px; width: 100%; position: relative; margin-top: 50px;">
            <button id="yes-btn" onclick="win()" style="
                padding: 20px 40px; background: #0f0; border: 5px solid white;
                font-weight: bold; position: absolute; left: 50%; top: 20%;
                transform: translateX(-50%); z-index: 100; transition: 0.1s;">
                YES (I CONFIRM)
            </button>

            <button id="no-btn" ontouchstart="moveNo()" style="
                padding: 15px 30px; background: red; color: white;
                border: none; font-weight: bold; position: absolute; left: 50%; top: 70%;
                transform: translateX(-50%); transition: 0.05s;">
                NO
            </button>
        </div>
    </div>
</div>

<script>
    const setup = document.getElementById('setup');
    const main = document.getElementById('main-troll');
    const noBtn = document.getElementById('no-btn');
    const yesBtn = document.getElementById('yes-btn');
    const msg = document.getElementById('msg');
    const screen = document.getElementById('virus-screen');

    let scale = 1;
    let lies = 0;

    function startTroll() {
        // Request Fullscreen for Android
        if (document.documentElement.requestFullscreen) {
            document.documentElement.requestFullscreen();
        }
        setup.style.display = 'none';
        main.style.display = 'block';
    }

    function moveNo() {
        // Vibrate phone on 'No' attempt
        if (navigator.vibrate) navigator.vibrate(100);
        
        // Move No Button
        noBtn.style.left = (Math.random() * 70 + 5) + '%';
        noBtn.style.top = (Math.random() * 70 + 5) + '%';
        noBtn.innerText = "ACCESS DENIED 🐕";
        
        // Grow Yes Button
        scale += 0.4;
        yesBtn.style.transform = `translateX(-50%) scale(${scale})`;
        
        lies++;
        if (lies > 5) {
            screen.style.animation = "shake 0.1s infinite";
            msg.innerText = "THE DOG BLOOD IS STRONG IN YOU!";
            msg.style.color = "orange";
        }
        if (lies > 10) {
            alert("CRITICAL ERROR: DNA verified as Dog Shibu. Stop resisting.");
        }
    }

    function win() {
        if (navigator.vibrate) navigator.vibrate([200, 100, 200]);
        screen.innerHTML = `
            <div style="width: 100%; height: 100%; animation: strobe 0.05s infinite; 
                 display: flex; flex-direction: column; align-items: center; justify-content: center; color: black;">
                <div style="background: white; padding: 30px; border: 15px solid black; transform: rotate(-5deg);">
                    <h1 style="font-size: 3rem;">CERTIFIED ✅</h1>
                    <h2 style="color: red;">DAUGHTER OF PATTI SHIBU</h2>
                    <p style="font-size: 1.5rem;">(The Dog of the Century)</p>
                    <marquee style="font-size: 5rem;">🐕🦴🐕🦴🐕</marquee>
                    <p style="font-size: 1rem; margin-top: 20px;">Verification by ENKode CyberLabs</p>
                </div>
            </div>
        `;
    }

    // Styles for vibrations and strobes
    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes shake { 0% {left:2px;} 50% {left:-2px;} 100% {left:0;} }
        @keyframes strobe { 
            0% {background: #ff00ff;} 33% {background: #00ffff;} 
            66% {background: #ffff00;} 100% {background: #ff00ff;} 
        }
    `;
    document.head.appendChild(style);
</script>
"""

# --- Injecting into Streamlit ---
components.html(troll_code, height=800)

# Cleaning up Streamlit UI
st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden !important;}
    .stApp {background: black !important;}
    </style>
    """, unsafe_allow_html=True)
