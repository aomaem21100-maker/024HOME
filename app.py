```python
import streamlit as st

st.set_page_config(
    page_title="Recommend_car",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;800&display=swap');

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

.hero {
    text-align: center;
    padding: 50px 20px 30px 20px;
}

.hero h1 {
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 3.3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 0%, #EF4444 50%, #991B1B 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
    letter-spacing: -1px;
    line-height: 1.2;
}

.hero p {
    color: #A3A3A3;
    font-size: 1.15rem;
    letter-spacing: 0.5px;
    margin-top: 0;
    font-weight: 300;
}

.card {
    background: rgba(24, 24, 24, 0.75);
    border: 1px solid rgba(239, 68, 68, 0.15);
    border-radius: 20px;
    padding: 28px;
    height: 260px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.4s ease;
    margin-bottom: 24px;
    box-shadow:
        0 4px 6px -1px rgba(0, 0, 0, 0.30),
        0 2px 4px -1px rgba(0, 0, 0, 0.20);
    position: relative;
    overflow: hidden;
}

.card:hover {
    transform: translateY(-8px);
    border-color: rgba(239, 68, 68, 0.55);
    box-shadow:
        0 20px 40px -5px rgba(220, 38, 38, 0.25),
        0 10px 20px -5px rgba(0, 0, 0, 0.50);
    background: rgba(35, 35, 35, 0.90);
}

.card .icon {
    font-size: 2.5rem;
    margin-bottom: 12px;
    display: inline-block;
    filter: drop-shadow(0 0 10px rgba(239, 68, 68, 0.45));
}

.card h3 {
    color: #F5F5F5;
    margin: 0 0 8px 0;
    font-size: 1.25rem;
    font-weight: 600;
}

.card p {
    color: #A3A3A3;
    font-size: 0.90rem;
    line-height: 1.6;
    margin: 0;
}

.btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    padding: 12px 20px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #DC2626 0%, #991B1B 100%);
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(220, 38, 38, 0.30);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.btn:hover {
    background: linear-gradient(135deg, #EF4444 0%, #B91C1C 100%);
    box-shadow: 0 8px 25px rgba(220, 38, 38, 0.45);
    transform: translateY(-2px);
}

.section-title {
    text-align: center;
    color: #D4D4D4;
    font-size: 1.15rem;
    margin: 10px 0 28px 0;
    font-weight: 400;
}

.custom-footer {
    text-align: center;
    color: #666666;
    margin-top: 40px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(239, 68, 68, 0.12);
}

footer, #MainMenu {
    visibility: hidden;
}

[data-testid="stSidebar"] {
    background: #0D0D0D !important;
    border-right: 1px solid rgba(239, 68, 68, 0.15) !important;
}

/* Streamlit button */
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(135deg, #DC2626, #991B1B);
    color: white;
    border: none;
    padding: 12px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #EF4444, #B91C1C);
    color: white;
    border: none;
}
</style>

<div class="hero">
    <h1>🚗 Recommend_car</h1>
    <p>ระบบแนะนำรถยนต์จากข้อมูลและความสัมพันธ์ของรถยนต์</p>
</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="section-title">🚗 รวมระบบ Recommend_car</div>',
    unsafe_allow_html=True,
)


APPS = [
    (
        "🚗",
        "โครงสร้างข้อมูลรถยนต์",
        "จัดการและวิเคราะห์ข้อมูลรถยนต์สำหรับระบบแนะนำ",
        "https://colab.research.google.com/drive/1TSqD6dk7fj__txvG_xBwG3HH9vDFcz5K?usp=sharing",
    ),
    (
        "📊",
        "วิเคราะห์ข้อมูลรถยนต์",
        "วิเคราะห์คุณสมบัติและความสัมพันธ์ของข้อมูลรถยนต์",
        "https://colab.research.google.com/drive/1tbFJ48SuP3vwyOX_ZFAfnXY3_4s_7JHW?usp=drive_link",
    ),
    (
        "🎯",
        "ระบบแนะนำรถยนต์",
        "แนะนำรถยนต์ที่เหมาะสมจากข้อมูลและความต้องการของผู้ใช้",
        "https://recommed-bfjta8sisqgrpbc7fbcfkx.streamlit.app/",
    ),
]


cols = st.columns(3)

for i, (icon, title, desc, url) in enumerate(APPS):

    with cols[i]:

        st.markdown(
            f"""
            <div class="card">
                <div>
                    <div class="icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "เปิดระบบ →",
            url,
            use_container_width=True,
        )


st.markdown(
    """
    <div class="custom-footer">
        Made with ❤️ using Streamlit · Recommend_car 2026
    </div>
    """,
    unsafe_allow_html=True,
)
```
