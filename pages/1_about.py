import base64
from pathlib import Path

import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ผู้พัฒนา | Recommend_car",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GOOGLE FONTS
    ===================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;700;800&display=swap'
    );


    /* =====================================================
       GLOBAL
    ===================================================== */

    .stApp {
        background-color: #080808;

        background-image:
            radial-gradient(
                circle at 15% 50%,
                rgba(220, 38, 38, 0.18) 0%,
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 30%,
                rgba(153, 27, 27, 0.18) 0%,
                transparent 28%
            ),
            radial-gradient(
                circle at 50% 80%,
                rgba(239, 68, 68, 0.08) 0%,
                transparent 30%
            );

        background-attachment: fixed;
    }


    html,
    body,
    [class*="css"] {
        font-family: "Prompt", "Inter", sans-serif;
        color: #f5f5f5;
    }


    /* =====================================================
       REMOVE STREAMLIT DEFAULT UI
    ===================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* =====================================================
       HERO
    ===================================================== */

    .hero {
        text-align: center;
        padding: 50px 20px 20px;
    }

    .hero h1 {
        margin: 0 0 8px;

        font-family: "Inter", "Prompt", sans-serif;

        font-size: 3rem;
        font-weight: 800;

        background: linear-gradient(
            135deg,
            #ffffff 0%,
            #ef4444 50%,
            #991b1b 100%
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        background-clip: text;

        letter-spacing: -0.5px;
    }

    .hero p {
        margin: 0;

        color: #a3a3a3;

        font-size: 1.1rem;
        font-weight: 300;

        letter-spacing: 0.5px;
    }


    /* =====================================================
       PROFILE PHOTO
    ===================================================== */

    .profile-photo-wrap {
        display: flex;
        justify-content: center;
        align-items: center;

        margin-top: 20px;
    }

    .profile-photo {
        width: 200px;
        height: 200px;

        object-fit: cover;

        border-radius: 50%;

        border: 3px solid #dc2626;

        background: #181818;

        box-shadow:
            0 0 35px rgba(220, 38, 38, 0.35);

        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
    }

    .profile-photo:hover {
        transform: scale(1.04);

        box-shadow:
            0 0 55px rgba(220, 38, 38, 0.55);
    }


    /* =====================================================
       PROFILE FALLBACK
    ===================================================== */

    .profile-fallback {
        width: 200px;
        height: 200px;

        display: flex;
        justify-content: center;
        align-items: center;

        border-radius: 50%;

        background: #181818;

        border: 3px solid #dc2626;

        font-size: 4rem;

        box-shadow:
            0 0 35px rgba(220, 38, 38, 0.35);
    }


    /* =====================================================
       PROFILE CARD
    ===================================================== */

    .profile-card {
        width: 100%;
        max-width: 450px;

        margin: 30px auto 0;

        padding: 32px 36px;

        box-sizing: border-box;

        text-align: center;

        background: rgba(24, 24, 24, 0.78);

        border: 1px solid rgba(239, 68, 68, 0.18);

        border-radius: 20px;

        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);

        box-shadow:
            0 10px 30px -5px rgba(0, 0, 0, 0.45);

        transition:
            border-color 0.3s ease,
            box-shadow 0.3s ease;
    }

    .profile-card:hover {
        border-color: rgba(239, 68, 68, 0.45);

        box-shadow:
            0 15px 40px -5px rgba(220, 38, 38, 0.18);
    }

    .profile-card h2 {
        margin: 0 0 20px;

        color: #f5f5f5;

        font-family: "Prompt", sans-serif;

        font-size: 1.5rem;
        font-weight: 700;
    }


    /* =====================================================
       INFORMATION ROW
    ===================================================== */

    .info-row {
        display: flex;

        justify-content: space-between;
        align-items: center;

        padding: 14px 4px;

        border-top: 1px solid rgba(239, 68, 68, 0.15);

        font-size: 1rem;
    }

    .info-row:first-of-type {
        border-top: none;
    }

    .info-row .label {
        color: #a3a3a3;

        font-weight: 400;
    }

    .info-row .value {
        color: #ef4444;

        font-weight: 600;

        letter-spacing: 0.5px;
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    [data-testid="stSidebar"] {
        background: #0d0d0d !important;

        border-right:
            1px solid rgba(239, 68, 68, 0.15) !important;
    }

    [data-testid="stSidebarNav"] {
        padding-top: 20px;
    }

    [data-testid="stSidebarNav"]::before {
        content: "RECOMMEND_CAR";

        display: block;

        margin: 0 20px 20px;
        padding-bottom: 16px;

        border-bottom:
            1px solid rgba(239, 68, 68, 0.15);

        color: #737373;

        font-family: "Inter", sans-serif;

        font-size: 0.75rem;
        font-weight: 700;

        letter-spacing: 2px;
    }

    [data-testid="stSidebarNav"] a {
        margin: 4px 12px !important;

        padding: 12px 16px !important;

        border-radius: 10px;

        color: #a3a3a3 !important;

        font-family: "Prompt", sans-serif;

        font-size: 0.95rem;
        font-weight: 500;

        background: transparent !important;

        transition:
            background 0.2s ease,
            color 0.2s ease;
    }

    [data-testid="stSidebarNav"] a:hover {
        background:
            rgba(220, 38, 38, 0.12) !important;

        color: #fca5a5 !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background:
            linear-gradient(
                90deg,
                rgba(220, 38, 38, 0.20),
                transparent
            ) !important;

        color: #ef4444 !important;

        border-left:
            3px solid #dc2626;

        font-weight: 600;
    }


    /* =====================================================
       SIDEBAR MENU TEXT
    ===================================================== */

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


    /* =====================================================
       FOOTER
    ===================================================== */

    .custom-footer {
        margin-top: 50px;
        padding: 30px 20px;

        text-align: center;

        color: #666666;

        font-size: 0.85rem;

        border-top:
            1px solid rgba(239, 68, 68, 0.12);
    }


    /* =====================================================
       MOBILE
    ===================================================== */

    @media (max-width: 600px) {

        .hero {
            padding-top: 30px;
        }

        .hero h1 {
            font-size: 2.3rem;
        }

        .hero p {
            font-size: 0.95rem;
        }

        .profile-photo,
        .profile-fallback {
            width: 160px;
            height: 160px;
        }

        .profile-card {
            padding: 25px 22px;
        }

        .profile-card h2 {
            font-size: 1.25rem;
        }

        .info-row {
            font-size: 0.9rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">
        <h1>ผู้พัฒนา</h1>
        <p>ข้อมูลผู้จัดทำโปรเจค Recommend_car</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PROFILE IMAGE
# =========================================================

photo_path = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "024.jpg"
)


if photo_path.exists():

    photo_b64 = base64.b64encode(
        photo_path.read_bytes()
    ).decode("utf-8")

    st.markdown(
        f"""
        <div class="profile-photo-wrap">
            <img
                class="profile-photo"
                src="data:image/jpeg;base64,{photo_b64}"
                alt="รูปผู้พัฒนา"
            >
        </div>
        """,
        unsafe_allow_html=True,
    )

else:

    st.markdown(
        """
        <div class="profile-photo-wrap">
            <div class="profile-fallback">
                🧑‍💻
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# PROFILE INFORMATION
# =========================================================

st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="custom-footer">
        Made with ❤️ using Streamlit · Recommend_car Project 2026
    </div>
    """,
    unsafe_allow_html=True,
)
