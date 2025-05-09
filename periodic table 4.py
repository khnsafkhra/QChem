import streamlit as st
import random

# --- Sidebar untuk memilih game ---
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# --- Styling aesthetic & background dengan gambar kimia ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

    .stApp {
        background: url('https://images.unsplash.com/photo-1581092160614-b8d1f1cf1515?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .question-card {
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        padding: 25px; border-radius: 20px;
        box-shadow: 4px 4px 30px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        animation: fadeIn 1s ease-in-out;
        color: #fff;
    }
    .score-box {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        padding: 15px; border-radius: 12px;
        font-size: 18px; font-weight: 600;
        text-align: center; color: white;
        margin-top: 10px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; padding: 10px 24px;
        border-radius: 10px; border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        filter: brightness(1.1); transform: scale(1.03);
    }
    .stTextInput>div>div>input {
        background-color: #fff !important;
        color: #000 !important;
        border: 1px solid #ccc; border-radius: 10px;
    }
    @keyframes fadeIn {
        from {opacity:0; transform:translateY(20px);}
        to {opacity:1; transform:translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# === GAME 1: Kuis Tabel Periodik ===
NUM_PT = 5

if selected_game == "Kuis Tabel Periodik":
    st.title("🧪 Kuis Tabel Periodik Unsur")

    periodic_table = [
        {"name":"hidrogen","symbol":"H","number":1,"group":1,"period":1},
        {"name":"helium","symbol":"He","number":2,"group":18,"period":1},
        {"name":"litium","symbol":"Li","number":3,"group":1,"period":2},
        {"name":"berilium","symbol":"Be","number":4,"group":2,"period":2},
        {"name":"karbon","symbol":"C","number":6,"group":14,"period":2},
        {"name":"oksigen","symbol":"O","number":8,"group":16,"period":2},
        {"name":"natrium","symbol":"Na","number":11,"group":1,"period":3},
        {"name":"kalsium","symbol":"Ca","number":20,"group":2,"period":4},
        {"name":"nitrogen","symbol":"N","number":7,"group":15,"period":2},
        {"name":"magnesium","symbol":"Mg","number":12,"group":2,"period":3},
        {"name":"aluminium","symbol":"Al","number":13,"group":13,"period":3},
        {"name":"klorin","symbol":"Cl","number":17,"group":17,"period":3},
        {"name":"fosfor","symbol":"P","number":15,"group":15,"period":3},
        {"name":"argon","symbol":"Ar","number":18,"group":18,"period":3},
        {"name":"kalium","symbol":"K","number":19,"group":1,"period":4},
        {"name":"mangan","symbol":"Mn","number":25,"group":7,"period":4},
        {"name":"besi","symbol":"Fe","number":26,"group":8,"period":4},
        {"name":"tembaga","symbol":"Cu","number":29,"group":11,"period":4},
        {"name":"zinc","symbol":"Zn","number":30,"group":12,"period":4},
        {"name":"fluorin","symbol":"F","number":9,"group":17,"period":2},
        {"name":"neon","symbol":"Ne","number":10,"group":18,"period":2},
        {"name":"silikon","symbol":"Si","number":14,"group":14,"period":3},
        {"name":"nikel","symbol":"Ni","number":28,"group":10,"period":4},
    ]

    # Inisialisasi session state
    if "pt_score" not in st.session_state:
        st.session_state.pt_score = 0
        st.session_state.pt_index = 0
        st.session_state.pt_q = None
        st.session_state.pt_feedback = ""
        st.session_state.pt_answered = False

    st.progress(st.session_state.pt_index / NUM_PT)

    def new_pt_q():
        return {"el": random.choice(periodic_table), "type": random.choice(["symbol", "number", "group", "period"])}

    if st.session_state.pt_index < NUM_PT:
        if st.session_state.pt_q is None:
            st.session_state.pt_q = new_pt_q()
            st.session_state.pt_answered = False

        q = st.session_state.pt_q
        e = q["el"]
        ans = str(e[q["type"]])
        question_map = {

