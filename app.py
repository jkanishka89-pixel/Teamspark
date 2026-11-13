import streamlit as st
import json
import pandas as pd
import os

# Page Config
st.set_page_config(page_title="TeamSpark AI", page_icon="🚀", layout="wide")

# ============================================
# AUTO-GENERATE DATA IF FILES DON'T EXIST
# ============================================
def ensure_data_files():
    """Create the JSON data files if they don't exist."""
    
    students_data = [
        {"user_id": "USR0001", "name": "Abhishek Singh", "branch": "CS", "year": "3rd", "experience_level": "Intermediate", "skill_vector": {"Dev": 0.85, "Design": 0.46, "AI_ML": 0.83}, "skills": ["Python", "React", "ML"], "interests": ["HealthTech", "Web3"], "personality_type": "Explorer", "reliability_score": 0.6, "hackathons_attended": 7, "availability_hours": 27, "is_mentor": False, "looking_for_team": True},
        {"user_id": "USR0002", "name": "Sneha Kaur", "branch": "Design", "year": "1st", "experience_level": "Beginner", "skill_vector": {"Dev": 0.24, "Design": 0.66, "AI_ML": 0.17}, "skills": ["Figma", "UI/UX"], "interests": ["EdTech", "SocialImpact"], "personality_type": "Mentor", "reliability_score": 0.63, "hackathons_attended": 0, "availability_hours": 15, "is_mentor": False, "looking_for_team": True},
        {"user_id": "USR0003", "name": "Vivek Kaur", "branch": "IT", "year": "4th", "experience_level": "Advanced", "skill_vector": {"Dev": 1.0, "Design": 0.53, "AI_ML": 0.95}, "skills": ["FastAPI", "DSA", "ML"], "interests": ["AgriTech", "EdTech"], "personality_type": "Creative", "reliability_score": 0.63, "hackathons_attended": 12, "availability_hours": 20, "is_mentor": True, "looking_for_team": True},
        {"user_id": "USR0004", "name": "Rohan Das", "branch": "ECE", "year": "3rd", "experience_level": "Intermediate", "skill_vector": {"Dev": 0.7, "Design": 0.3, "AI_ML": 0.4}, "skills": ["C++", "Embedded"], "interests": ["IoT", "Automation"], "personality_type": "Leader", "reliability_score": 0.8, "hackathons_attended": 4, "availability_hours": 10, "is_mentor": False, "looking_for_team": True},
        {"user_id": "USR0005", "name": "Meera Iyer", "branch": "Design", "year": "3rd", "experience_level": "Advanced", "skill_vector": {"Dev": 0.3, "Design": 0.9, "AI_ML": 0.2}, "skills": ["Figma", "UI/UX", "Presentation"], "interests": ["EdTech", "HealthTech"], "personality_type": "Creative", "reliability_score": 0.9, "hackathons_attended": 6, "availability_hours": 18, "is_mentor": True, "looking_for_team": True},
        {"user_id": "USR0006", "name": "Kabir Gupta", "branch": "CS", "year": "2nd", "experience_level": "Novice", "skill_vector": {"Dev": 0.6, "Design": 0.2, "AI_ML": 0.5}, "skills": ["Python", "ML"], "interests": ["FinTech", "EdTech"], "personality_type": "Analyst", "reliability_score": 0.7, "hackathons_attended": 1, "availability_hours": 25, "is_mentor": False, "looking_for_team": True},
        {"user_id": "USR0007", "name": "Sara Reddy", "branch": "MBA", "year": "2nd", "experience_level": "Novice", "skill_vector": {"Dev": 0.2, "Design": 0.5, "AI_ML": 0.1}, "skills": ["Presentation", "Strategy"], "interests": ["SocialImpact", "E-commerce"], "personality_type": "Leader", "reliability_score": 0.85, "hackathons_attended": 2, "availability_hours": 12, "is_mentor": False, "looking_for_team": True},
        {"user_id": "USR0008", "name": "Aarav Patel", "branch": "CS", "year": "1st", "experience_level": "Beginner", "skill_vector": {"Dev": 0.4, "Design": 0.1, "AI_ML": 0.3}, "skills": ["Python", "HTML"], "interests": ["Gaming", "EdTech"], "personality_type": "Explorer", "reliability_score": 0.5, "hackathons_attended": 0, "availability_hours": 30, "is_mentor": False, "looking_for_team": True}
    ]

    events_data = [
        {"event_id": "EVT001", "name": "HackFest 2026", "theme": "EdTech for All", "required_roles": ["Design", "Dev", "AI/ML"], "difficulty": "Beginner", "team_size_limit": 4, "registration_deadline_days": 15, "prize_pool": 10000, "platform": "Unstop", "estimated_participants": 100, "location": "Online", "status": "Open"},
        {"event_id": "EVT002", "name": "AI for Good", "theme": "Smart City Solutions", "required_roles": ["Dev", "Infra", "Design"], "difficulty": "Intermediate", "team_size_limit": 4, "registration_deadline_days": 10, "prize_pool": 25000, "platform": "Devfolio", "estimated_participants": 150, "location": "Campus", "status": "Open"},
        {"event_id": "EVT003", "name": "CodeSprint", "theme": "AI for Healthcare", "required_roles": ["AI/ML", "Dev", "Design"], "difficulty": "Advanced", "team_size_limit": 3, "registration_deadline_days": 5, "prize_pool": 50000, "platform": "HackerEarth", "estimated_participants": 80, "location": "Hybrid", "status": "Closing Soon"}
    ]

    matches_data = [
        {"match_id": "MAT001", "user_id": "USR0001", "event_id": "EVT001", "match_score": 85.1, "match_category": "Excellent Match", "skill_complementarity": 29.8, "interest_alignment": 17.0, "experience_fit": 17.0, "availability_score": 8.5, "reliability_score": 12.8},
        {"match_id": "MAT002", "user_id": "USR0002", "event_id": "EVT001", "match_score": 78.2, "match_category": "Good Match", "skill_complementarity": 25.0, "interest_alignment": 15.0, "experience_fit": 10.0, "availability_score": 10.0, "reliability_score": 18.2},
        {"match_id": "MAT003", "user_id": "USR0003", "event_id": "EVT001", "match_score": 92.4, "match_category": "Excellent Match", "skill_complementarity": 32.0, "interest_alignment": 18.0, "experience_fit": 20.0, "availability_score": 10.0, "reliability_score": 12.4},
        {"match_id": "MAT004", "user_id": "USR0005", "event_id": "EVT001", "match_score": 88.0, "match_category": "Excellent Match", "skill_complementarity": 30.0, "interest_alignment": 17.0, "experience_fit": 18.0, "availability_score": 9.0, "reliability_score": 14.0},
        {"match_id": "MAT005", "user_id": "USR0006", "event_id": "EVT001", "match_score": 72.5, "match_category": "Good Match", "skill_complementarity": 24.0, "interest_alignment": 14.0, "experience_fit": 12.0, "availability_score": 10.0, "reliability_score": 12.5}
    ]

    # Write files only if they don't exist
    if not os.path.exists("students.json"):
        with open("students.json", "w") as f:
            json.dump(students_data, f)
    if not os.path.exists("events.json"):
        with open("events.json", "w") as f:
            json.dump(events_data, f)
    if not os.path.exists("matches.json"):
        with open("matches.json", "w") as f:
            json.dump(matches_data, f)

