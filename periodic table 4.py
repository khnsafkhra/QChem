# === GAME 2: Kuis Senyawa Organik (10 soal) ===
elif selected_game == "Kuis Senyawa Organik":
    st.title("🧪 Kuis Senyawa Organik")

    organic_questions = [
        {"q": "Apa rumus molekul dari metana?", "a": "CH4"},
        {"q": "Apa gugus fungsi dari alkohol?", "a": "OH"},
        {"q": "Apa nama senyawa CH3COOH?", "a": "Asam asetat"},
        {"q": "Apa nama senyawa dengan rumus C2H5OH?", "a": "Etanol"},
        {"q": "Apa nama senyawa C6H6?", "a": "Benzena"},
        {"q": "Apa nama senyawa dengan rumus HCOOH?", "a": "Asam format"},
        {"q": "Apa rumus dari aseton?", "a": "C3H6O"},
        {"q": "Apa gugus fungsi dari aldehida?", "a": "CHO"},
        {"q": "Apa nama senyawa CH3NH2?", "a": "Metilamina"},
        {"q": "Apa rumus molekul dari etena?", "a": "C2H4"},
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
            if st.button("➡️ Soal Berikutnya", key=f"org_next_{st.session_state.org_index}"):
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
