"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball team for intramural and league play",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu", "alex@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn tennis skills and participate in friendly matches",
        "schedule": "Wednesdays and Saturdays, 3:00 PM - 4:30 PM",
        "max_participants": 16,
        "participants": ["laura@mergington.edu", "chris@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and various art techniques",
        "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "lucas@mergington.edu"]
    },
    "Drama Club": {
        "description": "Perform in theatrical productions and develop acting skills",
        "schedule": "Wednesdays and Saturdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["grace@mergington.edu", "ryan@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and critical thinking through debate competitions",
        "schedule": "Mondays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["sarah@mergington.edu", "david@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts through hands-on activities",
        "schedule": "Tuesdays, 3:30 PM - 4:45 PM",
        "max_participants": 16,
        "participants": ["nathan@mergington.edu", "amber@mergington.edu"]
    }
}

cities_by_country = {
    "United States": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary"],
    "United Kingdom": ["London", "Manchester", "Birmingham", "Edinburgh"],
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")



@app.get("/activities")
def get_activities():
    return activities


@app.get("/countries/{country}/cities")
def get_cities(country: str):
    """Return the cities for a country or region."""
    cities = cities_by_country.get(country)
    if cities is None:
        raise HTTPException(
            status_code=404,
            detail=f"Country or region '{country}' not found",
        )
    return {"country": country, "cities": cities}


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/participants/{email}")
def remove_participant(activity_name: str, email: str):
    """Remove a student from an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if email exists in participants
    if email not in activity["participants"]:
        raise HTTPException(status_code=404, detail="Participant not found")

    # Remove student
    activity["participants"].remove(email)
    return {"message": f"Removed {email} from {activity_name}"}
