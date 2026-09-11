import streamlit as st
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
def listen_bg():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("बोलिए, सुन रहे हैं...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="hi-IN")
            return text
        except:
            return ""

st.set_page_config(page_title="Gram-Setu Advanced", page_icon="🌾", layout="centered")

st.title("🌾 ग्राम-सेतु (Gram-Setu AI)")
st.subheader("Advanced Voice-Controlled Smart Farming & Tech Support Platform")

# Session state configuration
if 'members' not in st.session_state:
    st.session_state.members = {}

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for Navigation & Multi-access
st.sidebar.markdown("### 🌐 कम्युनिटी और एक्सेस")
access_mode = st.sidebar.radio("मोड चुनें:", ["मुख्य ऐप (Main App)", "नया सदस्य/मोबाइल नंबर जोड़ें"])

if access_mode == "नया सदस्य/मोबाइल नंबर जोड़ें":
    st.markdown("#### ➕ परिवार के सदस्य को जोड़ें (All-In Access)")
    new_name = st.text_input("सदस्य का नाम:")
    new_phone = st.text_input("मोबाइल नंबर:")
    
    if st.button("सदस्य को जोड़ें"):
        if new_name and new_phone:
            st.session_state.members[new_phone] = new_name
            st.success(f"🎉 {new_name} ({new_phone}) सफलतापूर्वक जुड़ गए हैं।")
        else:
            st.warning("कृपया नाम और मोबाइल नंबर दोनों भरें।")
else:
    role = st.sidebar.selectbox("अपनी भूमिका चुनें (Role)", ["किसान (Farmer)", "आईटीआई मैकेनिक/छात्र (ITAI Technician)"])

    if role == "किसान (Farmer)":
        st.markdown("### 🗣️ Gemini AI वॉयस और विजुअल कमांड सेंटर")
        
        # Voice Assistant Simulator Toggle
        voice_mode = st.checkbox("🎙️ वॉयस कमांड मोड चालू करें (Voice-Base Control)")
        if voice_mode:
            st.info("🎤 'सुन रहा हूँ...' बोलिए या नीचे दिए गए विकल्पों का उपयोग करें:")
            spoken_input = st.text_input("वॉयस टेक्स्ट सिमुलेशन (Voice Input):", placeholder="जैसे: 'मेरी फसल में कीड़ा लग गया है' या 'पंप खराब है'")
            if spoken_input:
                st.write(f"🔊 AI कमांड समझी गई: **{spoken_input}**")

        lang = st.selectbox("भाषा चुनें", ["भोजपुरी", "अवधी", "बुंदेली", "हिंदी"])
        
        query_type = st.radio("आप क्या करना चाहते हैं?", [
            "3-स्टेप वेरीफाई और लाइव कैमरा फसल जाँच (Advanced AI Crop Scan)", 
            "खेत का मोटर/पंप रिपेयर सपोर्ट (Repair Support)", 
            "अपनी फसल का सही दाम (Crop Pricing & Escrow)", 
            "शहर से बाहर रहकर खेत का स्टेटस (Remote Farm Status via WhatsApp)"
        ])
        
        if query_type == "3-स्टेप वेरीफाई और लाइव कैमरा फसल जाँच (Advanced AI Crop Scan)":
            st.markdown("#### 📸 लाइव कैमरा स्कैन और एआई हेल्थ रिपोर्ट")
            st.info("चरण 1: जमीन रिकॉर्ड आईडी दर्ज करें | चरण 2: फसल की फोटो अपलोड करें | चरण 3: एआई हेल्थ रिपोर्ट पाएं।")
            
            f_id = st.text_input("खेत/खाता संख्या दर्ज करें:")
            uploaded_image = st.file_uploader("खेत या फसल की लाइव फोटो अपलोड करें (Live Camera Scan):", type=["jpg", "png", "jpeg"])
            
            if st.button("एआई हेल्थ रिपोर्ट जनरेट करें"):
                if f_id and uploaded_image:
                    st.success("✅ 3-स्टेप वेरिफिकेशन सफल!")
                    st.markdown("---")
                    st.markdown("### 🧬 **AI-Generated Crop Health Report**")
                    st.markdown(
                        f"* **खेत आईडी (Farm ID):** {f_id}\n"
                        f"* **जमीन ओनरशिप:** वेरीफाइड (Verified)\n"
                        f"* **फसल स्वास्थ्य स्थिति:** **स्वस्थ (85% Healthy)** - नाइट्रोजन की हल्की कमी महसूस हो रही है।\n"
                        f"* **कीटनाशक सुझाव:** नीम आधारित जैविक कीटनाशक का छिड़काव करें।\n"
                        f"* **सिंचाई सलाह:** अगले 48 घंटों में हल्की सिंचाई की आवश्यकता है।"
                    )
                else:
                    st.warning("कृपया खेत आईडी और फोटो दोनों प्रदान करें।")

        elif query_type == "खेत का मोटर/पंप रिपेयर सपोर्ट (Repair Support)":
            location = st.text_input("अपना गाँव/क्षेत्र दर्ज करें:")
            if st.button("सहायता के लिए अनुरोध भेजें"):
                if location:
                    st.success(f"✅ आपका अनुरोध '{location}' के पास के 5 किमी दायरे में मौजूद आईटीआई मैकेनिक को भेज दिया गया है!")
                    st.info("मैकेनिक कुछ ही देर में आपसे संपर्क करेगा।")
                else:
                    st.warning("कृपया अपना स्थान दर्ज करें।")
                    
        elif query_type == "अपनी फसल का सही दाम (Crop Pricing & Escrow)":
            crop_name = st.selectbox("फसल का नाम चुनें:", ["गेहूं", "धान", "आलू", "सरसों"])
            st.info(f"📊 वर्तमान मंडी भाव ({crop_name}): ₹2,250 प्रति क्विंटल (सीधे आपके खाते में एस्क्रो पेमेंट उपलब्ध)")

        elif query_type == "शहर से बाहर रहकर खेत का स्टेटस (Remote Farm Status via WhatsApp)":
            st.markdown("#### 📱 व्हाट्सएप आधारित रिमोट खेत स्टेटस वेरिफिकेशन")
            farmer_phone = st.text_input("अपना रजिस्टर्ड मोबाइल नंबर दर्ज करें:")
            farm_id = st.text_input("खेत/जमीन का खाता संख्या दर्ज करें:")
            
            if st.button("व्हाটসঅ্যাপ पर स्टेटस मंगाएं"):
                if farmer_phone and farm_id:
                    st.success(f"💬 आपके नंबर ({farmer_phone}) पर व्हाट्सएप मैसेज भेज दिया गया है!")
                    st.info(f"🟢 **Gram-Setu Update:** खेत (ID: {farm_id}) का 3-स्टेप वेरिफिकेशन सफल। फसल सुरक्षित है!")
                else:
                    st.warning("कृपया सभी विवरण भरें।")

    else:
        st.markdown("### 🔧 आईटीआई छात्र/मैकेनिक डैशबोर्ड")
        tech_name = st.text_input("मैकेनिक का नाम:")
        skills = st.multiselect("विशेषज्ञता:", ["वाटर पंप रिपेयर", "सोलर पैनल फिक्सिंग", "रोबोटिक फार्मिंग टूल्स"])
        
        if st.button("उपलब्धता दर्ज करें"):
            if tech_name:
                st.success(f"🎉 स्वागत है {tech_name}! आपका हाइपर-लोकल नेटवर्क डेटाबेस में पंजीकरण सफल रहा।")
            else:
                st.warning("कृपया अपना नाम दर्ज करें।")
