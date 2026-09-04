# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey dmmsureshcbe-bit!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/dmmsureshcbe-bit/skills-getting-started-with-github-copilot-SureshM0209cts/issues/1)

---

## Run the project

This project is a FastAPI application for browsing Mergington High School activities and signing up for them.

### Prerequisites

- Python 3.10 or newer
- Git

### Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/dmmsureshcbe-bit/skills-getting-started-with-github-copilot-SureshM0209cts.git
cd skills-getting-started-with-github-copilot-SureshM0209cts
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Start the development server

```bash
uvicorn src.app:app --reload
```

Open [http://localhost:8000](http://localhost:8000) to use the application. Interactive API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs), and the alternative documentation is at [http://localhost:8000/redoc](http://localhost:8000/redoc).

### Run the tests

With the virtual environment activated, run:

```bash
pytest
```

### API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/activities` | List all activities and participants |
| `GET` | `/countries/{country}/cities` | List cities for a supported country or region |
| `POST` | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up a student for an activity |
| `DELETE` | `/activities/{activity_name}/participants/{email}` | Remove a participant from an activity |

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

