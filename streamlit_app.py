import streamlit as st
import requests

# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8080"

st.title("Text Summarization App")
st.write("Enter text to summarize and interact with the backend API.")

# Input Text
user_input = st.text_area("Enter Text to Summarize", height=200)

# Predict Button
if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text before summarizing.")
    else:
        with st.spinner("Summarizing your text... Please wait."):
            try:
                # Send text as query parameter
                response = requests.post(
                    f"{BASE_URL}/predict?text={user_input}"
                )
                if response.status_code == 200:
                    summarized_text = response.text  # Expect plain string response
                    st.subheader("Summarized Text:")
                    st.write(summarized_text)
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")


# Train Button with Spinner
if st.button("Train Model"):
    with st.spinner("Training the model... This may take a while."):
        try:
            response = requests.get(f"{BASE_URL}/train")
            if response.status_code == 200:
                st.success(response.text)
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
