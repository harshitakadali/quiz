import streamlit as st

# Title
st.title("🧠 Mental Health Awareness Quiz")

# Introduction
st.write("Welcome to the Mental Health Awareness Quiz! Answer the following questions to test your knowledge.")

# Questions
score = 0

# Question 1
q1 = st.radio("1. Which of the following is a common symptom of depression?", 
              ["Increased energy", "Excessive happiness", "Persistent sadness", "Improved concentration"])
if q1 == "Persistent sadness":
    score += 1

# Question 2
q2 = st.radio("2. What does 'anxiety disorder' typically involve?", 
              ["Extreme calmness", "Chronic worry and fear", "Lack of motivation", "Mania"])
if q2 == "Chronic worry and fear":
    score += 1

# Question 3
q3 = st.radio("3. How many hours of sleep is generally recommended for good mental health?", 
              ["3-4 hours", "5-6 hours", "7-9 hours", "10-12 hours"])
if q3 == "7-9 hours":
    score += 1

# Submit Button
if st.button("Submit"):
    st.success(f"✅ You scored {score}/3!")
    if score == 3:
        st.balloons()
        st.write("Excellent! You have great awareness about mental health.")
    elif score == 2:
        st.write("Good job! A little more to learn.")
    else:
        st.write("Keep learning! Mental health is important.")

