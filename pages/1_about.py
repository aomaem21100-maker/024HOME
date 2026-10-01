import base64
from pathlib import Path
 
import streamlit as st
 
st.set_page_config(
    page_title="ผู้พัฒนา | Recommend_car",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Prompt:wght@300;400;500;600;700&display=swap');
 
:root {
    --nf-red: #E50914;
    --nf-red-dark: #B20710;
    --nf-bg: #141414;
    --nf-text: #FFFFFF;
    --nf-muted: #B3B3B3;
}
 
.stApp { background: var(--nf-bg); }
 
html, body, [class*="css"] {
    font-family: 'Prompt', sans-serif;
    color: var(--nf-text);
}
 
header[data-testid="stHeader"], footer, #MainMenu { display: none !important; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { display: none !important; }
 
.block-container {
    padding: 0 0 40px 0 !important;
    max-width: 100% !important;
}
 
/* ---------- Navbar ---------- */
.nav {
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    gap: 28px;
    padding: 16px 4%;
    background: linear-gradient(180deg, rgba(0,0,0,.85) 0%, rgba(20,20,20,0) 100%);
}
.logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.1rem;
    letter-spacing: 2px;
    color: var(--nf-red);
    line-height: 1;
}
.nav a {
    color: #E5E5E5;
    text-decoration: none !important;
    font-size: .9rem;
}
.nav a:hover { color: var(--nf-muted); }
.nav a.active { color: #FFFFFF; font-weight: 600; }
 
/* ---------- Hero ---------- */
.hero {
    position: relative;
    padding: 70px 4% 50px 4%;
    text-align: center;
    background:
        linear-gradient(0deg, var(--nf-bg) 0%, rgba(20,20,20,0) 35%),
        radial-gradient(circle at 50% 30%, rgba(229,9,20,.45) 0%, rgba(229,9,20,0) 55%),
        linear-gradient(135deg, #2a0306 0%, #0b0b0b 70%);
    overflow: hidden;
}
.hero .tag {
    color: var(--nf-red);
    font-weight: 700;
    letter-spacing: 3px;
    font-size: .85rem;
    margin-bottom: 10px;
}
.hero h1 {
    font-family: 'Bebas Neue', 'Prompt', sans-serif;
    font-size: clamp(3rem, 8vw, 5.5rem);
    font-weight: 400;
    line-height: 1;
    margin: 0 0 12px 0;
    letter-spacing: 2px;
    text-shadow: 2px 4px 12px rgba(0,0,0,.6);
}
.hero p {
    font-size: 1.05rem;
    color: #E5E5E5;
    margin: 0;
    text-shadow: 1px 2px 6px rgba(0,0,0,.7);
}
 
/* ---------- Profile (สไตล์ Who's watching) ---------- */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: -10px;
}
.profile-photo-wrap img,
.profile-photo-wrap .ph {
    width: 200px;
    height: 200px;
    border-radius: 8px;
    border: 3px solid transparent;
    object-fit: cover;
    box-shadow: 0 8px 24px rgba(0,0,0,.7);
    transition: border-color .2s ease, transform .3s ease;
}
.profile-photo-wrap img:hover {
    border-color: #FFFFFF;
    transform: scale(1.05);
}
.profile-photo-wrap .ph {
    background: #333333;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4.5rem;
}
 
/* ---------- Profile Card ---------- */
.profile-card {
    max-width: 460px;
    margin: 28px auto 0 auto;
    background: #181818;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,.6);
    border-top: 3px solid var(--nf-red);
}
.profile-card h2 {
    margin: 0;
    padding: 24px 28px 8px 28px;
    font-size: 1.5rem;
    font-weight: 600;
    text-align: center;
    color: #FFFFFF;
}
.profile-card .role {
    text-align: center;
    color: var(--nf-muted);
    font-size: .85rem;
    padding-bottom: 14px;
}
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 28px;
    border-top: 1px solid #2a2a2a;
    font-size: 1rem;
}
.info-row .label { color: var(--nf-muted); }
.info-row .value { font-weight: 600; color: #FFFFFF; letter-spacing: .5px; }
.info-row .value.red { color: var(--nf-red); }
 
/* ---------- Button ---------- */
.btn-wrap { text-align: center; margin-top: 28px; }
.nbtn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 28px;
    border-radius: 4px;
    font-size: 1.05rem;
    font-weight: 600;
    text-decoration: none !important;
    background: #FFFFFF;
    color: #000000 !important;
    transition: all .2s ease;
}
.nbtn:hover { background: rgba(255,255,255,.75); }
 
.nf-footer {
    margin: 60px 4% 0 4%;
    padding-top: 24px;
    border-top: 1px solid #333333;
    color: #757575;
    font-size: .85rem;
    text-align: center;
}
</style>
"""
 
nav = """
<div class="nav">
<div class="logo">RECOMMEND_CAR</div>
<a href="/" target="_self">หน้าแรก</a>
<a href="/#systems" target="_self">ระบบทั้งหมด</a>
<a href="/about" target="_self" class="active">ผู้พัฒนา</a>
</div>
<div class="hero">
<div class="tag">DEVELOPER</div>
<h1>ผู้พัฒนา</h1>
<p>ข้อมูลผู้จัดทำโปรเจค Recommend_car</p>
</div>
"""
 
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(nav, unsafe_allow_html=True)
 
# โหลดรูปภาพ
photo_path = Path(__file__).resolve().parent.parent / "assets" / "024.jpg"
try:
    photo_b64 = base64.b64encode(photo_path.read_bytes()).decode()
    st.markdown(
        f'<div class="profile-photo-wrap"><img src="data:image/jpeg;base64,{photo_b64}" alt="Profile Photo"></div>',
        unsafe_allow_html=True,
    )
except FileNotFoundError:
    st.markdown(
        '<div class="profile-photo-wrap"><div class="ph">🧑‍💻</div></div>',
        unsafe_allow_html=True,
    )
 
card = """
<div class="profile-card">
<h2>จตุรภัทร สถาปิตานนท์</h2>
<div class="role">นักพัฒนาโปรเจค Recommend_car</div>
<div class="info-row"><span class="label">รหัสนักศึกษา</span><span class="value red">664245024</span></div>
<div class="info-row"><span class="label">หมู่เรียน</span><span class="value">Sec. 66/43</span></div>
</div>
<div class="btn-wrap"><a class="nbtn" href="/" target="_self">← กลับหน้าหลัก</a></div>
"""
st.markdown(card, unsafe_allow_html=True)
 
st.markdown(
    '<div class="nf-footer">Made with ❤️ using Streamlit · Recommend_car 2026</div>',
    unsafe_allow_html=True,
)
