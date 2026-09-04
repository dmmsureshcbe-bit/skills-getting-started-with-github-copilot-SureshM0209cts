<div align="center">

# 🎉 Congratulations dmmsureshcbe-bit! 🎉

<img src="https://octodex.github.com/images/welcometocat.png" height="200px" />

### 🌟 You've successfully completed the exercise! 🌟

## 🚀 Share Your Success!

**Show off your new skills and inspire others!**

<a href="https://twitter.com/intent/tweet?text=I%20just%20completed%20the%20%22Getting%20Started%20with%20GitHub%20Copilot%22%20GitHub%20Skills%20hands-on%20exercise!%20%F0%9F%8E%89%0A%0Ahttps%3A%2F%2Fgithub.com%2Fdmmsureshcbe-bit%2Fskills-getting-started-with-github-copilot-SureshM0209cts%0A%0A%23GitHubSkills%20%23OpenSource%20%23GitHubLearn" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Share%20on%20X-1da1f2?style=for-the-badge&logo=x&logoColor=white" alt="Share on X" />
</a>
<a href="https://bsky.app/intent/compose?text=I%20just%20completed%20the%20%22Getting%20Started%20with%20GitHub%20Copilot%22%20GitHub%20Skills%20hands-on%20exercise!%20%F0%9F%8E%89%0A%0Ahttps%3A%2F%2Fgithub.com%2Fdmmsureshcbe-bit%2Fskills-getting-started-with-github-copilot-SureshM0209cts%0A%0A%23GitHubSkills%20%23OpenSource%20%23GitHubLearn" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Share%20on%20Bluesky-0085ff?style=for-the-badge&logo=bluesky&logoColor=white" alt="Share on Bluesky" />
</a>
<a href="https://www.linkedin.com/feed/?shareActive=true&text=I%20just%20completed%20the%20%22Getting%20Started%20with%20GitHub%20Copilot%22%20GitHub%20Skills%20hands-on%20exercise!%20%F0%9F%8E%89%0A%0Ahttps%3A%2F%2Fgithub.com%2Fdmmsureshcbe-bit%2Fskills-getting-started-with-github-copilot-SureshM0209cts%0A%0A%23GitHubSkills%20%23OpenSource%20%23GitHubLearn" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Share%20on%20LinkedIn-0077b5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Share on LinkedIn" />
</a>

### 🎯 What's Next?

**Keep the momentum going!**

[![](https://img.shields.io/badge/Return%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/dmmsureshcbe-bit/skills-getting-started-with-github-copilot-SureshM0209cts/issues/1)
[![GitHub Skills](https://img.shields.io/badge/Explore%20GitHub%20Skills-000000?style=for-the-badge&logo=github&logoColor=white)](https://learn.github.com/skills)

*There's no better way to learn than building things!* 🚀

</div>

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

