
import streamlit as st
import torch
from transformers import (
    MBartForConditionalGeneration,
    MBart50TokenizerFast
)

st.set_page_config(
    page_title="Multilingual Translator",
    page_icon="🌍",
    layout="wide"
)

MODEL_NAME = "facebook/mbart-large-50-many-to-many-mmt"

@st.cache_resource
def load_model():
    tokenizer = MBart50TokenizerFast.from_pretrained(MODEL_NAME)
    model = MBartForConditionalGeneration.from_pretrained(MODEL_NAME)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    model.eval()

    return tokenizer, model, device

tokenizer, model, device = load_model()

languages = {
    "English": "en_XX",
    "French": "fr_XX",
    "German": "de_DE",
    "Spanish": "es_XX",
    "Hindi": "hi_IN",
    "Japanese": "ja_XX",
    "Chinese": "zh_CN",
    "Arabic": "ar_AR",
    "Tamil": "ta_IN",
    "Telugu": "te_IN",
    "Bengali": "bn_IN",
    "Marathi": "mr_IN",
    "Gujarati": "gu_IN",
    "Korean": "ko_KR",
    "Russian": "ru_RU",
    "Portuguese": "pt_XX",
    "Italian": "it_IT",
    "Urdu": "ur_PK",
    "Malayalam": "ml_IN"
}

def translate(text, source, target):
    tokenizer.src_lang = source

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    output = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[target],
        max_new_tokens=200,
        num_beams=5
    )

    return tokenizer.batch_decode(
        output,
        skip_special_tokens=True
    )[0]

st.title("🌍 LinguaTranslate")
st.subheader("AI-Powered Multilingual Translation System")
st.write("Translate text between multiple supported languages.")

col1, col2 = st.columns(2)

with col1:
    source_name = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=0
    )

with col2:
    target_name = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

input_text = st.text_area(
    "Enter text to translate",
    height=150,
    placeholder="Type your sentence here..."
)

if st.button("Translate", type="primary"):
    if not input_text.strip():
        st.warning("Please enter some text.")

    elif source_name == target_name:
        st.warning("Please select different languages.")

    else:
        with st.spinner("Translating..."):
            result = translate(
                input_text,
                languages[source_name],
                languages[target_name]
            )

        st.success("Translation completed!")
        st.subheader("Translated Text")
        st.text_area(
            "Output",
            value=result,
            height=150
        )

        st.download_button(
            "Download Translation",
            result,
            file_name="translation.txt"
        )

st.caption("Powered by Hugging Face mBART-50")
