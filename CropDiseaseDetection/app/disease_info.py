"""
Disease Information Database — All 38 PlantVillage Classes
"""

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "crop": "Apple", "disease": "Apple Scab", "severity": "Medium",
        "description": "Fungal disease caused by Venturia inaequalis affecting apple leaves and fruit.",
        "symptoms": "Dark, olive-green spots on leaves that turn brown and velvety. Leaves may curl and drop early.",
        "treatment": "Apply fungicides like Captan or Mancozeb during spring. Remove fallen leaves. Prune for air circulation.",
        "prevention": "Plant resistant varieties. Ensure good air circulation. Clean up fallen leaves in autumn."
    },
    "Apple___Black_rot": {
        "crop": "Apple", "disease": "Black Rot", "severity": "High",
        "description": "Caused by fungus Botryosphaeria obtusa. Affects leaves, fruit, and bark.",
        "symptoms": "Purple spots on leaves expanding with brown centers. Fruit develops brown-black rot.",
        "treatment": "Remove infected fruit and cankers. Apply Captan or Thiophanate-methyl fungicide.",
        "prevention": "Prune dead wood. Remove mummified fruit. Maintain tree vigor with proper fertilization."
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple", "disease": "Cedar Apple Rust", "severity": "Medium",
        "description": "Fungal disease caused by Gymnosporangium juniperi-virginianae requiring two hosts.",
        "symptoms": "Bright orange-yellow spots on upper leaf surface. Tube-like structures on underside.",
        "treatment": "Apply Myclobutanil fungicide in spring. Remove nearby cedar/juniper trees if possible.",
        "prevention": "Plant resistant apple varieties. Avoid planting near cedar trees."
    },
    "Apple___healthy": {
        "crop": "Apple", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms. Leaf appears green and normal.",
        "treatment": "No treatment needed. Continue regular care and monitoring.",
        "prevention": "Maintain good watering schedule. Regular pruning. Monitor for early signs of disease."
    },
    "Blueberry___healthy": {
        "crop": "Blueberry", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed. Continue regular care.",
        "prevention": "Maintain acidic soil pH (4.5-5.5). Mulch around plants. Water regularly."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry", "disease": "Powdery Mildew", "severity": "Medium",
        "description": "Caused by Podosphaera clandestina. Common fungal disease on cherry trees.",
        "symptoms": "White powdery coating on leaves. Leaves may curl and become distorted.",
        "treatment": "Apply sulfur-based or potassium bicarbonate fungicide. Neem oil can also help.",
        "prevention": "Ensure good air circulation. Avoid overhead watering. Plant in sunny locations."
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Regular pruning. Adequate spacing between trees."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn", "disease": "Gray Leaf Spot", "severity": "High",
        "description": "Caused by Cercospora zeae-maydis. Major disease in corn production.",
        "symptoms": "Rectangular gray-brown lesions on leaves running parallel to veins.",
        "treatment": "Apply foliar fungicides (Azoxystrobin). Use resistant hybrids.",
        "prevention": "Crop rotation. Tillage to bury infected residue. Plant resistant varieties."
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn", "disease": "Common Rust", "severity": "Medium",
        "description": "Caused by Puccinia sorghi. Common fungal disease in corn.",
        "symptoms": "Small reddish-brown pustules on both leaf surfaces. Pustules may turn dark brown.",
        "treatment": "Apply fungicides like Mancozeb or Propiconazole if severe.",
        "prevention": "Plant resistant hybrids. Early planting to avoid peak spore periods."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn", "disease": "Northern Leaf Blight", "severity": "High",
        "description": "Caused by Exserohilum turcicum. Can cause significant yield loss.",
        "symptoms": "Long, elliptical gray-green lesions (1-6 inches) on leaves.",
        "treatment": "Apply foliar fungicides at first sign. Use resistant hybrids.",
        "prevention": "Crop rotation. Tillage management. Plant resistant varieties."
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Proper spacing. Adequate nutrition. Regular monitoring."
    },
    "Grape___Black_rot": {
        "crop": "Grape", "disease": "Black Rot", "severity": "High",
        "description": "Caused by Guignardia bidwellii. One of the most serious grape diseases.",
        "symptoms": "Small brown circular lesions on leaves. Fruit turns brown then black and shrivels.",
        "treatment": "Apply Mancozeb or Myclobutanil fungicide before bloom. Remove mummified berries.",
        "prevention": "Sanitation — remove infected material. Good canopy management."
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape", "disease": "Esca (Black Measles)", "severity": "High",
        "description": "Complex fungal disease caused by multiple fungi. Affects older vines.",
        "symptoms": "Tiger-stripe pattern on leaves. Dark spots on berries. Sudden vine collapse.",
        "treatment": "No effective chemical cure. Remove severely affected vines. Apply wound protectants.",
        "prevention": "Avoid large pruning wounds. Protect wounds with fungicide paste."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape", "disease": "Leaf Blight", "severity": "Medium",
        "description": "Caused by Isariopsis leaf spot fungus affecting grape leaves.",
        "symptoms": "Dark brown spots with yellow halos on leaves. Premature defoliation.",
        "treatment": "Apply Bordeaux mixture or copper-based fungicides.",
        "prevention": "Good air circulation. Remove infected leaves. Proper vine training."
    },
    "Grape___healthy": {
        "crop": "Grape", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Proper canopy management. Regular monitoring. Balanced fertilization."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange", "disease": "Citrus Greening (HLB)", "severity": "High",
        "description": "Bacterial disease spread by Asian citrus psyllid. Most devastating citrus disease.",
        "symptoms": "Blotchy yellow mottling on leaves. Lopsided, bitter fruit. Tree decline.",
        "treatment": "No cure exists. Remove infected trees. Control psyllid population with insecticides.",
        "prevention": "Use certified disease-free nursery stock. Monitor for psyllid insects. Remove infected trees."
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach", "disease": "Bacterial Spot", "severity": "Medium",
        "description": "Caused by Xanthomonas arboricola. Common in warm, humid climates.",
        "symptoms": "Small dark spots on leaves. Spots may fall out creating shot-hole appearance.",
        "treatment": "Apply copper-based bactericides. Oxytetracycline sprays during bloom.",
        "prevention": "Plant resistant varieties. Avoid overhead irrigation. Proper tree spacing."
    },
    "Peach___healthy": {
        "crop": "Peach", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Regular pruning. Proper watering. Annual dormant spray."
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper", "disease": "Bacterial Spot", "severity": "High",
        "description": "Caused by Xanthomonas bacteria. Major disease in peppers.",
        "symptoms": "Small, dark, water-soaked spots on leaves. Spots may merge causing leaf drop.",
        "treatment": "Apply copper-based sprays. Remove infected plants. Use certified seeds.",
        "prevention": "Use disease-free seeds. Crop rotation (2-3 years). Avoid overhead watering."
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Regular watering. Balanced fertilizer. Mulching."
    },
    "Potato___Early_blight": {
        "crop": "Potato", "disease": "Early Blight", "severity": "Medium",
        "description": "Caused by Alternaria solani. Common in warm, humid conditions.",
        "symptoms": "Dark brown concentric rings (target-shaped spots) on older leaves.",
        "treatment": "Apply Chlorothalonil or Mancozeb fungicide. Remove infected leaves.",
        "prevention": "Crop rotation. Adequate spacing. Avoid overhead irrigation. Use certified seed."
    },
    "Potato___Late_blight": {
        "crop": "Potato", "disease": "Late Blight", "severity": "High",
        "description": "Caused by Phytophthora infestans. Historically devastating disease (Irish Potato Famine).",
        "symptoms": "Water-soaked dark spots that rapidly enlarge. White mold on underside in humid conditions.",
        "treatment": "Apply Metalaxyl or Chlorothalonil immediately. Destroy heavily infected plants.",
        "prevention": "Plant resistant varieties. Avoid wet conditions. Destroy volunteer plants."
    },
    "Potato___healthy": {
        "crop": "Potato", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Proper hilling. Balanced fertilization. Adequate spacing."
    },
    "Raspberry___healthy": {
        "crop": "Raspberry", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Regular pruning. Good drainage. Proper spacing."
    },
    "Soybean___healthy": {
        "crop": "Soybean", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Crop rotation. Proper seeding rate. Monitor for pests."
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash", "disease": "Powdery Mildew", "severity": "Medium",
        "description": "Caused by Podosphaera xanthii. Very common on squash and cucurbits.",
        "symptoms": "White powdery spots on leaf surfaces. Leaves yellow and die.",
        "treatment": "Apply sulfur or potassium bicarbonate. Neem oil for organic treatment.",
        "prevention": "Plant resistant varieties. Ensure air circulation. Avoid overhead watering."
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry", "disease": "Leaf Scorch", "severity": "Medium",
        "description": "Caused by Diplocarpon earlianum. Common fungal disease.",
        "symptoms": "Small dark purple spots that enlarge. Leaf margins appear scorched.",
        "treatment": "Apply Captan or copper fungicides. Remove badly infected leaves.",
        "prevention": "Use resistant varieties. Avoid overhead irrigation. Proper plant spacing."
    },
    "Strawberry___healthy": {
        "crop": "Strawberry", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed.",
        "prevention": "Mulching. Proper drainage. Renovate beds annually."
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato", "disease": "Bacterial Spot", "severity": "High",
        "description": "Caused by Xanthomonas species. Thrives in warm, wet conditions.",
        "symptoms": "Small dark raised spots on leaves and fruit. Leaves yellow and drop.",
        "treatment": "Copper-based bactericides. Remove infected plants.",
        "prevention": "Use pathogen-free seed. Crop rotation. Avoid working with wet plants."
    },
    "Tomato___Early_blight": {
        "crop": "Tomato", "disease": "Early Blight", "severity": "Medium",
        "description": "Caused by Alternaria solani. One of the most common tomato diseases.",
        "symptoms": "Dark concentric ring spots (bull's-eye pattern) on lower leaves first.",
        "treatment": "Apply Chlorothalonil or copper-based fungicide. Remove infected lower leaves.",
        "prevention": "Mulch around plants. Water at base. Stake plants. Crop rotation."
    },
    "Tomato___Late_blight": {
        "crop": "Tomato", "disease": "Late Blight", "severity": "High",
        "description": "Caused by Phytophthora infestans. Rapid spread in cool, wet conditions.",
        "symptoms": "Large, dark, water-soaked lesions on leaves and stems. White mold underneath.",
        "treatment": "Apply Chlorothalonil or Mancozeb immediately. Destroy severely infected plants.",
        "prevention": "Use resistant varieties. Proper spacing. Avoid overhead watering."
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato", "disease": "Leaf Mold", "severity": "Medium",
        "description": "Caused by Passalora fulva (Cladosporium fulvum). Common in greenhouses.",
        "symptoms": "Pale yellow spots on upper leaf surface. Olive-green mold on underside.",
        "treatment": "Improve ventilation. Apply Mancozeb or copper fungicide.",
        "prevention": "Reduce humidity. Good air circulation. Avoid leaf wetting."
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato", "disease": "Septoria Leaf Spot", "severity": "Medium",
        "description": "Caused by Septoria lycopersici. Very common tomato disease.",
        "symptoms": "Many small circular spots with dark borders and gray centers on lower leaves.",
        "treatment": "Apply Chlorothalonil or copper fungicide. Remove infected lower leaves.",
        "prevention": "Crop rotation. Mulching. Avoid overhead watering. Stake plants."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato", "disease": "Spider Mites", "severity": "Medium",
        "description": "Infestation by Tetranychus urticae. Tiny pests that suck plant sap.",
        "symptoms": "Tiny yellow dots on leaves. Fine webbing on undersides. Leaves bronze and dry.",
        "treatment": "Spray with insecticidal soap or neem oil. Use miticides for severe cases.",
        "prevention": "Regular inspection. Maintain humidity. Introduce predatory mites."
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato", "disease": "Target Spot", "severity": "Medium",
        "description": "Caused by Corynespora cassiicola. Affects leaves, stems, and fruit.",
        "symptoms": "Brown spots with concentric rings (target pattern). Leaves may drop.",
        "treatment": "Apply Chlorothalonil or Azoxystrobin fungicide.",
        "prevention": "Good air circulation. Crop rotation. Remove plant debris."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato", "disease": "Yellow Leaf Curl Virus", "severity": "High",
        "description": "Viral disease spread by whiteflies. Devastating to tomato crops.",
        "symptoms": "Leaves curl upward and turn yellow. Stunted growth. Poor fruit set.",
        "treatment": "No cure. Remove infected plants. Control whiteflies with insecticides.",
        "prevention": "Use resistant varieties. Control whitefly population. Use reflective mulches."
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato", "disease": "Mosaic Virus", "severity": "High",
        "description": "Caused by Tomato mosaic virus (ToMV). Highly contagious.",
        "symptoms": "Mottled light and dark green mosaic pattern on leaves. Leaf distortion.",
        "treatment": "No cure. Remove and destroy infected plants. Disinfect tools.",
        "prevention": "Use resistant varieties. Wash hands before handling. Disinfect tools."
    },
    "Tomato___healthy": {
        "crop": "Tomato", "disease": "Healthy", "severity": "Healthy",
        "description": "The leaf is healthy with no signs of disease.",
        "symptoms": "No disease symptoms detected.",
        "treatment": "No treatment needed. Continue regular care.",
        "prevention": "Consistent watering. Balanced fertilizer. Regular monitoring."
    }
}


def get_disease_info(class_name):
    """Get disease information for a predicted class."""
    return DISEASE_INFO.get(class_name, {
        "crop": "Unknown", "disease": "Unknown", "severity": "Unknown",
        "description": "Information not available for this class.",
        "symptoms": "N/A", "treatment": "Consult a local agricultural expert.",
        "prevention": "Regular crop monitoring recommended."
    })


def get_readable_name(class_name):
    """Convert class folder name to readable display name."""
    info = get_disease_info(class_name)
    return f"{info['crop']} — {info['disease']}"


def get_severity_color(severity):
    """Return color for severity level."""
    colors = {
        "Healthy": "#4CAF50",
        "Low": "#8BC34A",
        "Medium": "#FF9800",
        "High": "#F44336"
    }
    return colors.get(severity, "#9E9E9E")
