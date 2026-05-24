# agents.py
from langchain_community.llms import Ollama
from langgraph.graph import StateGraph, END
from typing import TypedDict

llm = Ollama(model="llama3")

class AgentState(TypedDict):
    question: str
    data_summary: str
    anomalies: str
    insight: str

def planner_agent(state: AgentState):
    """Decides what to analyse"""
    prompt = f"""
    User question: {state['question']}
    You are a data analyst. Summarise what needs to be investigated.
    Be concise.
    """
    response = llm.invoke(prompt)
    return {"data_summary": response}

def anomaly_agent(state: AgentState):
    """Runs anomaly detection and summarises findings"""
    # Load and analyse data
    import pandas as pd
    from anomaly import detect_anomalies
    
    df = pd.read_csv("data/timeseries.csv")
    df = detect_anomalies(df)
    anomaly_count = df['is_anomaly'].sum()
    anomaly_times = df[df['is_anomaly']]['timestamp'].tolist()[:5]
    
    summary = f"Found {anomaly_count} anomalies. Top timestamps: {anomaly_times}"
    return {"anomalies": summary}

def insight_agent(state: AgentState):
    """Generates natural language RCA"""
    prompt = f"""
    Question: {state['question']}
    Analysis: {state['data_summary']}
    Anomalies found: {state['anomalies']}
    
    Write a crisp root cause analysis and recommended action in 3-4 lines.
    """
    response = llm.invoke(prompt)
    return {"insight": response}

# Build the graph
def build_graph():
    graph = StateGraph(AgentState)
    
    graph.add_node("planner", planner_agent)
    graph.add_node("anomaly_detector", anomaly_agent)
    graph.add_node("insight_generator", insight_agent)
    
    graph.set_entry_point("planner")
    graph.add_edge("planner", "anomaly_detector")
    graph.add_edge("anomaly_detector", "insight_generator")
    graph.add_edge("insight_generator", END)
    
    return graph.compile()