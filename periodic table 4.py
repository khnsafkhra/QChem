if selected_game == "Kuis Tabel Periodik":
    if "pt_started" not in st.session_state:
        st.session_state.pt_started = False

    if not st.session_state.pt_started:
        st.title("🧪 Kuis Tabel Periodik Unsur")
        st.image("https://i.imgur.com/Kcgjoc5.png", caption="Tabel Periodik Unsur", use_container_width=True)
        if st.button("Mulai Kuis"):
            st.session_state.pt_started = True
        st.stop()

    NUM_PT = 5
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
        {"name":"kalium","symbol":"K","number":1,"group":1,"period":4},
        {"name":"mangan","symbol":"Mn","number":25,"group":7,"period":4},
        {"name":"besi","symbol":"Fe","number":26,"group":8,"period":4},
        {"name":"tembaga","symbol":"Cu","number":29,"group":11,"period":4},
        {"name":"zinc","symbol":"Zn","number":30,"group":12,"period":4},
        {"name":"fluorin","symbol":"F","number":9,"group":17,"period":2},
        {"name":"neon","symbol":"Ne","number":10,"group":18,"period":2},
        {"name":"silikon","symbol":"Si","number":14,"group":14,"period":3},
        {"name":"nikel","symbol":"Ni","number":28,"group":10,"period":4},
    ]

    # Tambahkan mapping golongan ke label A/B
    group_labels = {
        1: "1A", 2: "2A", 13: "3A", 14: "4A", 15: "5A", 16: "6A", 17: "7A", 18: "8A",
        3: "3B", 4: "4B", 5: "5B", 6: "6B", 7: "7B", 8: "8B", 9: "8B", 10: "8B", 11: "1B", 12: "2B"
    }

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

        if q["type"] == "symbol":
            text = f"🧪 Apa simbol dari unsur {e['name'].capitalize()}?"
            ans = e["symbol"]
        elif q["type"] == "number":
            text = f"🔢 Berapa nomor atom dari {e['name'].capitalize()}?"
            ans = str(e["number"])
        elif q["type"] == "group":
            text = f"📚 Golongan berapa unsur {e['name'].capitalize()}?"
            ans = str(e["group"])
            st.caption("💡 Jawaban bisa berupa angka (mis. 1) atau format lama (mis. 1A)")
        else:
            text = f"🕏 Periode berapa unsur {e['name'].capitalize()}?"
            ans = str(e["period"])

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.pt_index+1} dari {NUM_PT}")
        user = st.text_input(text, key=f"pt_in_{st.session_state.pt_index}")

        if st.button("Kirim Jawaban", key=f"pt_sub_{st.session_state.pt_index}") and not st.session_state.pt_answered:
            user_ans = user.strip().lower()
            correct = ans.lower()
            alt_label = group_labels.get(e["group"], "").lower()
            if user_ans == correct or (q["type"] == "group" and user_ans == alt_label):
                st.session_state.pt_score += 1
                st.session_state.pt_feedback = "✅ Jawaban Benar!"
                st.balloons()
            else:
                correct_display = f"{correct} / {alt_label.upper()}" if q["type"] == "group" and alt_label else correct
                st.session_state.pt_feedback = f"❌ Salah. Jawaban benar: {correct_display}"
            st.session_state.pt_answered = True

        st.write(st.session_state.pt_feedback)

        if st.session_state.pt_answered:
            if st.button("➡ Soal Berikutnya", key=f"pt_next_{st.session_state.pt_index}"):
                st.session_state.pt_index += 1
                st.session_state.pt_q = None
                st.session_state.pt_feedback = ""
                st.session_state.pt_answered = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>🌟 Skor: {st.session_state.pt_score}/{NUM_PT}</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.pt_score}/{NUM_PT}")
        if st.button("🔁 Ulangi Kuis"):
            for k in ["pt_score", "pt_index", "pt_q", "pt_feedback", "pt_answered", "pt_started"]:
                del st.session_state[k]
