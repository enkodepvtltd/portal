import streamlit as st
import streamlit.components.v1 as components

# --- Mobile-First Layout ---
st.set_page_config(page_title="A Message for You", layout="centered")

troll_html = """
<div id="wrapper" style="
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: #fff5f5; z-index: 999999; overflow: hidden;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    transition: all 0.5s ease;">

    <div id="letter-stage" style="text-align: center; padding: 30px; font-family: 'Georgia', serif;">
        <div style="font-size: 5rem; margin-bottom: 20px;">✉️</div>
        <h1 style="color: #d63384; font-style: italic;">To Someone Special</h1>
        <p style="color: #555; line-height: 1.6; font-size: 1.1rem;">
            I've been thinking about our friendship and everything we've been through. 
            I wanted to share something sincere with you... 
            please open this digital envelope to see the truth.
        </p>
        <button onclick="triggerTwist()" style="
            background: #d63384; color: white; padding: 15px 40px; 
            border: none; border-radius: 30px; font-size: 1.2rem; 
            cursor: pointer; box-shadow: 0 4px 15px rgba(214, 51, 132, 0.3);">
            Open Heartfelt Letter
        </button>
    </div>

    <div id="chaos-stage" style="display: none; width: 100%; text-align: center;">
        <h1 id="warning" style="font-family: 'Courier New', monospace; color: red; font-size: 2rem;">
            ⚠️ SCANNING GENETICS... ⚠️
        </h1>
        <div id="button-area" style="height: 400px; width: 100%; position: relative;">
            <button id="yes-btn" onclick="finishHim()" style="
                position: absolute; left: 50%; top: 30%; transform: translateX(-50%);
                padding: 20px 40px; background: #28a745; color: white; 
                border: 4px solid #fff; font-weight: bold; font-size: 1.5rem; z-index: 10;">
                YES, I AM A SHIBU
            </button>
            <button id="no-btn" ontouchstart="trollNo()" style="
                position: absolute; left: 50%; top: 70%; transform: translateX(-50%);
                padding: 15px 30px; background: #000; color: #fff; border: none;
                font-weight: bold;">
                I AM NOT
            </button>
        </div>
    </div>
</div>

<script>
    const wrapper = document.getElementById('wrapper');
    const letter = document.getElementById('letter-stage');
    const chaos = document.getElementById('chaos-stage');
    const noBtn = document.getElementById('no-btn');
    const yesBtn = document.getElementById('yes-btn');
    const warning = document.getElementById('warning');
    
    let scale = 1;
    let attempts = 0;

    function triggerTwist() {
        // Fullscreen for Android impact
        if (document.documentElement.requestFullscreen) {
            document.documentElement.requestFullscreen();
        }
        
        // Sudden switch from Pink to Black/Matrix style
        letter.style.display = 'none';
        chaos.style.display = 'block';
        wrapper.style.backgroundColor = 'black';
        
        if (navigator.vibrate) navigator.vibrate([100, 50, 100]);
    }

    function trollNo() {
        attempts++;
        if (navigator.vibrate) navigator.vibrate(80);
        
        // Move NO button randomly
        noBtn.style.left = Math.random() * 80 + '%';
        noBtn.style.top = Math.random() * 80 + '%';
        noBtn.innerText = "LIES DETECTED 🐕";
        
        // Scale YES button to take over
        scale += 0.5;
        yesBtn.style.transform = `translateX(-50%) scale(${scale})`;
        
        if (attempts > 5) {
            wrapper.style.animation = "glitch 0.1s infinite";
            warning.innerText = "DNA CONFIRMED: 100% DOG";
        }
    }

    function finishHim() {
        if (navigator.vibrate) navigator.vibrate([500, 100, 500]);
        wrapper.innerHTML = `
            <div style="height: 100vh; width: 100vw; animation: strobe 0.05s infinite; 
                 display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;">
                <div style="background: yellow; border: 20px solid black; padding: 40px; transform: rotate(5deg);">
                    <h1 style="color: black; font-size: 3rem;">CERTIFIED ✅</h1>
                    <h2 style="color: red; font-size: 2rem;">THE REAL DAUGHTER OF</h2>
                    <h1 style="color: blue; font-size: 4.5rem;">PATTI SHIBU</h1>
                    <p style="font-size: 1.5rem; color: black;">(Adhava Dog Shibu's Daughter)</p>
                    <marquee scrollamount="40" style="font-size: 6rem;">🐕🐕🐕🐕🐕</marquee>
                    <h3 style="background: black; color: white; padding: 10px;">PROUD BLOODLINE</h3>
                </div>
            </div>
        `;
    }

    // CSS Animations
    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes glitch { 0% { filter: hue-rotate(0deg); } 50% { filter: invert(1); } 100% { filter: hue-rotate(360deg); } }
        @keyframes strobe { 0% { background: #ff00ff; } 50% { background: #00ffff; } 100% { background: #ffff00; } }
    `;
    document.head.appendChild(style);
</script>
"""

# --- Inject HTML ---
components.html(troll_html, height=1000)

# Hide Streamlit Default UI
st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden !important;}
    .stApp {background: #fff5f5 !important;}
    </style>
    """, unsafe_allow_html=True)
