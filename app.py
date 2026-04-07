import streamlit as st
import streamlit.components.v1 as components

# --- FULL SCREEN TAKEOVER ---
st.set_page_config(page_title="🚨 FATAL ERROR: SHIBU_VIRUS 🚨", layout="wide", initial_sidebar_state="collapsed")

# --- THE POLTERGEIST ENGINE (JS) ---
# This is where the real trolling happens.
troll_engine = """
<script>
    const d = window.parent.document;
    let clickCount = 0;

    function absoluteChaos() {
        const buttons = d.querySelectorAll('button');
        let yesBtn, noBtn;
        
        buttons.forEach(b => {
            if (b.innerText.includes('YES')) yesBtn = b;
            if (b.innerText.includes('NO')) noBtn = b;
        });

        if (noBtn && yesBtn) {
            // 1. THE REJECTED 'NO'
            noBtn.onmouseover = () => {
                noBtn.style.position = 'fixed';
                noBtn.style.left = Math.random() * 90 + 'vw';
                noBtn.style.top = Math.random() * 90 + 'vh';
                noBtn.style.transform = `rotate(${Math.random() * 360}deg)`;
                noBtn.innerText = "LIES! 🐕";
                
                // 2. THE GROWING 'YES' (Covers everything)
                clickCount++;
                const scale = 1 + (clickCount * 0.5);
                yesBtn.style.position = 'fixed';
                yesBtn.style.left = '50%';
                yesBtn.style.top = '50%';
                yesBtn.style.transform = `translate(-50%, -50%) scale(${scale})`;
                yesBtn.style.zIndex = '10000';
                
                // 3. COLOR INVERSION TROLL
                if(clickCount > 5) {
                    d.body.style.filter = clickCount % 2 === 0 ? 'invert(1)' : 'invert(0)';
                }
            };
        }
    }
    
    // Force the engine to run every 50ms
    setInterval(absoluteChaos, 50);
    
    // Block the escape key
    d.onkeydown = (e) => {
        if(e.key === 'Escape') {
            alert("ESC IS DISABLED FOR PATTI SHIBU'S DAUGHTER");
            return false;
        }
    };
</script>
"""

# --- THE VISUAL NIGHTMARE (CSS) ---
st.markdown("""
    <style>
    /* Hide Everything Streamlit */
    header, footer, #MainMenu {visibility: hidden !important;}
    .stApp { background: #000 !important; overflow: hidden !important; }

    @keyframes glitch {
        0% { clip: rect(44px, 9999px, 56px, 0); transform: skew(0.5deg); }
        100% { clip: rect(12px, 9999px, 90px, 0); transform: skew(0.5deg); }
    }
    .glitch-title {
        font-family: 'Courier New', monospace;
        font-size: 6rem;
        font-weight: bold;
        color: #00ff00;
        text-align: center;
        animation: glitch 0.1s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
if 'stage' not in st.session_state:
    st.session_state.stage = 'lock'

if st.session_state.stage == 'lock':
    st.markdown("<h1 class='glitch-title'>DATABASE LOCKED</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:red; font-size: 2rem;'>ENKode Bio-Metric Scanner: DNA Match found with 'Patti Shibu'</p>", unsafe_allow_html=True)
    if st.button("VERIFY DNA"):
        st.session_state.stage = 'chaos'
        st.rerun()

elif st.session_state.stage == 'chaos':
    components.html(troll_engine, height=0)
    st.markdown("<h1 style='color:white; text-align:center;'>FINAL VERIFICATION</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:yellow; text-align:center;'>Are you Patti Shibu's biological daughter?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES (I CONFIRM MY DOG HERITAGE)", type="primary"):
            st.session_state.stage = 'ultimate'
            st.rerun()
    with col2:
        st.button("NO", type="secondary")

elif st.session_state.stage == 'ultimate':
    st.markdown("""
        <style>
        @keyframes flash-chaos {
            0% { background: #ff00ff; }
            20% { background: #00ffff; }
            40% { background: #ffff00; }
            60% { background: #ff0000; }
            80% { background: #00ff00; }
            100% { background: #ffffff; }
        }
        .stApp { animation: flash-chaos 0.03s infinite !important; }
        </style>
        <div style="position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); 
                    background:white; color:black; padding:100px; border:30px solid black; 
                    z-index:99999; text-align:center; min-width:80vw;">
            <h1 style="font-size: 8rem;">CONFIRMED ✅</h1>
            <h2 style="font-size: 4rem; color:red;">PATTI SHIBU'S DAUGHTER</h2>
            <marquee scrollamount="60" style="font-size: 10rem;">🐕🦴🐕🦴🐕🦴🐕🦴🐕</marquee>
            <marquee direction="right" scrollamount="100" style="font-size: 10rem;">🦴🐕🦴🐕🦴🐕🦴🐕🦴</marquee>
            <h1 style="font-size: 5rem;">(Dog Shibu Supremacy)</h1>
        </div>
    """, unsafe_allow_html=True)
