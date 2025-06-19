import streamlit as st
from streamlit_lottie import st_lottie
import requests
from pathlib import Path
import base64
import streamlit.components.v1 as components
# st-confetti is used for confetti effect
try:
    from st_confetti import confetti
except ImportError:
    confetti = None

# --------------------------------------------------
# ASSETS & DATA
# --------------------------------------------------
NAME    = "Amine Ali DJOUAB"
ROLE    = "AI Engineer – NLP & LLM Specialist"
TAGLINE = "Building scalable language-driven solutions for real-world impact"

HERE        = Path(__file__).resolve().parent
ASSETS      = HERE.parent / "assets"
RESUME_PATH = ASSETS / "CV_ENG.pdf"
VIDEO_PATH  = ASSETS / "sung-jin-woo-darkness.3840x2160.mp4"
PROFILE_IMG = ASSETS / "background.png"

EMAIL    = "amine.djouab03@gmail.com"
PHONE    = "+33 6 64 91 13 35"
LOCATION = "France"
SOCIALS = {
    "LinkedIn": "https://www.linkedin.com/in/amine-ali-djouab",
    "GitHub":   "https://github.com/aminedj97",
    "Kaggle":   "https://www.kaggle.com/aminedjouab",
}

SKILLS = {
    "Transformers & Tokenizers": 90,
    "Prompt Engineering & PEFT": 85,
    "Fine-tuning (LoRA, RLHF…)": 80,
    "PyTorch / TensorFlow":      85,
    "Scikit-Learn":              80,
    "CNN / RNN / MLP":           75,
    "Python / MicroPython":     95,
    "C / C++ / JavaScript":     75,
    "SQL / NoSQL":              80,
    "LangChain / HuggingFace":  80,
    "Symbolic & Multi-Agent AI":70,
}

EXPERIENCE = [
    {
        "role":    "AI Engineer Intern (LLM fine-tuning)",
        "company": "Université Côte d'Azur / I3S Lab",
        "period":  "Apr 2025 – Present",
        "details": (
            "Fine-tuned and evaluated large language models for pedagogical content, "
            "preprocessed and structured educational datasets, "
            "explored multi-agent knowledge integration (SMA)."
        )
    },
    {
        "role":    "Embedded Systems Intern",
        "company": "CRIStal Lille",
        "period":  "Apr 2024 – Oct 2024",
        "details": (
            "Developed and optimized real-time analog signal acquisition firmware, "
            "implemented autonomous sampling modes and synchronization."
        )
    },
    {
        "role":    "Full-Stack Web Dev Intern",
        "company": "Algérie Télécom Annaba",
        "period":  "Oct 2022 – Apr 2023",
        "details": (
            "Built a responsive web application, "
            "implemented new features and optimizations, "
            "authored technical documentation."
        )
    },
]

PROJECTS = [
    {
        "title": "Image Dimensionality Reduction",
        "description": "Research project on image dimensionality reduction in collaboration with Centrale Lille. Application of advanced compression and optimization techniques to maintain quality while significantly reducing data size.",
        "period": "Since September 2023",
    },
    {
        "title": "XAI for Medical Error Detection",
        "description": "Development of an explainable AI (XAI) system for detecting medical prescription errors. Focus on algorithmic decision transparency in medical context.",
        "period": "Since September 2023",
    },
    {
        "title": "Hospital Resource Optimization",
        "description": "Implementation of metaheuristic algorithms to optimize human and material resource management in hospitals. Improvement of operational efficiency and cost reduction.",
        "period": "Since September 2023",
    },
    {
        "title": "Augmented Reality Project",
        "description": "Design and development of an augmented reality solution integrated into smart glasses. Focus on user experience and seamless integration of AR technology.",
        "period": "Since September 2023",
    },
    {
        "title": "Automated AI Prompt Validation",
        "description": "Research on automation and validation of AI prompts compared to human medical expertise. Development of evaluation metrics and validation framework.",
        "period": "Since September 2023",
    },
    {
        "title": "Emergency Wait Time Optimization",
        "description": "Developed an AI model for emergency time optimization using machine learning algorithms (linear regression) and deep learning (MLP).",
        "period": "December 2023 to March 2024",
    },
    {
        "title": "Alzheimer Detection Application",
        "description": "Development of a native application for people with Alzheimer's disease, using logical trees for early disease detection. The application was built with React Native and Firebase.",
        "period": "January 2023 to July 2023",
    }
]

