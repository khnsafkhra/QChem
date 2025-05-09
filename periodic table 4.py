import streamlit as st
import random

# --- Sidebar ---
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Kimia Organik"])

# --- Aesthetic Background & CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

    .stApp {
        background-image: url('https://images.unsplash.com/photo-1581090700227-1e8e1b2849b0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    .question-card {
        background: rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        padding: 25px; border-radius: 20px;
        box-shadow: 0 0 20px rgba(255,255,255,0.2);
        margin-bottom: 25px;
        color: #fff;
    }

    .score-box {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(5px);
        padding: 15px; border-radius: 12px;
        font-size: 18px; font-weight: 600;
        text-align: center; color: white;
        margin-top: 10px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
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
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ===================== KUIS TABEL PERIODIK =====================
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
    ]

    if "pt_score" not in st.session_state:
        st.session_state.pt_score = 0
        st.session_state.pt_index = 0
        st.session_state.pt_q = None
        st.session_state.pt_feedback = ""
        st.session_state.pt_answered = False

    st.progress(st.session_state.pt_index / NUM_PT)

    def new_pt_q():
        el = random.choice(periodic_table)
        typ = random.choice(["symbol", "number", "group", "period"])
        return {"el": el, "type": typ}

    if st.session_state.pt_index < NUM_PT:
        if st.session_state.pt_q is None:
            st.session_state.pt_q = new_pt_q()
            st.session_state.pt_answered = False

        q = st.session_state.pt_q
        e = q["el"]
        question_map = {
            "symbol": f"Apa simbol dari unsur {e['name'].capitalize()}?",
            "number": f"Berapa nomor atom dari {e['name'].capitalize()}?",
            "group": f"Golongan berapa unsur {e['name'].capitalize()}?",
            "period": f"Periode berapa unsur {e['name'].capitalize()}?"
        }
        ans = str(e[q["type"]])

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.pt_index+1} dari {NUM_PT}")
        user = st.text_input(f"🧪 {question_map[q['type']]}", key=f"pt_in_{st.session_state.pt_index}")

        if st.button("Kirim Jawaban", key=f"pt_sub_{st.session_state.pt_index}") and not st.session_state.pt_answered:
            if user.strip().lower() == ans.lower():
                st.session_state.pt_score += 1
                st.session_state.pt_feedback = "✅ Jawaban Benar!"
                st.balloons()
            else:
                st.session_state.pt_feedback = f"❌ Salah. Jawaban benar: {ans}"
            st.session_state.pt_answered = True

        st.write(st.session_state.pt_feedback)

        if st.session_state.pt_answered:
            if st.button("➡️ Soal Berikutnya", key=f"pt_next_{st.session_state.pt_index}"):
                st.session_state.pt_index += 1
                st.session_state.pt_q = None
                st.session_state.pt_feedback = ""
                st.session_state.pt_answered = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>🌟 Skor: {st.session_state.pt_score}/{NUM_PT}</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.pt_score}/{NUM_PT}")
        if st.button("🔁 Ulangi Kuis"):
            for k in ["pt_score", "pt_index", "pt_q", "pt_feedback", "pt_answered"]:
                del st.session_state[k]

# ===================== KUIS KIMIA ORGANIK =====================
elif selected_game == "Kuis Kimia Organik":
    st.title("🧪 Kuis Kimia Organik")

    organic_questions = [
        {"q": "Apa rumus molekul dari metana?", "a": "CH4"},
        {"q": "Apa gugus fungsi dari alkohol?", "a": "OH"},
        {"q": "Apa nama senyawa CH3COOH?", "a": "Asam asetat"},
        {"q": "Apa nama senyawa dengan rumus C2H5OH?", "a": "Etanol"},
        {"q": "Apa nama senyawa C6H6?", "a": "Benzena"},
        {"q": "Apa rumus molekul dari etana?", "a": "C2H6"},
        {"q": "Apa
