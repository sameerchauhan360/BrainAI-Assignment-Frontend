# 🧠 BrainAI – Mental Health Assessment Frontend (Streamlit)

This is the frontend for the AI-Powered Mental Health Assessment & Recommendation System, built using **Streamlit** as a minimal, clean alternative to React. It provides an interactive web interface to collect user responses to mental health questionnaires and display model predictions and tailored advice.

---

## 💡 Why Streamlit?

While React.js is preferred, Streamlit offers a fast and lightweight solution for prototyping data-driven apps — perfect for this use case where **usability and logic** matter more than complex visuals.

---
## 🌐 Live Demo
### 🔗 Try the App:
👉 [BrainAI Frontend APP](https://brainai-assignment-frontend.onrender.com/)

## 👥 User Flow

1. **Fill the Questionnaire:** Users answer 16 questions (9 for depression, 7 for anxiety), shown 2 at a time for better readability.
2. **Submit Responses:** On clicking "Submit", answers are sent to the backend API hosted on Railway.
3. **View Result & Suggestions:** The user sees the predicted mental health status and evidence-based recommendations from `recommendations.json`.

---

## 🔧 Technologies Used

- **Frontend:** Streamlit (Python)
- **Backend API:** Django + Django REST Framework
- **ML:** Logistic Regression (via backend)
- **Recommendation Source:** Local `recommendations.json` file (evidence-based tips)

---

## 🔗 Backend API

Ensure the Django API is running and accessible at:

```bash
POST https://brainai-project.up.railway.app/api/predict/
```

## Request payload:
```
{
  "responses": [0, 1, 2, ..., 3]  // 16 values
}
```
## Response:
```
{
  "mental_health_status": "Moderate"
}
```
## 🚀 Getting Started
### 1. Clone the repo
```
git clone https://github.com/your-username/brainai-frontend.git
cd brainai-frontend
```
### 2. Create virtual environment and install dependencies
```
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```
### 3. Run the app
```
streamlit run app.py
```
## ✅ Minimalistic UI
This app is intentionally designed to be clean and focused — no unnecessary styles or distractions, just clear functionality for maximum user clarity.
