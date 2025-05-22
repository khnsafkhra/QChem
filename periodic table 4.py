import streamlit as st
import random

st.set_page_config(page_title="QChems", layout="centered")

# ===== CSS Styling =====
st.markdown("""
    <style>
    body {
        background-color: #f2f2f2;
        font-family: 'Arial', sans-serif;
    }
    .question-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .score-box {
        font-size: 18px;
        margin-top: 20px;
        color: #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

# ===== Sidebar Navigation =====
st.sidebar.title("🧠 QChems")
selected_game = st.sidebar.radio("Pilih Kuis", ["Beranda", "Kuis Tabel Periodik", "Kuis Senyawa Organik"])

# ===== Halaman Beranda =====
if selected_game == "Beranda":
    st.title("🔬 Selamat Datang di QChems!")
    st.markdown("""
    **QChems** adalah aplikasi kuis edukatif untuk mengasah pengetahuan kimia kamu.

    🔹 *Kuis Tabel Periodik*: Uji kemampuanmu mengenali simbol, nomor atom, dan nama unsur.

    🔹 *Kuis Senyawa Organik*: Pelajari dan uji pemahamanmu tentang senyawa karbon, gugus fungsi, dan rumus kimia.

    Pilih salah satu kuis dari sidebar dan mulai belajar sambil bermain! 🎓✨
    """)

# ===== GAME 1: Kuis Tabel Periodik =====
elif selected_game == "Kuis Tabel Periodik":
    st.title("🔢 Kuis Tabel Periodik")

    elements = [
        {"nama": "Hidrogen", "simbol": "H", "nomor": 1},
        {"nama": "Helium", "simbol": "He", "nomor": 2},
        {"nama": "Litium", "simbol": "Li", "nomor": 3},
        {"nama": "Berilium", "simbol": "Be", "nomor": 4},
        {"nama": "Bor", "simbol": "B", "nomor": 5},
        {"nama": "Karbon", "simbol": "C", "nomor": 6},
        {"nama": "Nitrogen", "simbol": "N", "nomor": 7},
        {"nama": "Oksigen", "simbol": "O", "nomor": 8},
        {"nama": "Fluorin", "simbol": "F", "nomor": 9},
        {"nama": "Neon", "simbol": "Ne", "nomor": 10},
    ]

    if "elemen_score" not in st.session_state:
        st.session_state.elemen_score = 0
        st.session_state.elemen_index = 0
        st.session_state.elemen_feedback = ""
        st.session_state.elemen_answered = False
        st.session_state.elemen_questions = random.sample(elements, 5)

    if st.session_state.elemen_index < len(st.session_state.elemen_questions):
        q = st.session_state.elemen_questions[st.session_state.elemen_index]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.elemen_index+1} dari 5")
        ans = st.text_input(f"🌡️ Apa simbol dari unsur **{q['nama']}**?", key=f"elemen_q{st.session_state.elemen_index}")

        if st.button("Kirim Jawaban", key=f"elemen_submit{st.session_state.elemen_index}") and not st.session_state.elemen_answered:
            if ans.strip().lower() == q["simbol"].lower():
                st.session_state.elemen_score += 1
                st.session_state.elemen_feedback = "✅ Jawaban Benar!"
                st.balloons()
            else:
                st.session_state.elemen_feedback = f"❌ Salah. Jawaban benar: {q['simbol']}"
            st.session_state.elemen_answered = True

        st.write(st.session_state.elemen_feedback)

        if st.session_state.elemen_answered:
            if st.button("➡ Soal Berikutnya", key=f"elemen_next{st.session_state.elemen_index}"):
                st.session_state.elemen_index += 1
                st.session_state.elemen_feedback = ""
                st.session_state.elemen_answered = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>🌟 Skor: {st.session_state.elemen_score}/5</div>", unsafe_allow_html=True)
    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.elemen_score}/5")
        if st.button("🔁 Ulangi Kuis"):
            for k in ["elemen_score", "elemen_index", "elemen_feedback", "elemen_answered", "elemen_questions"]:
                del st.session_state[k]

# ===== GAME 2: Kuis Senyawa Organik =====
elif selected_game == "Kuis Senyawa Organik":
    st.title("🧪 Kuis Senyawa Organik")

    if "org_started" not in st.session_state:
        st.session_state.org_started = False

    if not st.session_state.org_started:
        st.markdown("""
        ### 📚 Pengantar Senyawa Organik

        **I. Hidrokarbon**  
        *Definisi*: Senyawa organik yang hanya mengandung atom karbon (C) dan hidrogen (H).  
        **Contoh:**  
        1. **Metana (CH₄)**  
        2. **Benzena (C₆H₆)**  

        **II. Gugus Fungsi dan Golongan Senyawa Organik**  
        Gugus fungsi menentukan sifat kimia dan reaktivitas.

        - **Alkohol**: -OH, contoh: Etanol (C₂H₅OH)  
        - **Asam Karboksilat**: -COOH, contoh: Asam Asetat (CH₃COOH)  
        - **Keton**: >C=O, contoh: Aseton (CH₃COCH₃)  
        - **Amina**: -NH₂, contoh: Metilamina (CH₃NH₂)  
        - **Ester**: -COOR', contoh: Metil asetat (CH₃COOCH₃)
        """, unsafe_allow_html=True)

        if st.button("🚀 Mulai Kuis"):
            st.session_state.org_started = True
        st.stop()

    organic_questions = [
        {"q":"Apa rumus molekul dari metana?","a":"CH4"},
        {"q":"Apa gugus fungsi dari alkohol?","a":"OH"},
        {"q":"Apa nama senyawa CH3COOH?","a":"Asam asetat"},
        {"q":"Apa nama senyawa dengan rumus C2H5OH?","a":"Etanol"},
        {"q":"Apa nama senyawa C6H6?","a":"Benzena"},
        {"q":"Apa nama senyawa CH3CH2COOH?","a":"Asam propionat"},
        {"q":"Apa nama senyawa dengan rumus C3H7OH?","a":"Propanol"},
        {"q":"Apa nama senyawa yang memiliki rumus C6H12O6?","a":"Glukosa"},
        {"q":"Apa nama senyawa C4H9OH?","a":"Butanol"},
        {"q":"Apa nama senyawa CH3NH2?","a":"Metilamina"},
        {"q":"Apa nama senyawa dengan rumus C5H10O?","a":"Pentanol"},
        {"q":"Apa nama senyawa CH3CH2COCH3?","a":"Aseton"},
        {"q":"Apa nama senyawa dengan rumus C7H8?","a":"Toluena"},
        {"q":"Apa nama senyawa C8H10?","a":"Etilbenzen"},
        {"q":"Apa nama senyawa C10H12O2?","a":"Asam benzoat metil ester"},
        {"q":"Apa nama senyawa dengan rumus C3H6O?","a":"Asetaldehida"},
        {"q":"Apa nama senyawa C4H8O2?","a":"Asam butirat"},
        {"q":"Apa nama senyawa CH3COOCH3?","a":"Metil asetat"},
        {"q":"Apa nama senyawa dengan rumus C2H4O2?","a":"Asam asetat"},
        {"q":"Apa nama senyawa C9H12O?","a":"Fenilpropanol"}
    ]

    if "org_score" not in st.session_state:
        st.session_state.org_score = 0
        st.session_state.org_index = 0
        st.session_state.org_feedback = ""
        st.session_state.org_answered = False
        st.session_state.org_questions = random.sample(organic_questions, 5)

    if st.session_state.org_index < len(st.session_state.org_questions):
        q = st.session_state.org_questions[st.session_state.org_index]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.org_index+1} dari 5")
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
            if st.button("➡ Soal Berikutnya", key=f"org_next_{st.session_state.org_index}"):
                st.session_state.org_index += 1
                st.session_state.org_feedback = ""
                st.session_state.org_answered = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>🌟 Skor: {st.session_state.org_score}/5</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.org_score}/5")
        if st.button("🔁 Ulangi Kuis"):
            for k in ["org_score", "org_index", "org_feedback", "org_answered", "org_questions", "org_started"]:
                del st.session_state[k]
