import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def isolated_activities():
    original_activities = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original_activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)


def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_activity_data(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert expected_activity in activities
    assert "michael@mergington.edu" in activities[expected_activity]["participants"]


def test_signup_adds_participant_to_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Signed up {email} for {activity}"
    }
    assert email in app_module.activities[activity]["participants"]


def test_signup_for_unknown_activity_returns_not_found(client):
    # Arrange
    email = "student@mergington.edu"
    endpoint = "/activities/Unknown%20Club/signup"

    # Act
    response = client.post(
        endpoint,
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_duplicate_signup_returns_bad_request(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Already signed up for this activity"}


def test_remove_participant_removes_existing_participant(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Chess%20Club/participants/michael%40mergington.edu"
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Removed {email} from Chess Club"
    }
    assert email not in app_module.activities["Chess Club"]["participants"]


def test_remove_participant_from_unknown_activity_returns_not_found(client):
    # Arrange
    activity = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Unknown%20Club/participants/student%40mergington.edu"
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_remove_missing_participant_returns_not_found(client):
    # Arrange
    endpoint = "/activities/Chess%20Club/participants/missing%40mergington.edu"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}