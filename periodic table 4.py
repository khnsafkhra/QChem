import streamlit as st
import random

# --- Sidebar untuk memilih game ---
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["Kuis Tabel Periodik", "Kuis Senyawa Organik"])

# --- Styling aesthetic & background gradient ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

    .stApp {
        background: linear-gradient(to right, #f8cdda, #1d2b64);
        background-attachment: fixed;
        color: white;
    }
    .question-card {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 20px;
        box-shadow: 4px 4px 30px rgba(0,0,0,0.2);
        margin-bottom: 25px;
        animation: fadeIn 1s ease-in-out;
        color: #fff;
    }
    .score-box {
        background: rgba(0,0,0,0.25);
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

    # (Data dan logika kuis tabel periodik tidak diubah)

# === GAME 2: Kuis Senyawa Organik ===
elif selected_game == "Kuis Senyawa Organik":
    st.title("🧪 Kuis Senyawa Organik")

    organic_questions = [
        {"q":"Apa rumus molekul dari metana?", "a":"CH4"},
        {"q":"Apa gugus fungsi dari alkohol?", "a":"OH"},
        {"q":"Apa nama senyawa CH3COOH?", "a":"Asam asetat"},
        {"q":"Apa nama senyawa dengan rumus C2H5OH?", "a":"Etanol"},
        {"q":"Apa nama senyawa C6H6?", "a":"Benzena"},
    ]

    if "org_score" not in st.session_state:
        st.session_state.org_score = 0
        st.session_state.org_index = 0
        st.session_state.org_feedback = ""
        st.session_state.org_answered = False

    if st.session_state.org_index < len(organic_questions):
        q = organic_questions[st.session_state.org_index]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.org_index+1} dari {len(organic_questions)}")
        ans_in = st.text_input(f"🔬 {q['q']}", key=f"org_in_{st.session_state.org_index}")

        if st.button("Kirim Jawaban", key=f"org_sub_{st.session_state.org_index}") and not st.session_state.org_answered:
            if ans_in.strip().lower() == q['a'].lower():
                st.session_state.org_score += 1
                st.session_state.org_feedback = "✅ Jawaban Benar!"
                st.balloons()
            else:
                st.session_state.org_feedback = f"❌ Salah. Jawaban benar: {q['a']}"
            st.session_state.org_answered = True

        st.write(st.session_state.org_feedback)

        if st.session_state.org_answered:
            st.markdown("### ✅ Jawaban telah dikirim!")
            if st.button("➡️ Lanjut ke Soal Berikutnya", key=f"org_next_{st.session_state.org_index}"):
                st.session_state.org_index += 1
                st.session_state.org_feedback = ""
                st.session_state.org_answered = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>🌟 Skor: {st.session_state.org_score}/{len(organic_questions)}</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.org_score}/{len(organic_questions)}")
        if st.button("🔁 Ulangi Kuis"):
            for k in ["org_score", "org_index", "org_feedback", "org_answered"]:
                del st.session_state[k]
