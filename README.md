# 🌐 LinguaTranslate – Multilingual Language Translation

**A multilingual text translation application powered by the mBART-50 pretrained transformer model.**

## 🚀 Live Application

👉 https://multilingual-translator-3kzathsjfh3vtfgys8xn3m.streamlit.app/

## 📌 About the Project

LinguaTranslate is a multilingual machine translation application developed using the mBART-50 many-to-many multilingual translation model. It allows users to translate text between supported languages through a simple and user-friendly web interface.

## ✨ Features

- Multilingual text translation
- Source and target language selection
- Transformer-based translation using mBART-50
- Interactive Streamlit interface
- Cloud deployment for public access
- Translation quality and performance evaluation

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| mBART-50 | Machine translation model |
| Hugging Face Transformers | Model integration |
| Google Colab | Model implementation and testing |
| Streamlit | Web application |
| GitHub | Source code management |
| Streamlit Community Cloud | Application deployment |
| SacreBLEU | BLEU evaluation |
| chrF | Character-level translation evaluation |

## 🧠 Model Information

- **Model:** `facebook/mbart-large-50-many-to-many-mmt`
- **Architecture:** Multilingual sequence-to-sequence Transformer
- **Model Type:** Many-to-many neural machine translation

## 📊 Performance Evaluation

The project evaluates translation quality and computational performance using:

- BLEU Score
- chrF Score
- Average Translation Time
- 95th Percentile Latency (P95)
- Throughput

Evaluation is performed in Google Colab using reference translations.

## ⚙️ Project Workflow

1. Load the pretrained mBART-50 model.
2. Initialize the tokenizer and model.
3. Implement multilingual translation.
4. Develop the Streamlit application.
5. Push project files to GitHub.
6. Deploy the application using Streamlit Community Cloud.
7. Evaluate translation quality and performance.

## ▶️ Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🔮 Future Enhancements

- Expand translation evaluation using larger multilingual datasets.
- Improve translation quality through systematic benchmarking.
- Add support for additional language pairs.
- Explore translation history and document translation.

## 👩‍💻 Project

**Project Name:** LinguaTranslate  
**Domain:** Artificial Intelligence and Machine Learning  
**Model:** mBART-50  
**Application:** Streamlit

---

⭐ If you find this project interesting, feel free to explore the live application!
