import streamlit as st
 
st.set_page_config(
    page_title="Recommend_car",
    page_icon="🚗",
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
 
/* ซ่อน sidebar ทั้งหมด เพราะใช้ navbar เองแทน */
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
 
/* ---------- Hero ---------- */
.hero {
    position: relative;
    min-height: 62vh;
    padding: 90px 4% 70px 4%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background:
        linear-gradient(77deg, rgba(0,0,0,.85) 0%, rgba(0,0,0,.35) 55%, rgba(0,0,0,0) 100%),
        linear-gradient(0deg, var(--nf-bg) 0%, rgba(20,20,20,0) 30%),
        radial-gradient(circle at 78% 35%, rgba(229,9,20,.55) 0%, rgba(229,9,20,0) 45%),
        linear-gradient(135deg, #2a0306 0%, #0b0b0b 70%);
    overflow: hidden;
}
.hero .bg-car {
    position: absolute;
    right: 6%;
    top: 50%;
    transform: translateY(-50%);
    font-size: 15rem;
    opacity: .16;
    filter: blur(1px);
    pointer-events: none;
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
    font-size: clamp(3rem, 8vw, 6rem);
    font-weight: 400;
    line-height: 1;
    margin: 0 0 16px 0;
    letter-spacing: 2px;
    text-shadow: 2px 4px 12px rgba(0,0,0,.6);
}
.hero p {
    max-width: 560px;
    font-size: 1.15rem;
    color: #E5E5E5;
    line-height: 1.6;
    margin: 0 0 26px 0;
    text-shadow: 1px 2px 6px rgba(0,0,0,.7);
}
.hero .meta {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-bottom: 18px;
    font-size: .9rem;
    color: var(--nf-muted);
}
.hero .match { color: #46D369; font-weight: 700; }
.hero .badge {
    border: 1px solid rgba(255,255,255,.4);
    padding: 0 6px;
    border-radius: 3px;
    font-size: .8rem;
}
.hero-btns { display: flex; gap: 12px; flex-wrap: wrap; }
.nbtn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 28px;
    border-radius: 4px;
    font-size: 1.1rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: all .2s ease;
}
.nbtn.play { background: #FFFFFF; color: #000000 !important; }
.nbtn.play:hover { background: rgba(255,255,255,.75); }
.nbtn.info { background: rgba(109,109,110,.7); color: #FFFFFF !important; }
.nbtn.info:hover { background: rgba(109,109,110,.45); }
 
/* ---------- Rows ---------- */
.row { padding: 0 4%; margin-top: 12px; }
.row-title {
    font-size: 1.35rem;
    font-weight: 600;
    margin: 26px 0 14px 0;
    color: #E5E5E5;
}
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 14px;
}
 
/* ---------- Poster cards ---------- */
.poster {
    position: relative;
    display: block;
    aspect-ratio: 16 / 9;
    border-radius: 6px;
    overflow: hidden;
    text-decoration: none !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 14px rgba(0,0,0,.5);
    transition: transform .3s ease, box-shadow .3s ease;
}
.poster:hover {
    transform: scale(1.06);
    z-index: 10;
    box-shadow: 0 18px 40px rgba(0,0,0,.8);
}
.poster .icon {
    position: absolute;
    right: 8%;
    top: 12%;
    font-size: 5.5rem;
    opacity: .9;
    filter: drop-shadow(0 6px 14px rgba(0,0,0,.6));
}
.poster .num {
    position: absolute;
    left: 14px;
    bottom: 6px;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 6.5rem;
    line-height: 1;
    color: transparent;
    -webkit-text-stroke: 3px rgba(255,255,255,.55);
}
.poster .info-box {
    position: absolute;
    left: 0; right: 0; bottom: 0;
    padding: 36px 16px 14px 16px;
    background: linear-gradient(0deg, rgba(0,0,0,.92) 0%, rgba(0,0,0,0) 100%);
}
.poster h3 {
    margin: 0 0 4px 0;
    font-size: 1.1rem;
    font-weight: 600;
    text-align: right;
}
.poster p {
    margin: 0;
    font-size: .8rem;
    color: #D2D2D2;
    line-height: 1.45;
    text-align: right;
}
.poster .go {
    position: absolute;
    top: 12px;
    left: 12px;
    background: var(--nf-red);
    padding: 2px 10px;
    border-radius: 3px;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: 1px;
}
.g1 { background: linear-gradient(135deg, #E50914 0%, #4a0408 100%); }
.g2 { background: linear-gradient(135deg, #831010 0%, #1a1a1a 100%); }
.g3 { background: linear-gradient(135deg, #b20710 0%, #0f0f0f 100%); }
 
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
 
APPS = [
    {
        "icon": "🚗",
        "title": "โครงสร้างข้อมูลรถยนต์",
        "desc": "จัดการและวิเคราะห์ข้อมูลรถยนต์สำหรับระบบแนะนำ",
        "url": "https://colab.research.google.com/drive/1TSqD6dk7fj__txvG_xBwG3HH9vDFcz5K?usp=sharing",
        "tag": "NOTEBOOK",
        "grad": "g1",
    },
    {
        "icon": "📊",
        "title": "วิเคราะห์ข้อมูลรถยนต์",
        "desc": "วิเคราะห์คุณสมบัติและความสัมพันธ์ของข้อมูลรถยนต์",
        "url": "https://colab.research.google.com/drive/1tbFJ48SuP3vwyOX_ZFAfnXY3_4s_7JHW?usp=drive_link",
        "tag": "NOTEBOOK",
        "grad": "g2",
    },
    {
        "icon": "🎯",
        "title": "ระบบแนะนำรถยนต์",
        "desc": "แนะนำรถยนต์ที่เหมาะสมจากข้อมูลและความต้องการของผู้ใช้",
        "url": "https://recommed-bfjta8sisqgrpbc7fbcfkx.streamlit.app/",
        "tag": "LIVE APP",
        "grad": "g3",
    },
 {
        "icon": "🎯",
        "title": "canva นำเสนอ",
        "desc": "Canva",
        "url": "https://canva.link/713sawc3mr83jej",
        "tag": "LIVE APP",
        "grad": "g4",
    },
]
 
MAIN_URL = APPS[2]["url"]
FIRST_URL = APPS[0]["url"]
 
# HTML ทั้งหมดเขียนชิดซ้าย เพื่อไม่ให้ Markdown มองเป็น code block
hero = f"""
<div class="nav">
<div class="logo">RECOMMEND_CAR</div>
<a href="/" target="_self">หน้าแรก</a>
<a href="#systems">ระบบทั้งหมด</a>
<a href="/about" target="_self">ผู้พัฒนา</a>
</div>
<div class="hero">
<div class="bg-car">🚗</div>
<div class="tag">GRAPH DATABASE ORIGINAL</div>
<h1>RECOMMEND_CAR</h1>
<div class="meta">
<span class="match">แม่นยำ 98%</span>
<span>2026</span>
<span class="badge">3 ระบบ</span>
<span>Graph · Neo4j · Cypher</span>
</div>
<p>ระบบแนะนำรถยนต์จากข้อมูลและความสัมพันธ์ของรถยนต์ ค้นหารถที่ใช่จากเครือข่ายเพื่อนและสิ่งที่คนรอบตัวคุณขับ</p>
<div class="hero-btns">
<a class="nbtn play" href="{MAIN_URL}" target="_blank">▶ เริ่มใช้งาน</a>
<a class="nbtn info" href="{FIRST_URL}" target="_blank">ⓘ ข้อมูลเพิ่มเติม</a>
</div>
</div>
"""
 
cards = ""
for i, a in enumerate(APPS, start=1):
    cards += (
        f'<a class="poster {a["grad"]}" href="{a["url"]}" target="_blank">'
        f'<span class="go">{a["tag"]}</span>'
        f'<span class="icon">{a["icon"]}</span>'
        f'<span class="num">{i}</span>'
        f'<div class="info-box"><h3>{a["title"]}</h3><p>{a["desc"]}</p></div>'
        f"</a>"
    )
 
rows = (
    '<div class="row" id="systems">'
    '<div class="row-title">รวมระบบ Recommend_car</div>'
    f'<div class="grid">{cards}</div>'
    "</div>"
)
 
footer = '<div class="nf-footer">Made with ❤️ using Streamlit · Recommend_car 2026</div>'
 
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(hero, unsafe_allow_html=True)
st.markdown(rows, unsafe_allow_html=True)
st.markdown(footer, unsafe_allow_html=True)
