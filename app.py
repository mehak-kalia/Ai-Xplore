# app.py
import streamlit as st
import plotly.express as px
import pandas as pd
from anomaly import detect_anomalies
from agents import build_graph
from memory import save_to_memory, retrieve_similar

st.set_page_config(page_title="AnalyticsAgent", layout="wide")
st.title("AnalyticsAgent — Agentic AI for Autonomous Data Analysis")

# Load data
df = pd.read_csv("data/timeseries.csv")
df = detect_anomalies(df)

# Chart
fig = px.line(df, x='timestamp', y='value', title='Time Series with Anomalies')
anomalies = df[df['is_anomaly']]
fig.add_scatter(x=anomalies['timestamp'], y=anomalies['value'],
                mode='markers', marker=dict(color='red', size=8),
                name='Anomaly')
st.plotly_chart(fig, use_container_width=True)

# Query input
question = st.text_input("Ask the agent:", 
                          placeholder="Why did this metric spike on Nov 3?")

if st.button("Analyse") and question:
    # Check memory first
    past = retrieve_similar(question)
    if past:
        st.info(f"Similar past analysis found: {past[0][:200]}...")

    # Run agents
    graph = build_graph()
    with st.spinner("Agents working..."):
        result = graph.invoke({"question": question,
                               "data_summary": "",
                               "anomalies": "",
                               "insight": ""})
    
    st.subheader("Root Cause Analysis")
    st.write(result['insight'])
    
    # Save to memory
    save_to_memory(result['insight'])
    st.success("Analysis saved to memory.")