EDUCATION = [
    {
        "degree":  "Master in AI Management",
        "school":  "École Centrale de Lille",
        "period":  "Sep 2023 – Oct 2025",
        "location":"Lille, France",
    },
    {
        "degree":  "Bachelor in Computer Systems",
        "school":  "University of Chadli Ben Djedid",
        "period":  "Sep 2020 – Jun 2023",
        "location":"El Tarf, Algeria",
    },
]

CERTIFICATIONS = [
    {
        "title":    "TensorFlow Developer Certificate",
        "issuer":   "Google / Udemy",
        "date":     "Dec 2024",
    }
]

LOTTIE_ANIM_URL = "https://assets5.lottiefiles.com/packages/lf20_tfb3estd.json"
LOTTIE_EDU_URL  = "https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json"
LOTTIE_CERT_URL = "https://assets2.lottiefiles.com/packages/lf20_ysas1vcp.json"

def img_to_base64(img_path: Path) -> str:
    """Convert image file to base64 string."""
    if img_path.exists():
        data = img_path.read_bytes()
        return base64.b64encode(data).decode()
    return ""

# Get image extensions and base64 strings
profile_ext = PROFILE_IMG.suffix.lstrip(".")
profile_b64 = img_to_base64(PROFILE_IMG)

# --------------------------------------------------
# UTILS
# --------------------------------------------------
def load_lottie_url(url: str):
    """Fetch a Lottie animation by URL and return the JSON dict."""
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.warning(f"⚠️ Lottie animation couldn't be loaded: {e}")
        return None

def render_socials(socials):
    """Render social links as markdown with Font Awesome icons."""
    icons = {
        "LinkedIn": "fab fa-linkedin",
        "GitHub": "fab fa-github",
        "Kaggle": "fab fa-kaggle",
    }
    
    st.markdown("""
    <style>
    .header-social-links {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    .header-social-link {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #60a5fa;
        text-decoration: none;
        font-size: 1.1rem;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        background: rgba(59, 130, 246, 0.1);
        transition: all 0.3s ease;
    }
    .header-social-link:hover {
        background: rgba(59, 130, 246, 0.2);
        transform: translateY(-2px);
    }
    .header-social-link i {
        font-size: 1.2rem;
    }
    </style>
    <div class="header-social-links">
    """, unsafe_allow_html=True)
    
    for label, link in socials.items():
        icon_class = icons.get(label, "fas fa-link")
        st.markdown(
            f'<a href="{link}" target="_blank" class="header-social-link">'
            f'<i class="{icon_class}"></i> {label}'
            f'</a>', 
            unsafe_allow_html=True
        )
    
    st.markdown("</div>", unsafe_allow_html=True)

def project_card(proj, float_up=True):
    """Reusable project card component with alternating float animation."""
    float_class = "float-up" if float_up else "float-down"
    
    st.markdown(f'''
    <div class="project-card {float_class}">
        <h3 class="project-title">{proj['title']}</h3>
        <div class="project-period">{proj['period']}</div>
        <p class="project-description">{proj['description']}</p>
    </div>
    ''', unsafe_allow_html=True)

def section_card(title, icon_html, content_html):
    st.markdown(f'''
    <div class="fade-in-up card-section">
        <div class="section-header">{icon_html}<span>{title}</span></div>
        {content_html}
    </div>
    ''', unsafe_allow_html=True)

