
import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | Recommend_car",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;800&display=swap');

/* =========================
   MAIN APP
========================= */

.stApp {
    background-color: #080808;
    background-image:
        radial-gradient(circle at 15% 50%, rgba(220, 38, 38, 0.18) 0%, transparent 28%),
        radial-gradient(circle at 85% 30%, rgba(153, 27, 27, 0.18) 0%, transparent 28%),
        radial-gradient(circle at 50% 80%, rgba(239, 68, 68, 0.08) 0%, transparent 30%);
    background-attachment: fixed;
}

html, body, [class*="css"] {
    font-family: 'Prompt', 'Inter', sans-serif;
    color: #F5F5F5;
}


/* =========================
   HERO
========================= */

.hero {
    text-align: center;
    padding: 50px 20px 20px 20px;
}

.hero h1 {
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 3rem;
    font-weight: 800;

    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #EF4444 50%,
        #991B1B 100%
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 8px;
    letter-spacing: -0.5px;
}

.hero p {
    color: #A3A3A3;
    font-size: 1.1rem;
    letter-spacing: 0.5px;
    margin-top: 0;
    font-weight: 300;
}


/* =========================
   PROFILE PHOTO
========================= */

.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.profile-photo-wrap img {
    width: 200px;
    height: 200px;

    border-radius: 50%;

    border: 3px solid transparent;

    background:
        linear-gradient(#181818, #181818) padding-box,
        linear-gradient(
            135deg,
            #EF4444,
            #DC2626,
            #7F1D1D
        ) border-box;

    box-shadow:
        0 0 35px rgba(220, 38, 38, 0.35);

    object-fit: cover;

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;
}

.profile-photo-wrap img:hover {
    transform: scale(1.04);

    box-shadow:
        0 0 55px rgba(220, 38, 38, 0.55);
}


/* =========================
   PROFILE CARD
========================= */

.profile-card {
    max-width: 450px;

    margin: 30px auto 0 auto;

    background: rgba(24, 24, 24, 0.78);

    border: 1px solid rgba(239, 68, 68, 0.18);

    border-radius: 20px;

    padding: 32px 36px;

    text-align: center;

    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);

    box-shadow:
        0 10px 30px -5px rgba(0, 0, 0, 0.45);

    transition: all 0.3s ease;
}

.profile-card:hover {
    border-color: rgba(239, 68, 68, 0.45);

    box-shadow:
        0 15px 40px -5px rgba(220, 38, 38, 0.18);
}

.profile-card h2 {
    color: #F5F5F5;

    font-family: 'Inter', 'Prompt', sans-serif;

    font-size: 1.5rem;

    font-weight: 700;

    margin: 0 0 20px 0;
}


/* =========================
   INFORMATION ROW
========================= */

.info-row {
    display: flex;

    justify-content: space-between;

    align-items: center;

    padding: 14px 4px;

    border-top: 1px solid rgba(239, 68, 68, 0.15);

    color: #E5E5E5;

    font-size: 1rem;
}

.info-row:first-of-type {
    border-top: none;
}

.info-row span.label {
    color: #A3A3A3;
    font-weight: 400;
}

.info-row span.value {
    font-weight: 600;

    color: #EF4444;

    letter-spacing: 0.5px;
}


/* =========================
   SIDEBAR
========================= */

footer,
#MainMenu {
    visibility: hidden;
}

[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"] {
    visibility: visible !important;
}

[data-testid="stSidebar"] {
    background: #0D0D0D !important;

    border-right:
        1px solid rgba(239, 68, 68, 0.15) !important;
}

[data-testid="stSidebarNav"] {
    padding-top: 20px;
}

[data-testid="stSidebarNav"]::before {
    content: "RECOMMEND_CAR";

    display: block;

    margin: 0 20px 20px 20px;

    padding-bottom: 16px;

    border-bottom:
        1px solid rgba(239, 68, 68, 0.15);

    font-family: 'Inter', sans-serif;

    font-size: 0.75rem;

    font-weight: 700;

    letter-spacing: 2px;

    color: #737373;
}

[data-testid="stSidebarNav"] a {
    margin: 4px 12px !important;

    padding: 12px 16px !important;

    border-radius: 10px;

    color: #A3A3A3 !important;

    font-family: 'Prompt', sans-serif;

    font-weight: 500;

    font-size: 0.95rem;

    transition: all 0.2s ease;

    background: transparent !important;
}

[data-testid="stSidebarNav"] a:hover {
    background:
        rgba(220, 38, 38, 0.12) !important;

    color: #FCA5A5 !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background:
        linear-gradient(
            90deg,
            rgba(220, 38, 38, 0.20) 0%,
            transparent 100%
        ) !important;

    color: #EF4444 !important;

    border-left:
        3px solid #DC2626;

    font-weight: 600;
}


/* =========================
   SIDEBAR MENU TEXT
========================= */

[data-testid="stSidebarNav"] li:nth-child(1) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] li:nth-child(1) a::after {
    content: "🏠 หน้าหลัก";
    font-size: 0.95rem !important;
}

[data-testid="stSidebarNav"] li:nth-child(2) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] li:nth-child(2) a::after {
    content: "🧑‍💻 ผู้พัฒนา";
    font-size: 0.95rem !important;
}


/* =========================
   FOOTER
========================= */

.custom-footer {
    text-align: center;

    color: #666666;

    margin-top: 50px;

    padding: 30px 20px;

    font-size: 0.85rem;

    border-top:
        1px solid rgba(239, 68, 68, 0.12);
}

</style>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================

st.markdown("""
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>ข้อมูลผู้จัดทำโปรเจค Recommend_car</p>
</div>
""", unsafe_allow_html=True)


# =========================
# PROFILE IMAGE
# =========================

photo_path = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "024.jpg"
)

try:
    photo_b64 = base64.b64encode(
        photo_path.read_bytes()
    ).decode()

    st.markdown(
        f'''
        <div class="profile-photo-wrap">
            <img
                src="data:image/jpeg;base64,{photo_b64}"
                alt="Profile Photo"
            >
        </div>
        ''',
        unsafe_allow_html=True,
    )

except FileNotFoundError:

    st.markdown(
        '''
        <div class="profile-photo-wrap">

            <div style="
                width:200px;
                height:200px;
                border-radius:50%;
                background:#181818;
                border:3px solid #DC2626;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:4rem;
                box-shadow:0 0 35px rgba(220,38,38,0.35);
            ">
                🧑‍💻
            </div>

        </div>
        ''',
        unsafe_allow_html=True,
    )


# =========================
# PROFILE INFORMATION
# =========================

st.markdown("""
<div class="profile-card">

    <h2>จตุรภัทร สถาปิตานนท์</h2>

    <div class="info-row">
        <span class="label">
            รหัสนักศึกษา
        </span>

        <span class="value">
            664245024
        </span>
    </div>

    <div class="info-row">
        <span class="label">
            หมู่เรียน
        </span>

        <span class="value">
            Sec. 66/43
        </span>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="custom-footer">
    Made with ❤️ using Streamlit · Recommend_car Projects 2026
</div>
""", unsafe_allow_html=True)
