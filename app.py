import streamlit as st
import streamlit.components.v1 as components

# Forced Layout
st.set_page_config(page_title="Personal Message", layout="centered")

ultimate_troll = """
<div id="main-container" style="
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: #fffafa; z-index: 999999; overflow: hidden;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    font-family: 'Serif', 'Times New Roman'; transition: 0.5s;">

    <div id="bait" style="text-align: center; padding: 20px;">
        <div style="font-size: 100px; filter: drop-shadow(0 10px 10px rgba(0,0,0,0.1));">🎁</div>
        <h1 style="color: #4a4a4a; font-weight: 100;">A Small Token</h1>
        <p style="color: #999;">I spent a lot of time putting this together for you.<br>I hope you appreciate the honesty in it.</p>
        <button onclick="activate()" style="
            margin-top: 40px; padding: 18px 60px; background: #000; 
            color: #fff; border: none; border-radius: 2px; font-size: 1rem;
            letter-spacing: 3px; cursor: pointer; text-transform: uppercase;">
            Open Gift
        </button>
    </div>

    <div id="hijack" style="display: none; width: 100%; height: 100%; position: relative; background: #000;">
        <div id="glitch-overlay" style="position:absolute; width:100%; height:100%; pointer-events:none; opacity:0.1; background: repeating-linear-gradient(0deg, #0f0, #0f0 1px, transparent 1px, transparent 2px);"></div>
        
        <h1 id="warning-text" style="color: #0f0; font-family: monospace; font-size: 1.5rem; padding: 40px 20px;">
            [ALERTTT]: DNA CORRUPTION DETECTED...
        </h1>

        <button id="yes-btn" onclick="terminate()" style="
            position: absolute; left: 50%; top: 40%; transform: translate(-50%, -50%);
            padding: 30px 60px; background: #0f0; color: #000; font-weight: 900;
            border: 10px solid #fff; font-size: 2rem; z-index: 10000; transition: 0.05s;">
            YES, I AM SHIBU'S DAUGHTER
        </button>

        <button id="no-btn" ontouchstart="chaos(event)" style="
            position: absolute; left: 50%; top: 80%; transform: translate(-50%, -50%);
            padding: 20px 40px; background: red; color: white; border: none;
            font-weight: bold; font-size: 1.2rem; z-index: 500;">
            NO
        </button>
    </div>
</div>

<script>
    let grow = 1;
    let rage = 0;
    const container = document.getElementById('main-container');
    const bait = document.getElementById('bait');
    const hijack = document.getElementById('hijack');
    const yes = document.getElementById('yes-btn');
    const no = document.getElementById('no-btn');
    const warn = document.getElementById('warning-text');

    function activate() {
        if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen();
        bait.style.display = 'none';
        hijack.style.display = 'block';
        container.style.background = '#000';
        if (navigator.vibrate) navigator.vibrate([100, 50, 100, 50, 300]);
    }

    function chaos(e) {
        e.preventDefault();
        rage++;
        
        // PHYSICAL FEEDBACK
        if (navigator.vibrate) navigator.vibrate(200);

        // INSTANT MEGA GROWTH (The "Submit" Logic)
        grow += 1.2; 
        yes.style.transform = `translate(-50%, -50%) scale(${grow})`;
        
        // TELEPORT NO + MOCKERY
        no.style.left = Math.random() * 80 + 10 + '%';
        no.style.top = Math.random() * 80 + 10 + '%';
        const msgs = ["DOG GENES!", "STOP LYING", "SHIBU BLOOD", "ACCEPT IT", "WOOF?"];
        no.innerText = msgs[Math.floor(Math.random()*msgs.length)];

        // VISUAL ATTACK
        container.style.background = 'white';
        setTimeout(() => { container.style.background = 'black'; }, 30);

        if (rage > 4) {
            warn.innerText = "CRITICAL: PATTI SHIBU BIOMETRICS CONFIRMED. RESISTANCE IS FUTILE.";
            warn.style.color = "red";
            warn.style.fontSize = "2rem";
            container.style.animation = "vibrate 0.05s infinite";
        }
    }

    function terminate() {
        if (navigator.vibrate) navigator.vibrate([1000, 200, 1000]);
        container.innerHTML = `
            <div style="height:100vh; width:100vw; animation: strobe 0.03s infinite; display:flex; align-items:center; justify-content:center;">
                <div style="background:white; color:black; padding:50px; border:20px solid black; text-align:center; transform:scale(1.2) rotate(-5deg);">
                    <h1 style="font-size:4rem; margin:0;">VERIFIED ✅</h1>
                    <h2 style="color:red; font-size:2rem;">PATTI SHIBU'S DAUGHTER</h2>
                    <p style="font-size:1.5rem;">(Adhava Dog Shibu's Daughter)</p>
                    <marquee scrollamount="60" style="font-size:10rem;">🐕🦴🐕</marquee>
                    <h1 style="background:black; color:white; padding:10px;">CERTIFIED SHIBU</h1>
                </div>
            </div>
        `;
    }

    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes vibrate { 0% {transform:translate(4px,4px);} 50% {transform:translate(-4px,-4px);} 100% {transform:translate(0,0);} }
        @keyframes strobe { 0% {background:#f0f;} 50% {background:#0ff;} 100% {background:#ff0;} }
    `;
    document.head.appendChild(style);
</script>
"""

components.html(ultimate_troll, height=1000)

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden !important;}
    .stApp {background: #fffafa !important;}
    </style>
    """, unsafe_allow_html=True)
