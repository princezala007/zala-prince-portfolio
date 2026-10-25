import streamlit as st

st.set_page_config(page_title="Zala Prince Rajeshbhai | Engineering Hub 🚀", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #00f2fe !important; font-family: 'Poppins', sans-serif; }
    .custom-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 25px; border-radius: 15px; border-left: 5px solid #00f2fe; margin-bottom: 20px;
    }
    .custom-card-2 {
        background: linear-gradient(135deg, #2e1065 0%, #0f172a 100%);
        padding: 25px; border-radius: 15px; border-left: 5px solid #f43f5e; margin-bottom: 20px;
    }
    .profile-img { border-radius: 50%; border: 3px solid #00f2fe; display: block; margin: auto; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown('<img src="https://flaticon.com" class="profile-img" width="110">', unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: white !important;'>🔥 ઝાલા પ્રિન્સ</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #94a3b8;'>B.Tech Computer Engineering<br><b>Class of 2026 - 2030</b></p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

page = st.sidebar.radio("🌐 નેવિગેશન મેનુ:", ["🚀 Dashboard Intro", "📅 4-Year Live Timeline", "🛠️ My Tech Stack", "💻 Live Projects"])

if page == "🚀 Dashboard Intro":
    st.markdown("# 👋 Welcome to My Digital Space")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="custom-card"><h3>🎯 હું કોણ છું?</h3><p style="color: #cbd5e1;">મારું નામ <b>ઝાલા પ્રિન્સ</b> છે. હું એક કોમ્પ્યુટર એન્જિનિયરિંગ સ્ટુડન્ટ છું. આ મારો <b>Live Progress Tracker</b> છે.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="custom-card-2"><h3 style="color: #f43f5e !important;">⚡ મારો મંત્ર</h3><p style="color: #cbd5e1; font-style: italic;">"રોજ ૧% નવું શીખવું અને પ્રોજેક્ટ્સને સીધા લાઈવ સર્વર પર મૂકવા!"</p></div>', unsafe_allow_html=True)

elif page == "📅 4-Year Live Timeline":
    st.markdown("# ⏳ મારી એન્જિનિયરિંગ ટાઈમલાઈન")
    st.markdown('<div class="custom-card"><h3>🚀 1st Year — પાયો અને શરૂઆત (Active ⚡)</h3><p style="color: #cbd5e1;">Python પ્રોગ્રામિંગ શીખવાનું ચાલુ કર્યું અને પોતાની પહેલી લાઈવ બેન્કિંગ સિસ્ટમ વેબસાઈટ બનાવી!</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-card" style="opacity: 0.5;"><h3>💻 2nd Year — Core Concepts (Locked 🔒)</h3><p style="color: #a1a1aa;">Data Structures (DSA) અને Full Stack Web Development શીખવું છે.</p></div>', unsafe_allow_html=True)

elif page == "🛠️ My Tech Stack":
    st.markdown("# 🛠️ મારી સ્કિલ્સ અને કમાન્ડ")
    st.write("🐍 Python Programming"); st.progress(85)
    st.write("🚀 Streamlit Framework"); st.progress(75)

elif page == "💻 Live Projects":
    st.markdown("# 💻 મેં બનાવેલા જોરદાર પ્રોજેક્ટ્સ")
    st.markdown('<div class="custom-card"><h3>🏦 1. Mini Banking System Simulator</h3><p style="color: #cbd5e1;">Python અને Streamlit થી બનેલો લાઈવ પ્રોગ્રામ.</p></div>', unsafe_allow_html=True)
    
    if 'balance' not in st.session_state: st.session_state.balance = 5000.0
    st.metric(label="Current Account Balance", value=f"₹{st.session_state.balance:,.2f}")
    action = st.selectbox("Select Transaction", ["Deposit (જમા કરો)", "Withdraw (ઉપાડો)"])
    amount = st.number_input("Enter Amount (₹)", min_value=0.0, step=100.0)
    if st.button("Submit"):
        if action == "Deposit (જમા કરો)":
            st.session_state.balance += amount
            st.success(f"₹{amount} જમા થઈ ગયા!")
        elif action == "Withdraw (ઉપાડો)":
            if amount > st.session_state.balance: st.error("પૂરતા પૈસા નથી!")
            else:
                st.session_state.balance -= amount
                st.warning(f"₹{amount} ઉપાડી લીધા!")
