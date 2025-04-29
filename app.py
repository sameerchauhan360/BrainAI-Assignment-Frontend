import streamlit as st
import requests
import sys
import os
import json

from questions import questions

with open(os.path.join("recommendations.json")) as f:
    recommendation = json.load(f)


# Create a list of responses for the user to choose from
response_choices = [
    "Not at all",
    "Several days",
    "More than half the days",
    "Nearly every day",
]

# Display the title
st.title("Mental Health Assessment")
st.write("Please answer the following questions:")

# Store the responses
responses_phq9 = []
responses_gad7 = []


# Function to display questions in 2 per row
def display_questions_in_rows(questions_list, prefix):
    responses = []
    for i in range(0, len(questions_list), 2):  # 2 questions at a time
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(questions_list):
                with cols[j]:
                    question = questions_list[i + j]
                    response = st.radio(
                        question["question"],
                        response_choices,
                        index=0,
                        key=f"{prefix}_{question['id']}",
                    )
                    responses.append(response_choices.index(response))
    return responses


# Section for PHQ9 Questions
st.subheader("PHQ9 - Depression Assessment")
responses_phq9 = display_questions_in_rows(questions["PHQ9_QUESTIONS"], "phq9")

# Section for GAD7 Questions
st.subheader("GAD7 - Anxiety Assessment")
responses_gad7 = display_questions_in_rows(questions["GAD7_QUESTIONS"], "gad7")

# Combine both sets of responses
responses = responses_phq9 + responses_gad7

total_questions = len(questions["PHQ9_QUESTIONS"]) + len(questions["GAD7_QUESTIONS"])

# Button to submit the form
if st.button("Submit"):
    if len(responses) == total_questions:

        # Send the responses to the backend API for prediction
        api_url = "https://brainai-project.up.railway.app/api/predict/"
        data = {"responses": responses}

        # Send POST request to backend
        response = requests.post(api_url, json=data)

        if response.status_code == 200:
            result = response.json()
            mhs = result["mental_health_status"]

            st.write(f"**Mental Health Status**: {mhs}")

            if mhs == "Normal":
                st.write("**Recommendations**")
                for i in recommendation[0]["recommendations"]:
                    st.write(f"- {i}")

            elif mhs == "Mild":
                st.write("**Recommendations**")
                for i in recommendation[1]["recommendations"]:
                    st.write(f"- {i}")

            elif mhs == "Moderate":
                st.write("**Recommendations**")
                for i in recommendation[2]["recommendations"]:
                    st.write(f"- {i}")

            elif mhs == "Severe":
                st.write("**Recommendations**")
                for i in recommendation[3]["recommendations"]:
                    st.write(f"- {i}")

        else:
            st.error("Error in prediction, please try again.")
    else:
        st.error("Please answer all the questions.")
