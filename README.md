# Text Summarizer

## Overview
The **Text Summarizer** project is a robust web application designed to generate concise summaries of lengthy text inputs. It utilizes **Streamlit** for the frontend, providing an interactive and user-friendly interface, and **FastAPI** for the backend, ensuring efficient and scalable API services. The summarization functionality is powered by state-of-the-art transformer-based language models.

---

## Features
- **Text Summarization**: Generates summaries for long pieces of text using advanced transformer models.
- **Interactive Interface**: Built with Streamlit for a seamless user experience.
- **Efficient Backend**: FastAPI ensures rapid response times and scalability.
- **Customizable**: Easily switch or update the underlying summarization model.
- **Training Capability**: Trigger model training directly from the frontend (optional).

---

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/) - For the interactive user interface.
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) - For handling API requests.
- **Model**: Transformer-based models from [Hugging Face Transformers](https://huggingface.co/docs/transformers/).
- **Python**: The core programming language for all components.

---

## Installation

1. Clone the repository:
2. Create and activate a virtual environment:
3. Install dependencies:
   
### 1.Run the FastAPI backend:
The backend will be available at `http://127.0.0.1:8080`.

### 2. Start the Frontend
Run the Streamlit frontend:

Access the frontend at `http://localhost:8501`.

---

## API Endpoints

- **`GET /`**: Redirects to the FastAPI docs.
- **`POST /predict`**: Accepts text input and returns a summarized version.
- **`GET /train`**: (Optional) Triggers the model training process.

---

## Example Workflow

1. Open the Streamlit app.
2. Paste or type text into the input box.
3. Click "Summarize" to generate the summary.
4. View and interact with the summarized output.

---




