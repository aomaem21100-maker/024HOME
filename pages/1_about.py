import base64
from pathlib import Path
 
import streamlit as st
 
st.set_page_config(
    page_title="ผู้พัฒนา | ML Hub",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;800&display=swap');
 
/* Main App Layout - Modern Dark Red Theme */
.stApp {
    background-color: #0A0505;
    background-image: 
        radial-gradient(circle at 15% 50%, rgba(225, 29, 72, 0.15) 0%, transparent 30%),
        radial-gradient(circle at 85% 30%, rgba(153, 27, 27, 0.2) 0%, transparent 30%),
        radial-gradient(circle at 50% 80%, rgba(239, 68, 68, 0.1) 0%, transparent 35%);
    background-attachment: fixed;
}
 
html, body, [class*="css"] { 
    font-family: 'Prompt', 'Inter', sans-serif; 
    color: #F3F4F6;
}
 
/* Back link */
.back-link {
    display: inline-block;
    margin: 20px 0 0 4%;
    color: #F87171 !important;
    text-decoration: none !important;
    font-weight: 500;
}
.back-link:hover { color: #FECDD3 !important; }
 
/* Hero Section */
.hero { 
    text-align: center; 
    padding: 30px 20px 20px 20px; 
}
.hero h1 {
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #F87171 0%, #EF4444 50%, #DC2626 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}
.hero p { 
    color: #9CA3AF; 
    font-size: 1.1rem; 
    letter-spacing: 0.5px; 
    margin-top: 0; 
    font-weight: 300;
}
 
/* Profile Photo Wrapper */
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
        linear-gradient(#180C0C, #180C0C) padding-box,
        linear-gradient(135deg, #F87171, #EF4444, #991B1B) border-box;
    box-shadow: 0 0 40px rgba(225, 29, 72, 0.35);
    object-fit: cover;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.profile-photo-wrap img:hover {
    transform: scale(1.03);
    box-shadow: 0 0 50px rgba(225, 29, 72, 0.6);
}
 
/* Profile Card */
.profile-card {
    max-width: 450px;
    margin: 30px auto 0 auto;
    background: rgba(24, 12, 12, 0.7);
    border: 1px solid rgba(239, 68, 68, 0.2);
    border-radius: 20px;
    padding: 32px 36px;
    text-align: center;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.6);
}
.profile-card h2 {
    color: #FFFFFF;
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 0 20px 0;
}
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 4px;
    border-top: 1px solid rgba(239, 68, 68, 0.15);
    color: #F3F4F6;
    font-size: 1rem;
}
.info-row:first-of-type { border-top: none; }
.info-row span.label { color: #9CA3AF; font-weight: 400; }
.info-row span.value { font-weight: 600; color: #F87171; letter-spacing: 0.5px; }
 
/* Hide default Streamlit elements */
footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }
 
/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: #0F0707 !important;
    border-right: 1px solid rgba(239, 68, 68, 0.15) !important;
}
[data-testid="stSidebarNav"] {
    padding-top: 20px;
}
[data-testid="stSidebarNav"]::before {
    content: "ML HUB NAVIGATION";
    display: block;
    margin: 0 20px 20px 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(239, 68, 68, 0.15);
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: #78716C;
}
[data-testid="stSidebarNav"] a {
    margin: 4px 12px !important;
    padding: 12px 16px !important;
    border-radius: 10px;
    color: #9CA3AF !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    background: transparent !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(225, 29, 72, 0.15) !important;
    color: #FECDD3 !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(225, 29, 72, 0.25) 0%, transparent 100%) !important;
    color: #F87171 !important;
    border-left: 3px solid #EF4444;
    font-weight: 600;
}
 
/* เปลี่ยนข้อความเมนู: app -> หน้าหลัก, about -> ผู้พัฒนา */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "🏠 หน้าหลัก"; font-size: 0.95rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "🧑‍💻 ผู้พัฒนา"; font-size: 0.95rem !important; }
 
/* Footer */
.custom-footer {
    text-align: center;
    color: #78716C;
    margin-top: 50px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(239, 68, 68, 0.15);
}
</style>
""", unsafe_allow_html=True)
 
st.markdown(
    '<a class="back-link" href="/" target="_self">← กลับหน้าหลัก</a>',
    unsafe_allow_html=True,
)
 
st.markdown("""
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>ข้อมูลผู้จัดทำโปรเจค Recommend_car</p>
</div>
""", unsafe_allow_html=True)
 
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
        '<div class="profile-photo-wrap"><div style="width:200px;height:200px;border-radius:50%;background:#180C0C;border:3px solid #EF4444;display:flex;align-items:center;justify-content:center;font-size:4rem;">🧑‍💻</div></div>',
        unsafe_allow_html=True,
    )
 
st.markdown("""
<div class="profile-card">
    <h2>จตุรภัทร สถาปิตานนท์</h2>
    <div class="info-row">
        <span class="label">รหัสนักศึกษา</span>
        <span class="value">664245024</span>
    </div>
    <div class="info-row">
        <span class="label">หมู่เรียน</span>
        <span class="value">Sec. 66/43</span>
    </div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="custom-footer">
    Made with ❤️️ using Streamlit · Recommend_car Projects 2026
</div>
""", unsafe_allow_html=True)
