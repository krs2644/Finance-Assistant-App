# 💬 Finance QA Assistant

An interactive web application built with Streamlit and Hugging Face Transformers, designed to answer finance-related questions based on provided text context.

---

## ✨ Overview

This project provides a simple yet powerful tool for extracting specific information from financial documents or articles. Users can input a block of text (the "context") and then ask questions related to that text. The application leverages a pre-trained Natural Language Processing (NLP) model to find the most relevant answer within the given context.

---

## 🚀 Features

- **Interactive Web Interface:** User-friendly front-end developed with Streamlit.
- **Question Answering Capabilities:** Utilizes a fine-tuned Hugging Face Transformers model (`distilbert-base-cased-distilled-squad`) for efficient and accurate answer extraction.
- **Dynamic Input:** Easily provide text context and formulate questions through dedicated input fields.
- **Performance Optimized:** Model loading is cached using `st.cache_resource` for faster subsequent interactions.
- **Input Validation:** Ensures both context and question are provided before processing.

---

## 🛠️ Technologies Used

- **Python:** The core programming language.
- **Streamlit:** For building the interactive web application.
- **Hugging Face Transformers:** For the underlying Question Answering NLP model.
- **Accelerate:** (Recommended) A companion library for Hugging Face Transformers, aiding in efficient model loading and device management.

---

## 🏁 Getting Started

Follow these steps to get a local copy of the project up and running.

### Prerequisites

Ensure you have **Python 3.8+** installed.

### Installation

Clone the repository (if applicable):

```bash
git clone https://github.com/your-username/finance-qa-assistant.git
cd finance-qa-assistant
```

> **Note:** Replace `your-username` and `finance-qa-assistant` with your actual GitHub details if you create a repo.

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install streamlit transformers accelerate
```

---

## 🏃 How to Run

After installing the dependencies, run the Streamlit application from your terminal:

```bash
streamlit run app.py
```

This command will open the application in your default web browser (usually at [http://localhost:8501](http://localhost:8501)).

---

## 💡 Usage

1. **Enter Context:** Paste or type your financial text (e.g., an earnings report, market analysis) into the "Enter the context" text area.
2. **Enter Question:** Type your question related to the context into the "Enter your question" input field.
3. **Get Answer:** Click the "Get Answer" button. The application will process your request and display the extracted answer.

---

## 🤝 Contributing

Feel free to fork this repository, open issues, or submit pull requests to improve the project!

---

## 📄 License

This project is open source and available under the MIT License.
