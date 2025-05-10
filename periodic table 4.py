import streamlit as st
import random

# --- Sidebar untuk memilih game ---
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["-- Pilih Game --", "Kuis Tabel Periodik", "Kuis Senyawa Organik"])

# --- Styling umum font ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# --- Styling background berdasarkan halaman ---
if selected_game == "-- Pilih Game --":
    # Tampilan Selamat Datang dengan dark background
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
                    url("https://i.imgur.com/06z4doi.jpeg") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    # Styling dark theme untuk halaman game dengan gradasi warna
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #1a1a2e, #16213e, #0f3460);
        background-attachment: fixed;
        color: white;
        backdrop-filter: blur(10px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Styling komponen lainnya (selalu aktif) ---
st.markdown("""
    <style>
    .question-card {
        background: rgba(0, 0, 0, 0.8); /* Background lebih gelap agar lebih kontras */
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 4px 4px 30px rgba(0,0,0,0.6);
        margin-bottom: 25px;
        animation: fadeIn 1s ease-in-out;
        color: #fff;
    }
    .score-box {
        background: rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        color: white;
        margin-top: 10px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 24px;
        border-radius: 10px;
        border: none;
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

# --- Halaman Selamat Datang ---
if selected_game == "-- Pilih Game --":
    st.title("🎉 Selamat datang di QChems")
    st.markdown("""
    <div style='padding: 20px; background-color: rgba(255,255,255,0.1); border-radius: 15px;'>
        <h2 style='color: white;'>Aplikasi kuis interaktif seputar Tabel Periodik & Senyawa Organik.</h2>
        <p style='color: white;'>Silakan pilih game dari menu di sebelah kiri untuk memulai.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# --- Game Logic seperti sebelumnya ---
# Misalnya kamu sudah punya kode untuk 'Kuis Tabel Periodik' dan 'Kuis Senyawa Organik'...