# --------------------------------------------------
# ANIMATED BACKGROUND (deep blue/black with glowing blue/cyan)
# --------------------------------------------------
st.markdown(
    """
    <style>
    .site-bg-glow {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh; z-index: -2;
        pointer-events: none;
        background:
            radial-gradient(circle at 60% 20%, rgba(14,165,233,0.22) 0%, rgba(36,37,64,0.0) 60%),
            radial-gradient(circle at 80% 80%, rgba(139,92,246,0.18) 0%, rgba(36,37,64,0.0) 70%),
            radial-gradient(circle at 30% 90%, rgba(59,130,246,0.13) 0%, rgba(36,37,64,0.0) 70%);
        filter: blur(40px);
        opacity: 0.95;
    }
    </style>
    <div class='site-bg-glow'></div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# SUPER SAIYAN CSS (mimics Tailwind for rest of app)
# --------------------------------------------------
st.markdown(
    """
    <style>
    .fade-in-up { opacity:0; transform:translateY(40px); animation: fadeInUp 1s cubic-bezier(.23,1.01,.32,1) forwards; }
    @keyframes fadeInUp { to {opacity:1; transform:translateY(0);} }
    .card-section {
        background: rgba(255,255,255,0.07);
        border-radius: 1.5rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.12);
        padding: 2rem 2.5rem;
        margin-bottom: 2.5rem;
        backdrop-filter: blur(6px);
    }
    .section-header {
        font-size: 1.6rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 0.7em;
        margin-bottom: 1.2rem;
    }
    .project-img {
        border-radius: 1rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.10);
        margin-bottom: 1rem;
    }
    .social-link {
        font-size: 1.3rem;
        margin-right: 1.2em;
        text-decoration: none;
        color: #0ea5e9;
        transition: color 0.2s;
    }
    .social-link:hover { color: #fbbf24; }
    .contact-info {
        font-size: 1.1rem;
        margin-bottom: 0.5em;
    }
    .exp-section-grid {
        display: flex;
        flex-direction: row;
        overflow-x: auto;
        gap: 2.2rem;
        background: #1e293b ;
        border-radius: 1.7rem;
        box-shadow: 0 8px 48px 0 rgba(59,130,246,0.18), 0 1.5px 8px 0 rgba(139,92,246,0.13);
        padding: 2.5rem 1.5rem 1.5rem 1.5rem;
        margin-bottom: 2.5rem;
        border: 2px solid rgba(59,130,246,0.18);
        backdrop-filter: blur(14px);
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }
    .exp-section-grid::-webkit-scrollbar {
        display: none;
    }
    .exp-card {
        min-width: 420px;
        max-width: 480px;
        flex: 0 0 420px;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        background: linear-gradient(120deg, rgba(24, 27, 54, 0.98) 80%, rgba(59,130,246,0.13) 100%);
        border-left: 7px solid;
        border-image: linear-gradient(to bottom, #0ea5e9, #8b5cf6) 1;
        border-radius: 1.2rem;
        box-shadow: 0 2px 32px 0 #0ea5e955, 0 1.5px 8px 0 #8b5cf655;
        padding: 1.2rem 1.5rem 1.2rem 1.2rem;
        transition: box-shadow 0.2s, border-color 0.2s;
    }
    .exp-card:hover {
        box-shadow: 0 6px 32px 0 #8b5cf6cc, 0 1.5px 8px 0 #0ea5e9cc;
        border-left: 8px solid;
        border-image: linear-gradient(to bottom, #6366f1, #0ea5e9) 1;
    }
    .exp-card-icon {
        font-size: 2.2em;
        margin-right: 1.2em;
        margin-top: 0.2em;
        flex-shrink: 0;
        color: #8b5cf6;
        filter: drop-shadow(0 2px 6px #3b82f6cc);
    }
    .exp-card-content {
        flex: 1;
    }
    .exp-role {
        font-size: 1.18em;
        font-weight: 700;
        margin-bottom: 0.1em;
        color: #fff;
        letter-spacing: 0.01em;
        text-shadow: 0 2px 8px #0ea5e966;
    }
    .exp-company {
        color: #60a5fa;
        font-weight: 600;
        font-size: 1.05em;
        text-shadow: 0 1px 6px #0ea5e966;
    }
    .exp-period {
        background: linear-gradient(90deg, #6366f1 60%, #0ea5e9 100%);
        color: #fff;
        border-radius: 999px;
        padding: 0.18em 0.9em;
        font-size: 0.98em;
        margin-left: 0.7em;
        font-weight: 500;
        display: inline-block;
        box-shadow: 0 1px 6px #6366f133;
        text-shadow: 0 1px 6px #6366f199;
    }
    .exp-details {
        font-size: 1.05em;
        color: #e0e7ef;
        margin-top: 0.5em;
        letter-spacing: 0.01em;
        text-shadow: 0 1px 6px #0ea5e966;
    }
    /* Project Cards Animation and Styling */
    @keyframes floatUp {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    
    @keyframes floatDown {
        0% { transform: translateY(0px); }
        50% { transform: translateY(15px); }
        100% { transform: translateY(0px); }
    }
    
    .project-card {
        background: rgba(17, 24, 39, 0.7);
        border-radius: 16px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(59, 130, 246, 0.2);
        padding: 2rem;
        margin-bottom: 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .project-card.float-up {
        animation: floatUp 6s ease-in-out infinite;
    }
    
    .project-card.float-down {
        animation: floatDown 6s ease-in-out infinite;
        animation-delay: 0.5s;
    }
    
    .project-card:hover {
        border-color: rgba(99, 102, 241, 0.8);
        box-shadow: 0 8px 32px 0 rgba(78, 16, 229, 0.37);
        transform: scale(1.02);
    }
    
    .project-title {
        color: #e0e7ff;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .project-period {
        color: #60a5fa;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        font-style: italic;
        display: inline-block;
        background: rgba(96, 165, 250, 0.1);
        padding: 0.3rem 0.8rem;
        border-radius: 9999px;
    }
    
    .project-description {
        color: #94a3b8;
        font-size: 1rem;
        line-height: 1.6;
        white-space: pre-line;
    }
    </style>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const slider = document.querySelector('.exp-section-grid');
        let isDown = false;
        let startX;
        let scrollLeft;
        if (slider) {
            slider.addEventListener('mousedown', (e) => {
                isDown = true;
                slider.classList.add('active');
                startX = e.pageX - slider.offsetLeft;
                scrollLeft = slider.scrollLeft;
            });
            slider.addEventListener('mouseleave', () => {
                isDown = false;
                slider.classList.remove('active');
            });
            slider.addEventListener('mouseup', () => {
                isDown = false;
                slider.classList.remove('active');
            });
            slider.addEventListener('mousemove', (e) => {
                if (!isDown) return;
                e.preventDefault();
                const x = e.pageX - slider.offsetLeft;
                const walk = (x - startX) * 1.2; //scroll-fast
                slider.scrollLeft = scrollLeft - walk;
            });
        }
    });
    </script>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Djouab Amine ALi - Final Boss",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add Font Awesome CSS
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# Add custom styling with background images
st.markdown(
    f"""
    <style>
      /* Main content area background */
      div[data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.97), rgba(30, 41, 59, 0.97), rgba(49, 46, 129, 0.97)),
                    url("data:image/{profile_ext};base64,{profile_b64}") no-repeat center center fixed !important;
        background-size: cover !important;
        background-blend-mode: overlay !important;
      }}
      /* Sidebar styling */
      div[data-testid="stSidebar"] > div:first-child {{
        background: #1f2937 !important;
        color: #ffffff !important;
      }}
      div[data-testid="stSidebar"] h2,
      div[data-testid="stSidebar"] p {{
        color: #ffffff !important;
      }}
      /* Experience grid styling */
      .exp-section-grid {{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
      }}
      /* Default text color */
      [data-testid="stMarkdownContainer"] {{
        color: #e0e7ef !important;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Header Section
# --------------------------------------------------

if confetti:
    confetti()

with st.container():
    left, right = st.columns([3, 2])

    with left:
        if VIDEO_PATH.exists():
            with open(VIDEO_PATH, "rb") as video_file:
                video_bytes = video_file.read()
                encoded = base64.b64encode(video_bytes).decode()
                video_html = f'''
                    <video width="400" autoplay loop muted playsinline style="border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.08);">
                        <source src="data:video/mp4;base64,{encoded}" type="video/mp4" />
                    </video>
                '''
                st.markdown(video_html, unsafe_allow_html=True)
        else:
            st.error(f"❌ File not found: {VIDEO_PATH}")
        st.markdown(f"<div class='fade-in-up'><h1 style='margin-bottom:0'>{NAME}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='margin-top:0'>{ROLE}</h3>", unsafe_allow_html=True)
        st.write(TAGLINE)
        render_socials(SOCIALS)
        if RESUME_PATH.exists():
            with open(RESUME_PATH, "rb") as f:
                st.download_button("⬇ Download CV", data=f.read(), file_name=RESUME_PATH.name, mime="application/pdf")
        else:
            st.info("Add your CV PDF next to this script to enable the download button.")

    with right:
        st.markdown("""
        <div style='padding: 1.5em 0 0 0;'>
            <div style='font-size:1.2em;font-weight:700;margin-bottom:0.7em;color:#0ea5e9;'>Core Skills</div>
        </div>
        """, unsafe_allow_html=True)
        for skill, pct in SKILLS.items():
            st.markdown(f"""
            <div class="skill-item">
                <div class="skill-info">
                    <span class="skill-name">{skill}</span>
                    <span class="skill-percentage">{pct}%</span>
                </div>
                <div class="skill-bar-bg">
                    <div class="skill-bar-fill" style="width:{pct}%">
                        <div class="skill-bar-shine"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <style>
        .skill-item {
            margin-bottom: 1.2rem;
            transition: transform 0.3s ease;
        }
        
        .skill-item:hover {
            transform: translateY(-2px);
        }
        
        .skill-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.4rem;
        }
        
        .skill-name {
            color: #e0e7ef;
            font-weight: 500;
            font-size: 1rem;
        }
        
        .skill-percentage {
            color: #60a5fa;
            font-size: 0.9rem;
            font-weight: 600;
        }
        
        .skill-bar-bg {
            background: rgba(15, 23, 42, 0.6);
            border-radius: 999px;
            height: 8px;
            overflow: hidden;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        
        .skill-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #0ea5e9, #6366f1);
            border-radius: 999px;
            position: relative;
            transition: all 0.3s ease;
        }
        
        .skill-bar-shine {
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(255, 255, 255, 0.2),
                transparent
            );
            animation: shine 3s infinite;
        }
        
        .skill-item:hover .skill-bar-fill {
            background: linear-gradient(90deg, #6366f1, #0ea5e9);
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);
        }
        
        @keyframes shine {
            0% {
                left: -100%;
            }
            20% {
                left: 100%;
            }
            100% {
                left: 100%;
            }
        }
        </style>
        """, unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------------
# About Section
# --------------------------------------------------

with st.container():
    st.subheader("About Me")
    st.write("""\
    I'm an AI Engineer specialized in NLP & LLM, with hands-on expertise in fine-tuning,
        model evaluation, and prompt engineering. I build scalable language-driven solutions
        that turn unstructured text into actionable insights and power next-gen generative AI
        products for innovative teams.
    """)

# --------------------------------------------------
# Experience (Modern Card Layout with Glowing Blue/Violet Grid)
# --------------------------------------------------
with st.container():
    st.markdown("""
    <h2 style='color: #e0e7ff; margin-bottom: 2rem; font-size: 2rem; font-weight: 600;'>
        Experience
    </h2>
    <div class="experience-grid">
    """, unsafe_allow_html=True)
    
    # Create modern experience cards with left border
    for exp in EXPERIENCE:
        st.markdown(f'''
        <div class="experience-card">
            <div class="briefcase-icon">💼</div>
            <div class="card-content">
                <h3 class="exp-title">{exp['role']}</h3>
                <div class="exp-company-row">
                    <span class="exp-company">{exp['company']}</span>
                    <span class="exp-period">{exp['period']}</span>
                </div>
                <p class="exp-details">{exp['details']}</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# Update the CSS for modern experience cards
st.markdown("""
<style>
.experience-grid {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 0.5rem;
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
}

.experience-card {
    width: 100%;
    display: flex;
    align-items: flex-start;
    gap: 1.5rem;
    background: linear-gradient(120deg, rgba(15, 23, 42, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);
    border-radius: 12px;
    border-left: 6px solid;
    border-image: linear-gradient(to bottom, #0ea5e9, #6366f1) 1;
    padding: 1.5rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.briefcase-icon {
    font-size: 1.8rem;
    margin-top: 0.2rem;
    color: #6366f1;
    filter: drop-shadow(0 0 8px rgba(99, 102, 241, 0.3));
}

.card-content {
    flex: 1;
}

.exp-title {
    color: #ffffff;
    font-size: 1.2rem;
    font-weight: 600;
    margin: 0 0 0.5rem 0;
    letter-spacing: 0.01em;
}

.exp-company-row {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.8rem;
    flex-wrap: wrap;
}

.exp-company {
    color: #60a5fa;
    font-weight: 500;
    font-size: 1rem;
}

.exp-period {
    background: linear-gradient(90deg, #6366f1 0%, #0ea5e9 100%);
    color: white;
    padding: 0.2rem 0.8rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 500;
}

.exp-details {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.5;
    margin: 0;
}

.experience-card:hover {
    border-image: linear-gradient(to bottom, #6366f1, #0ea5e9) 1;
    box-shadow: 0 4px 25px rgba(99, 102, 241, 0.15);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Projects Section
# --------------------------------------------------

with st.container():
    st.markdown("""
    <h2 style='color: #e0e7ff; margin-bottom: 2rem; font-size: 2rem; font-weight: 600;'>
        Academic Projects
    </h2>
    """, unsafe_allow_html=True)
    
    # Create a 2-column layout for projects
    col1, col2 = st.columns(2)
    
    # Distribute projects across columns with alternating float animations
    for i, proj in enumerate(PROJECTS):
        with col1 if i % 2 == 0 else col2:
            project_card(proj, float_up=(i % 2 == 0))

# --------------------------------------------------
# Contact Section
# --------------------------------------------------

with st.container():
    st.markdown("""
    <div class="contact-section">
        <h2 class="section-title">Get In Touch</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Social Links
    st.markdown("""
    <div class="social-links">
        <a href="https://www.linkedin.com/in/amine-ali-djouab" target="_blank" class="social-link">
            <i class="fab fa-linkedin"></i>
            <span>LinkedIn</span>
        </a>
        <a href="https://github.com/aminedj97" target="_blank" class="social-link">
            <i class="fab fa-github"></i>
            <span>GitHub</span>
        </a>
        <a href="https://www.kaggle.com/aminedjouab" target="_blank" class="social-link">
            <i class="fab fa-kaggle"></i>
            <span>Kaggle</span>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Info Grid
    st.markdown(f"""
    <div class="contact-info-grid">
        <div class="contact-info-item">
            <i class="fas fa-envelope"></i>
            <span>{EMAIL}</span>
        </div>
        <div class="contact-info-item">
            <i class="fas fa-phone"></i>
            <span>{PHONE}</span>
        </div>
        <div class="contact-info-item">
            <i class="fas fa-map-marker-alt"></i>
            <span>{LOCATION}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Styles
    st.markdown("""
    <style>
    .contact-section {
        background: linear-gradient(120deg, rgba(15, 23, 42, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);
        border-radius: 16px;
        border: 1px solid rgba(59, 130, 246, 0.2);
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .section-title {
        color: #e0e7ff;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
        padding: 0 1rem;
    }
    
    .social-link {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #60a5fa;
        text-decoration: none;
        font-size: 1.1rem;
        padding: 0.7rem 1.2rem;
        border-radius: 8px;
        background: rgba(59, 130, 246, 0.1);
        transition: all 0.3s ease;
    }
    
    .social-link:hover {
        background: rgba(59, 130, 246, 0.2);
        transform: translateY(-2px);
        color: #60a5fa;
        text-decoration: none;
    }
    
    .social-link i {
        font-size: 1.4rem;
    }
    
    .contact-info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
        padding: 0 1rem;
    }
    
    .contact-info-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        color: #94a3b8;
        font-size: 1rem;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .contact-info-item:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateY(-2px);
    }
    
    .contact-info-item i {
        color: #60a5fa;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("""<center><small>Made with ❤️ + Streamlit · © 2025 Amine Ali DJOUAB</small></center>""", unsafe_allow_html=True) 