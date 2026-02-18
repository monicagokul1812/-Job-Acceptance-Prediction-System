import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Job Acceptance Dashboard", layout="wide")

# Load Data
df = pd.read_csv("feature_engineered_data.csv")

# Interview Average
df['interview_average'] = (
    df['technical_score'] +
    df['aptitude_score'] +
    df['communication_score']
) / 3

# KPIs
total_candidates = len(df)
placement_rate = df['status'].mean() * 100
avg_interview_score = df['interview_average'].mean()
avg_skills_match = df['skills_match_percentage'].mean()
offer_dropout_rate = (1 - df['status'].mean()) * 100

if 'placement_probability_score' in df.columns:
    high_risk_percent = (
        len(df[df['placement_probability_score'] < 50]) / len(df)
    ) * 100
else:
    high_risk_percent = 0

# Title
st.title("📊 Job Acceptance Prediction Dashboard")
st.markdown("---")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Candidates", total_candidates)
col2.metric("Placement Rate (%)", round(placement_rate, 2))
col3.metric("Offer Dropout Rate (%)", round(offer_dropout_rate, 2))
col4.metric("High Risk Candidates (%)", round(high_risk_percent, 2))

col5, col6 = st.columns(2)
col5.metric("Average Interview Score", round(avg_interview_score, 2))
col6.metric("Average Skills Match (%)", round(avg_skills_match, 2))

st.markdown("---")

# Placement Distribution
st.subheader("📌 Placement Distribution")

placement_counts = df['status'].value_counts()

st.bar_chart(placement_counts)

# Interview Score vs Placement
st.subheader("📌 Interview Score vs Placement")

fig, ax = plt.subplots()
sns.boxplot(x='status', y='interview_average', data=df, ax=ax)
st.pyplot(fig)

# Skills Match vs Placement
st.subheader("📌 Skills Match vs Placement")

fig2, ax2 = plt.subplots()
sns.boxplot(x='status', y='skills_match_percentage', data=df, ax=ax2)
st.pyplot(fig2)

# Risk Distribution
if 'placement_probability_score' in df.columns:
    st.subheader("📌 Risk Distribution")

    fig3, ax3 = plt.subplots()
    sns.histplot(df['placement_probability_score'], bins=20, kde=True, ax=ax3)
    st.pyplot(fig3)

# Feature Importance (Optional)
if 'technical_score' in df.columns:
    st.subheader("📌 Top Placement Drivers")

    corr = df.corr(numeric_only=True)['status'].sort_values(ascending=False)[1:10]

    fig4, ax4 = plt.subplots()
    corr.plot(kind='bar', ax=ax4)
    st.pyplot(fig4)

    #python -m streamlit run app.py