# Call the function to ensure data exists
ensure_data_files()

# ============================================
# LOAD DATA
# ============================================
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
    exp_counts = df_students["experience_level"].value_counts()
    st.bar_chart(exp_counts)

elif page == "🎯 AI Match Simulator":
    st.markdown("## 🎯 Interactive AI Match Simulator")
    
    event_names = [e["name"] for e in events]
    selected_name = st.selectbox("Select a Hackathon:", event_names)
    event = next(e for e in events if e["name"] == selected_name)
    
    st.info(f"**Event:** {event['name']} | **Theme:** {event['theme']} | **Roles Needed:** {', '.join(event['required_roles'])}")
    
    event_matches = df_matches[df_matches["event_id"] == event["event_id"]].sort_values("match_score", ascending=False)
    
    if not event_matches.empty:
        st.markdown("### 🤝 Recommended Teammates")
        
        for i, (_, m) in enumerate(event_matches.head(3).iterrows()):
            s = next((st for st in students if st["user_id"] == m["user_id"]), None)
            if s:
                st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #667eea;">
                    <h3>🥇 {i+1}. {s['name']} <span style="background:#667eea; color:white; padding:2px 8px; border-radius:10px; font-size:0.8em;">{m['match_score']}% Match</span></h3>
                    <p><b>Role:</b> {s['experience_level']} | <b>Skills:</b> {', '.join(s['skills'])}</p>
                    <p><b>Why?</b> {m['match_category']}. Skill Fit: {m['skill_complementarity']}% | Reliability: {m['reliability_score']}%</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Match Scores")
        st.bar_chart(event_matches.head(3).set_index("user_id")["match_score"])
    else:
        st.warning("No specific matches for this event yet. Try another event.")

elif page == "👥 Student Explorer":
    st.markdown("## 👥 Student Explorer")
    st.dataframe(df_students[["name", "branch", "year", "experience_level", "skills", "reliability_score"]])
