import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Config
st.set_page_config(page_title="TeamSpark AI", page_icon="🚀", layout="wide")

# Load Data
@st.cache_data
def load_data():
    with open("students.json") as f: students = json.load(f)
    with open("events.json") as f: events = json.load(f)
    with open("matches.json") as f: matches = json.load(f)
    return students, events, matches

students, events, matches = load_data()
df_students = pd.DataFrame(students)
df_events = pd.DataFrame(events)
df_matches = pd.DataFrame(matches)

# Header
st.markdown('<h1 style="text-align: center; color: #667eea;">🚀 TeamSpark AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">From "Who do I know?" to "Who fits best?"</p>', unsafe_allow_html=True)

# Sidebar
page = st.sidebar.radio("Navigation", ["📊 Overview", "🎯 AI Match Simulator", "👥 Student Explorer"])

if page == "📊 Overview":
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(students))
    col2.metric("Open Events", len(events))
    col3.metric("Avg Match Score", f"{df_matches['match_score'].mean():.1f}%")
    
    st.markdown("### 🎓 Experience Distribution")
    fig = px.pie(values=df_students["experience_level"].value_counts(), names=df_students["experience_level"].value_counts().index)
    st.plotly_chart(fig)

elif page == "🎯 AI Match Simulator":
    st.markdown("## 🎯 Interactive AI Match Simulator")
    event_names = [e["name"] for e in events]
    selected_name = st.selectbox("Select a Hackathon:", event_names)
    event = next(e for e in events if e["name"] == selected_name)
    
    st.info(f"**Event:** {event['name']} | **Theme:** {event['theme']} | **Roles Needed:** {', '.join(event['required_roles'])}")
    
    # Find matches for this event
    event_matches = df_matches[df_matches["event_id"] == event["event_id"]].sort_values("match_score", ascending=False)
    
    if not event_matches.empty:
        # Radar Chart for Team
        top_users = event_matches.head(3)["user_id"].tolist()
        team_skills = {"Dev": 0, "Design": 0, "AI_ML": 0}
        for uid in top_users:
            s = next(st for st in students if st["user_id"] == uid)
            for k in team_skills: team_skills[k] += s["skill_vector"].get(k, 0)
            
        fig = go.Figure(go.Scatterpolar(r=list(team_skills.values()), theta=list(team_skills.keys()), fill="toself", name="Team Skill"))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 3])), title="Team Skill Coverage")
        st.plotly_chart(fig)
        
        st.markdown("### 🤝 Recommended Teammates")
        for _, m in event_matches.iterrows():
            s = next(st for st in students if st["user_id"] == m["user_id"])
            st.markdown(f"**{s['name']}** - {m['match_score']}% Match | {s['experience_level']} | {', '.join(s['skills'])}")

elif page == "👥 Student Explorer":
    st.dataframe(df_students[["name", "branch", "year", "experience_level", "reliability_score"]])
