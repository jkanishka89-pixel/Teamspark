import json
import pandas as pd

# Mini-Dataset for Demo
students = [
    {"user_id": "USR0001", "name": "Abhishek Singh", "branch": "CS", "year": "3rd", "experience_level": "Intermediate", "skill_vector": {"Dev": 0.85, "Design": 0.46, "AI_ML": 0.83}, "skills": ["Python", "React", "ML"], "interests": ["HealthTech", "Web3"], "personality_type": "Explorer", "reliability_score": 0.6, "hackathons_attended": 7, "availability_hours": 27, "is_mentor": False, "looking_for_team": True},
    {"user_id": "USR0002", "name": "Sneha Kaur", "branch": "Design", "year": "1st", "experience_level": "Beginner", "skill_vector": {"Dev": 0.24, "Design": 0.66, "AI_ML": 0.17}, "skills": ["Figma", "UI/UX"], "interests": ["EdTech", "SocialImpact"], "personality_type": "Mentor", "reliability_score": 0.63, "hackathons_attended": 0, "availability_hours": 15, "is_mentor": False, "looking_for_team": True},
    {"user_id": "USR0003", "name": "Vivek Kaur", "branch": "IT", "year": "4th", "experience_level": "Advanced", "skill_vector": {"Dev": 1.0, "Design": 0.53, "AI_ML": 0.95}, "skills": ["FastAPI", "DSA", "ML"], "interests": ["AgriTech", "EdTech"], "personality_type": "Creative", "reliability_score": 0.63, "hackathons_attended": 12, "availability_hours": 20, "is_mentor": True, "looking_for_team": True},
    {"user_id": "USR0004", "name": "Rohan Das", "branch": "ECE", "year": "3rd", "experience_level": "Intermediate", "skill_vector": {"Dev": 0.7, "Design": 0.3, "AI_ML": 0.4}, "skills": ["C++", "Embedded"], "interests": ["IoT", "Automation"], "personality_type": "Leader", "reliability_score": 0.8, "hackathons_attended": 4, "availability_hours": 10, "is_mentor": False, "looking_for_team": True},
]

events = [
    {"event_id": "EVT001", "name": "HackFest 2026", "theme": "EdTech for All", "required_roles": ["Design", "Dev", "AI/ML"], "difficulty": "Beginner", "team_size_limit": 4, "registration_deadline_days": 15, "prize_pool": 10000, "platform": "Unstop", "estimated_participants": 100, "location": "Online", "status": "Open"},
    {"event_id": "EVT002", "name": "AI for Good", "theme": "Smart City Solutions", "required_roles": ["Dev", "Infra", "Design"], "difficulty": "Intermediate", "team_size_limit": 4, "registration_deadline_days": 10, "prize_pool": 25000, "platform": "Devfolio", "estimated_participants": 150, "location": "Campus", "status": "Open"},
]

matches = [
    {"match_id": "MAT001", "user_id": "USR0001", "event_id": "EVT001", "match_score": 85.1, "match_category": "Excellent Match", "skill_complementarity": 29.8, "interest_alignment": 17.0, "experience_fit": 17.0, "availability_score": 8.5, "reliability_score": 12.8},
    {"match_id": "MAT002", "user_id": "USR0002", "event_id": "EVT001", "match_score": 78.2, "match_category": "Good Match", "skill_complementarity": 25.0, "interest_alignment": 15.0, "experience_fit": 10.0, "availability_score": 10.0, "reliability_score": 18.2},
    {"match_id": "MAT003", "user_id": "USR0003", "event_id": "EVT001", "match_score": 92.4, "match_category": "Excellent Match", "skill_complementarity": 32.0, "interest_alignment": 18.0, "experience_fit": 20.0, "availability_score": 10.0, "reliability_score": 12.4},
]

with open("students.json", "w") as f: json.dump(students, f)
with open("events.json", "w") as f: json.dump(events, f)
with open("matches.json", "w") as f: json.dump(matches, f)

print("✅ Data files created successfully!")
