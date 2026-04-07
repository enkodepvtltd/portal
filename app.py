import streamlit as st
import streamlit.components.v1 as components

# Force a clean mobile slate
st.set_page_config(page_title="Message for You", layout="centered")

max_troll_html = """
<div id="box" style="
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: #fffafa; z-index: 999999; overflow: hidden;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    font-family: 'Georgia', serif; transition: 0.3s;">

    <div id="bait" style="text-align: center; padding: 20px;">
        <h1 style="color: #4a4a4a; font-size: 1.8rem;">A Special Memory</h1>
        <div style="font-size: 5rem; margin: 20px 0;">🎁</div>
        <p style="color: #777;">I put our best moments here. Open to view.</p>
        <button onclick="activate()" style="
            margin-top: 20px; padding: 15px 40px; background: #ff4b4b; 
            color: white; border: none; border-radius: 50px; font-weight: bold;">
            View Memory
        </button>
    </div>

    <div id="virus" style="display: none; width: 100%; height: 100%; position: relative; background: #000;">
        <h2 id="warn" style="color: #0f0; font-family: monospace; font-size: 1.2rem; padding: 20px; text-align: center;">
            [SYSTEM]: ACCESSING ENKODE BIO-LOCK...
        </h2>

        <div style="position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%); width: 100%; display: flex; justify-content: center;">
            <button id="yes" onclick="finish()" style="
                padding: 20px; background: #0f0; color: #000; font-weight: 900;
                border: 5px solid #fff; font-size: 1.2rem; transition: 0.1s;
                white-space: normal; width: 80%; max-width: 90vw;">
                YES, I ADMIT I AM PATTI SHIBU'S DAUGHTER
            </button>
        </div>

        <button id="no" ontouchstart="chaos(event)" style="
            position: absolute; left: 50%; top: 75%; transform: translateX(-50%);
            padding: 10px 20px; background: red; color: white; border: none;
            font-weight: bold; border-radius: 5px; font-size: 1rem;">
            I AM NOT
        </button>
    </div>
</div>

<script>
    let clicks = 0;
    const box = document.getElementById('box');
    const bait = document.getElementById('bait');
    const virus = document.getElementById('virus');
    const yes = document.getElementById('yes');
    const no = document.getElementById('no');
    const warn = document.getElementById('warn');

    function activate() {
        if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen();
        bait.style.display = 'none';
        virus.style.display = 'block';
        box.style.background = '#000';
        if (navigator.vibrate) navigator.vibrate([100, 50, 100]);
    }

    function chaos(e) {
        e.preventDefault();
        clicks++;
        if (navigator.vibrate) navigator.vibrate(150);

        // 1. MEGA GROWTH (The choice is being removed)
        let newScale = 1 + (clicks * 0.6);
        yes.style.transform = `scale(${newScale})`;
        
        // 2. TELEPORT + INSULTS
        no.style.left = (Math.random() * 60 + 20) + '%';
        no.style.top = (Math.random() * 60 + 20) + '%';
        const msgs = ["DOG GENES!", "STOP LYING", "SHIBU BLOOD", "ACCEPT IT", "WOOF!"];
        no.innerText = msgs[clicks % msgs.length];

        // 3. VISUAL DISTORTION (Makes her think her screen is broken)
        if (clicks > 3) {
            box.style.filter = "blur(1px) contrast(200%)";
            warn.innerText = "CRITICAL: DNA MATCH POSITIVE. CEASE RESISTANCE.";
            warn.style.color = "red";
        }
        if (clicks > 6) {
            box.style.animation = "shake 0.05s infinite";
        }
    }

    function finish() {
        if (navigator.vibrate) navigator.vibrate([1000, 200, 1000]);
        box.style.filter = "none";
        box.style.animation = "none";
        box.innerHTML = `
            <div style="height:100vh; width:100vw; animation: strobe 0.04s infinite; display:flex; align-items:center; justify-content:center; padding: 20px; box-sizing: border-box;">
                <div style="background:white; color:black; padding:30px; border:10px solid black; text-align:center; transform: rotate(-3deg); width: 90%;">
                    <h1 style="font-size: 2.5rem; margin:0;">VERIFIED ✅</h1>
                    <h2 style="color:red; font-size: 1.5rem; margin: 10px 0;">OFFICIAL DAUGHTER OF</h2>
                    <h1 style="color: blue; font-size: 2.8rem; line-height: 1;">PATTI SHIBU</h1>
                    <p style="font-size: 1.2rem; font-weight: bold; margin-top: 10px;">(Adhava Dog Shibu's Daughter)</p>
                    <marquee scrollamount="30" style="font-size: 5rem;">🐕🦴🐕</marquee>
                    <div style="background:black; color:white; padding:10px; font-family: monospace; font-size: 0.8rem;">
                        ENKode DNA REGISTRY #69420
                    </div>
                </div>
            </div>
        `;
    }

    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes shake { 0% {transform:translate(5px,5px);} 50% {transform:translate(-5px,-5px);} 100% {transform:translate(0,0);} }
        @keyframes strobe { 0% {background:#f0f;} 50% {background:#0ff;} 100% {background:#ff0;} }
    `;
    document.head.appendChild(style);
</script>
"""

# Inject and hide Streamlit UI
components.html(max_troll_html, height=800)
st.markdown("<style>header, footer, #MainMenu {visibility: hidden !important;} .stApp {background: #fffafa !important;}</style>", unsafe_allow_html=True)
