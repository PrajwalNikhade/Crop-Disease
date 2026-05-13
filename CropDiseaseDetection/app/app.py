"""
Crop Disease Detection — Streamlit Web Application
Premium UI with user-friendly design for non-technical users.
"""

import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from predict import predict_disease, is_model_available
from disease_info import get_disease_info, get_readable_name, get_severity_color

# ──────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="🌿 Crop Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ──────────────────────────────────────────────
# Custom CSS — Premium Dark Theme
# ──────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Import Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Global ── */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hero Section ── */
    .hero-container {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #1a3a2a 100%);
        border-radius: 20px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        border: 1px solid #30363d;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 50%, rgba(76, 175, 80, 0.08) 0%, transparent 50%);
        pointer-events: none;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4CAF50, #81C784, #A5D6A7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #8b949e;
        font-weight: 300;
        margin-bottom: 0;
    }

    /* ── Result Cards ── */
    .result-card {
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid #30363d;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .result-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
    }
    .result-title {
        font-size: 1rem;
        font-weight: 600;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    .result-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #e6edf3;
    }

    /* ── Confidence Gauge ── */
    .confidence-container {
        background: #161b22;
        border-radius: 16px;
        padding: 2rem;
        border: 1px solid #30363d;
        text-align: center;
        margin: 1rem 0;
    }
    .confidence-value {
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    .confidence-label {
        font-size: 0.9rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .confidence-bar {
        width: 100%;
        height: 12px;
        background: #21262d;
        border-radius: 6px;
        margin-top: 1rem;
        overflow: hidden;
    }
    .confidence-fill {
        height: 100%;
        border-radius: 6px;
        transition: width 1s ease-in-out;
    }

    /* ── Severity Badge ── */
    .severity-badge {
        display: inline-block;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
    }

    /* ── Treatment Card ── */
    .treatment-card {
        background: linear-gradient(135deg, #1a2332 0%, #0d1117 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.8rem 0;
        border-left: 4px solid;
    }
    .treatment-card h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1rem;
        font-weight: 600;
    }
    .treatment-card p {
        margin: 0;
        color: #8b949e;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* ── Info Card ── */
    .info-section {
        background: #161b22;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border: 1px solid #30363d;
    }
    .info-section h4 {
        color: #e6edf3;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .info-section p {
        color: #8b949e;
        font-size: 0.95rem;
        line-height: 1.6;
        margin: 0;
    }

    /* ── Upload Area ── */
    .upload-area {
        background: linear-gradient(135deg, #161b22 0%, #1a2332 100%);
        border: 2px dashed #30363d;
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        margin: 1.5rem 0;
        transition: border-color 0.3s;
    }
    .upload-area:hover {
        border-color: #4CAF50;
    }

    /* ── Step Indicator ── */
    .step-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    .step-item {
        text-align: center;
        padding: 1rem;
    }
    .step-number {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #4CAF50, #2E7D32);
        color: white;
        font-size: 1.3rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 0.5rem;
    }
    .step-text {
        color: #8b949e;
        font-size: 0.85rem;
        font-weight: 500;
    }

    /* ── Feature Cards ── */
    .feature-card {
        background: #161b22;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #30363d;
        height: 100%;
        transition: transform 0.2s;
    }
    .feature-card:hover {
        transform: translateY(-4px);
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 0.8rem;
    }
    .feature-title {
        font-size: 1rem;
        font-weight: 600;
        color: #e6edf3;
        margin-bottom: 0.3rem;
    }
    .feature-desc {
        font-size: 0.85rem;
        color: #8b949e;
    }

    /* ── Disease Library Cards ── */
    .disease-lib-card {
        background: #161b22;
        border-radius: 12px;
        padding: 1.2rem;
        border: 1px solid #30363d;
        margin-bottom: 0.8rem;
    }

    /* ── Hide Streamlit defaults ── */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Sidebar Navigation
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0;">
        <div style="font-size: 3rem;">🌿</div>
        <div style="font-size: 1.2rem; font-weight: 700; color: #4CAF50; margin-top: 0.3rem;">
            CropGuard AI
        </div>
        <div style="font-size: 0.8rem; color: #8b949e; margin-top: 0.2rem;">
            Disease Detection System
        </div>
    </div>
    <hr style="border-color: #30363d; margin: 1rem 0;">
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠 Home", "🔍 Detect Disease", "📚 Disease Library", "ℹ️ About"],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border-color: #30363d; margin: 1rem 0;'>", unsafe_allow_html=True)

    # Model status
    model_ready = is_model_available()
    if model_ready:
        st.success("✅ Model loaded & ready")
    else:
        st.error("❌ Model not found")
        st.caption("Train the model first using `scripts/train_model.py`")

    st.markdown("""
    <div style="position: fixed; bottom: 1rem; color: #484f58; font-size: 0.75rem;">
        Built with ❤️ using TensorFlow & Streamlit
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Page: Home
# ──────────────────────────────────────────────
if page == "🏠 Home":
    # Hero
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🌿 CropGuard AI</div>
        <div class="hero-subtitle">
            Upload a photo of your crop leaf and get instant disease detection
            with treatment recommendations — powered by Deep Learning
        </div>
    </div>
    """, unsafe_allow_html=True)

    # How it works
    st.markdown("### How It Works")
    st.markdown("""
    <div class="step-container">
        <div class="step-item">
            <div class="step-number">1</div>
            <div class="step-text">📸 Take Photo<br>of crop leaf</div>
        </div>
        <div class="step-item">
            <div class="step-number">2</div>
            <div class="step-text">📤 Upload Image<br>to the app</div>
        </div>
        <div class="step-item">
            <div class="step-number">3</div>
            <div class="step-text">🤖 AI Analyzes<br>the leaf</div>
        </div>
        <div class="step-item">
            <div class="step-number">4</div>
            <div class="step-text">💊 Get Results<br>& treatment</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Features
    st.markdown("### Features")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔬</div>
            <div class="feature-title">Disease Detection</div>
            <div class="feature-desc">Identifies 38 types of crop diseases accurately</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Confidence Score</div>
            <div class="feature-desc">Shows how sure the AI is about its prediction</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💊</div>
            <div class="feature-title">Treatment Guide</div>
            <div class="feature-desc">Get recommended treatments and prevention tips</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🌾</div>
            <div class="feature-title">Multi-Crop</div>
            <div class="feature-desc">Supports tomato, potato, corn, apple, grape & more</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Supported Crops")
    crops = ["🍎 Apple", "🫐 Blueberry", "🍒 Cherry", "🌽 Corn", "🍇 Grape",
             "🍊 Orange", "🍑 Peach", "🫑 Bell Pepper", "🥔 Potato",
             "🫐 Raspberry", "🫘 Soybean", "🎃 Squash", "🍓 Strawberry", "🍅 Tomato"]
    cols = st.columns(7)
    for i, crop in enumerate(crops):
        with cols[i % 7]:
            st.markdown(f"<div style='text-align:center; padding:0.5rem; background:#161b22; "
                       f"border-radius:10px; margin:0.3rem 0; font-size:0.85rem;'>{crop}</div>",
                       unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Page: Detect Disease
# ──────────────────────────────────────────────
elif page == "🔍 Detect Disease":
    st.markdown("""
    <div class="hero-container" style="padding: 2rem;">
        <div class="hero-title" style="font-size: 2rem;">🔍 Detect Crop Disease</div>
        <div class="hero-subtitle">Upload a clear photo of a crop leaf to detect diseases</div>
    </div>
    """, unsafe_allow_html=True)

    if not model_ready:
        st.error("⚠️ **Model not loaded.** Please train the model first by running `python scripts/train_model.py`")
        st.stop()

    # Upload section
    st.markdown("### 📤 Upload Leaf Image")
    st.markdown("<p style='color:#8b949e;'>Take a clear, well-lit photo of the leaf. "
                "Make sure the leaf fills most of the image.</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png", "bmp"],
        help="Upload a clear photo of a crop leaf",
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        col_img, col_result = st.columns([1, 1], gap="large")

        with col_img:
            st.markdown("### 🖼️ Your Image")
            st.image(uploaded_file, use_container_width=True)

        with col_result:
            with st.spinner("🤖 AI is analyzing your leaf..."):
                try:
                    result = predict_disease(uploaded_file)
                    disease_info = get_disease_info(result["class_name"])
                    confidence = result["confidence"]
                    severity_color = get_severity_color(disease_info["severity"])

                    # Confidence color
                    if confidence >= 80:
                        conf_color = "#4CAF50"
                        conf_label = "High Confidence"
                    elif confidence >= 50:
                        conf_color = "#FF9800"
                        conf_label = "Medium Confidence"
                    else:
                        conf_color = "#F44336"
                        conf_label = "Low Confidence"

                    # ── Disease Name ──
                    st.markdown("### 🔬 Detection Result")

                    if disease_info["severity"] == "Healthy":
                        st.markdown(f"""
                        <div class="result-card" style="border-left: 4px solid #4CAF50;">
                            <div class="result-title">Detected Condition</div>
                            <div class="result-value" style="color: #4CAF50;">
                                ✅ {disease_info['crop']} — Healthy
                            </div>
                            <div style="margin-top:0.5rem;">
                                <span class="severity-badge" style="background: rgba(76,175,80,0.2); color: #4CAF50;">
                                    🟢 HEALTHY
                                </span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="result-card" style="border-left: 4px solid {severity_color};">
                            <div class="result-title">Detected Disease</div>
                            <div class="result-value">
                                ⚠️ {disease_info['crop']} — {disease_info['disease']}
                            </div>
                            <div style="margin-top:0.5rem;">
                                <span class="severity-badge"
                                      style="background: rgba(244,67,54,0.15); color: {severity_color};">
                                    Severity: {disease_info['severity']}
                                </span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    # ── Confidence Gauge ──
                    st.markdown(f"""
                    <div class="confidence-container">
                        <div class="confidence-label">AI Confidence Level</div>
                        <div class="confidence-value" style="color: {conf_color};">
                            {confidence:.1f}%
                        </div>
                        <div style="font-size: 0.85rem; color: {conf_color}; margin-bottom: 0.5rem;">
                            {conf_label}
                        </div>
                        <div class="confidence-bar">
                            <div class="confidence-fill"
                                 style="width: {confidence}%; background: linear-gradient(90deg, {conf_color}, {conf_color}88);">
                            </div>
                        </div>
                        <div style="margin-top: 0.8rem; font-size: 0.8rem; color: #8b949e;">
                            {"✅ The AI is very confident about this result." if confidence >= 80
                             else "⚠️ Consider uploading a clearer image for better results." if confidence >= 50
                             else "❌ The AI is not sure. Please try a clearer or different image."}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"❌ Error during prediction: {str(e)}")
                    st.stop()

        # ── Treatment & Information Section ──
        if uploaded_file is not None and 'disease_info' in dir():
            st.markdown("---")
            st.markdown("### 📋 Detailed Information")

            col_a, col_b = st.columns(2, gap="large")

            with col_a:
                # Description
                st.markdown(f"""
                <div class="info-section">
                    <h4>📖 About This Condition</h4>
                    <p>{disease_info['description']}</p>
                </div>
                """, unsafe_allow_html=True)

                # Symptoms
                st.markdown(f"""
                <div class="info-section">
                    <h4>🔎 Symptoms to Look For</h4>
                    <p>{disease_info['symptoms']}</p>
                </div>
                """, unsafe_allow_html=True)

            with col_b:
                # Treatment
                treat_color = "#4CAF50" if disease_info["severity"] == "Healthy" else "#2196F3"
                st.markdown(f"""
                <div class="treatment-card" style="border-color: {treat_color};">
                    <h4 style="color: {treat_color};">💊 Recommended Treatment</h4>
                    <p>{disease_info['treatment']}</p>
                </div>
                """, unsafe_allow_html=True)

                # Prevention
                st.markdown(f"""
                <div class="treatment-card" style="border-color: #FF9800;">
                    <h4 style="color: #FF9800;">🛡️ Prevention Tips</h4>
                    <p>{disease_info['prevention']}</p>
                </div>
                """, unsafe_allow_html=True)

            # Disclaimer
            st.markdown("""
            <div style="background: rgba(255,152,0,0.1); border-radius: 12px; padding: 1rem;
                        margin-top: 1.5rem; border: 1px solid rgba(255,152,0,0.3);">
                <p style="color: #FF9800; font-size: 0.85rem; margin: 0;">
                    ⚠️ <strong>Disclaimer:</strong> This AI tool is meant to assist farmers and is not a
                    substitute for professional agricultural advice. Please consult a local agricultural
                    expert for confirmed diagnosis and treatment plans.
                </p>
            </div>
            """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Page: Disease Library
# ──────────────────────────────────────────────
elif page == "📚 Disease Library":
    from disease_info import DISEASE_INFO

    st.markdown("""
    <div class="hero-container" style="padding: 2rem;">
        <div class="hero-title" style="font-size: 2rem;">📚 Disease Library</div>
        <div class="hero-subtitle">Browse all diseases our AI can detect, with treatment information</div>
    </div>
    """, unsafe_allow_html=True)

    # Filter options
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        crops = sorted(set(info["crop"] for info in DISEASE_INFO.values()))
        selected_crop = st.selectbox("Filter by Crop", ["All Crops"] + crops)
    with col_f2:
        severities = ["All", "Healthy", "Low", "Medium", "High"]
        selected_severity = st.selectbox("Filter by Severity", severities)

    st.markdown("---")

    # Display diseases
    for class_name, info in sorted(DISEASE_INFO.items()):
        if selected_crop != "All Crops" and info["crop"] != selected_crop:
            continue
        if selected_severity != "All" and info["severity"] != selected_severity:
            continue

        sev_color = get_severity_color(info["severity"])
        with st.expander(f"{'✅' if info['severity'] == 'Healthy' else '⚠️'} "
                        f"{info['crop']} — {info['disease']}"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"**Severity:** <span style='color:{sev_color};font-weight:600;'>"
                          f"{info['severity']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Description:** {info['description']}")
                st.markdown(f"**Symptoms:** {info['symptoms']}")
            with c2:
                st.markdown(f"**💊 Treatment:** {info['treatment']}")
                st.markdown(f"**🛡️ Prevention:** {info['prevention']}")

    st.markdown(f"<p style='color:#8b949e; text-align:center; margin-top:1rem;'>"
               f"Total: {len(DISEASE_INFO)} diseases across {len(crops)} crops</p>",
               unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Page: About
# ──────────────────────────────────────────────
elif page == "ℹ️ About":
    st.markdown("""
    <div class="hero-container" style="padding: 2rem;">
        <div class="hero-title" style="font-size: 2rem;">ℹ️ About This Project</div>
        <div class="hero-subtitle">AI-Based Crop Disease Detection Using Deep Learning (CNN)</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Project Objective")
    st.markdown("""
    Farmers face significant crop losses due to late disease identification. Manual inspection is
    slow and inaccurate. This project uses **Deep Learning (CNN)** to automatically identify
    crop diseases from leaf images, providing instant results with treatment recommendations.
    """)

    st.markdown("### 🧠 How the AI Works")
    st.markdown("""
    Our system uses a **Convolutional Neural Network (CNN)** — a type of artificial intelligence
    that can recognize patterns in images, similar to how a doctor identifies diseases by looking
    at symptoms.

    **In simple terms:**
    1. The AI looks at thousands of leaf photos during training
    2. It learns to recognize patterns — spots, color changes, texture differences
    3. When you upload a new leaf photo, it compares it to what it learned
    4. It tells you what disease (if any) it found and how confident it is
    """)

    st.markdown("### 🏗️ CNN Architecture")
    arch_data = {
        "Layer": ["Conv2D (32 filters)", "Conv2D (64 filters)", "Conv2D (128 filters)",
                  "Conv2D (256 filters)", "Global Avg Pooling", "Dense (512)", "Dense (256)",
                  "Output (38 classes)"],
        "Purpose": ["Detects basic patterns (edges, colors)", "Detects shapes and textures",
                    "Detects complex features (spots, lesions)", "Detects disease-specific patterns",
                    "Summarizes all features", "Makes decision connections",
                    "Refines the decision", "Final disease prediction"]
    }
    st.table(arch_data)

    st.markdown("### 🛠️ Technology Stack")
    tech_data = {
        "Component": ["Language", "Deep Learning", "Image Processing", "Visualization", "Web App", "Dataset"],
        "Technology": ["Python 3.13", "TensorFlow / Keras", "OpenCV", "Matplotlib", "Streamlit", "PlantVillage (38 classes)"]
    }
    st.table(tech_data)

    st.markdown("### 📊 Model Performance")
    st.info("Train the model using `python scripts/train_model.py` and check `reports/` folder for accuracy and loss graphs.")

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #8b949e; padding: 1rem;">
        <p>AI-Based Crop Disease Detection System</p>
        <p style="font-size: 0.8rem;">Built with TensorFlow, Keras & Streamlit</p>
    </div>
    """, unsafe_allow_html=True)
