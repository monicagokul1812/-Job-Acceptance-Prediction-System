import streamlit as st
import pandas as pd

st.set_page_config(page_title="Job Acceptance Dashboard", layout="wide")

df = pd.read_csv("feature_engineered_data.csv")
if 'interview_average' not in df.columns:
    df['interview_average'] = (
        df['technical_score'] +
        df['aptitude_score'] +
        df['communication_score']
    ) / 3
#KPIs
total_candidates = len(df)
placement_rate = df['status'].mean() * 100
job_acceptance_rate = placement_rate
avg_interview_score = df['interview_average'].mean()
avg_skills_match = df['skills_match_percentage'].mean()
offer_dropout_rate = (1 - df['status'].mean()) * 100

if 'placement_probability_score' in df.columns:
    high_risk_percent = (
        len(df[df['placement_probability_score'] < 50]) / len(df)
    ) * 100
else:
    high_risk_percent = 0

st.title("Job Acceptance Prediction Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Candidates", total_candidates)
col2.metric("Placement Rate (%)", round(placement_rate, 2))
col3.metric("Job Acceptance Rate (%)", round(job_acceptance_rate, 2))
col4, col5, col6 = st.columns(3)
col4.metric("Average Interview Score", round(avg_interview_score, 2))
col5.metric("Average Skills Match (%)", round(avg_skills_match, 2))
col6.metric("Offer Dropout Rate (%)", round(offer_dropout_rate, 2))

st.metric("High-Risk Candidate Percentage (%)", round(high_risk_percent, 2))

st.subheader("Placement Distribution")

placement_counts = df['status'].value_counts()

st.bar_chart(placement_counts)


import matplotlib.pyplot as plt
import seaborn as sns

if 'interview_average' in df.columns:
    st.subheader("Interview Score vs Placement")

    fig, ax = plt.subplots()
    sns.boxplot(x='status', y='interview_average', data=df, ax=ax)
    st.pyplot(fig)

if 'skills_match_percentage' in df.columns:
    st.subheader("Skills Match vs Placement")

    fig2, ax2 = plt.subplots()
    sns.boxplot(x='status', y='skills_match_percentage', data=df, ax=ax2)
    st.pyplot(fig2)


if 'placement_probability_score' in df.columns:
    st.subheader("Risk Distribution")

    fig3, ax3 = plt.subplots()
    sns.histplot(df['placement_probability_score'], bins=20, kde=True, ax=ax3)
    st.pyplot(fig3)



    #python -m streamlit run app.py
    #http://localhost:8504/


