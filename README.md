# Summarize-it-AI-Text-Summarizer

A simple and interactive AI-powered text summarization web app built using **Streamlit** and **Hugging Face Inference API**.

🔗 **Live App:** https://summarize-it-ai-text-summarizer.streamlit.app/

---

## ✨ Features

* 🔹 Summarize long text into concise output
* 🔹 Handles long text using hierarchical summarization
* 🔹 Clean and intuitive UI with card-style output
  ---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend/API:** Hugging Face Inference API
* **Language:** Python
* **Libraries:** requests

---

## 🧠 How It Works

1. User inputs long text
2. Text is sent to Hugging Face summarization model
3. For long inputs:

   * Text is split into chunks
   * Each chunk is summarized
   * Final summary is generated from combined results
4. Output is displayed in a styled UI card

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Summarize-it-AI-Text-Summarizer.git
cd Summarize-it-AI-Text-Summarizer
```

---

### 2. Create environment (Anaconda recommended)

```bash
conda create -n summarizer python=3.10
conda activate summarizer
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add your Hugging Face API Key

Create a `.streamlit/secrets.toml` file:

```toml
HF_API_KEY = "your_api_key_here"
```

---

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This app is deployed using **Streamlit Cloud**.

Steps:

1. Push code to GitHub
2. Connect repo to Streamlit Cloud
3. Add secrets (API key)
4. Deploy

---

## ⚠️ Known Limitations

* Hugging Face API may occasionally:

  * Return slow responses
  * Require retries (model loading)
* Very large inputs may increase latency

---

## 🔮 Future Improvements

* 📌 Bullet-point summaries
* 📄 File upload (PDF/Text)
* ⚡ Faster model fallback
* 🎨 Enhanced UI/UX and themes

---

## 💡 Learnings

* Integrated external AI APIs into a web app
* Handled API unreliability and edge cases 
* Implemented hierarchical summarization for long text
* Built and deployed a full-stack AI application

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a PR.

---

## 📬 Contact

If you found this useful, feel free to connect or reach out!

---

⭐ If you like this project, don’t forget to star the repo!
