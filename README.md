# api-security

A hardened OpenWeatherMap API client built for a healthcare startup, demonstrating
secure credential management, graceful error handling, and privacy-compliant logging.

---

## Repository Contents

| File | Purpose |
|------|---------|
| `weather.py` | Production-ready API client with all security/privacy fixes applied |
| `.env.example` | Template showing which environment variables to set (no real secrets) |
| `.gitignore` | Ensures `.env` is never committed to version control |
| `README.md` | This file |

> **Note:** The real `.env` file is excluded from this repository via `.gitignore`.
> See the screenshot below confirming `.env` does not appear in the GitHub file tree.

---

## Security & Privacy Q&A

### Q1 — What are the real-world consequences of exposing an API key on GitHub?

Exposing an API key publicly on GitHub can lead to **immediate and severe consequences**.
Automated bots continuously scan GitHub commits for secrets; within minutes, a leaked key
can be harvested and abused. Attackers may run up thousands of dollars in API charges on
the account holder's billing plan, exhaust the free-tier quota, or pivot the key to access
other services if the same credential is reused. For a healthcare startup, a leaked key
could also violate vendor agreements, trigger breach notification obligations under HIPAA,
and undermine patient trust — all of which carry significant legal and financial penalties.

### Q2 — Why does the company privacy policy prohibit logging city names?

A patient's searched city is **location data** — a category of personal information
protected under multiple frameworks.  Under **GDPR Article 5(1)(c)** (data minimisation),
organisations must process *only* the data strictly necessary to achieve their stated
purpose; logging a city name for a weather alert goes beyond that purpose.  Under the
**HIPAA Minimum Necessary Rule (§164.502(b))**, covered entities must limit the use and
disclosure of Protected Health Information to the minimum required.  Storing or transmitting
a patient's location in log files could expose that data to monitoring systems, third-party
log aggregators, or future data breaches — creating liability that far outweighs any
operational benefit of logging the city name.

---

## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/api-security-yourname.git
cd api-security-yourname

# 2. Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install requests python-dotenv

# 3. Create your .env file from the example template
cp .env.example .env
# Edit .env and replace 'your_api_key_here' with your real OpenWeatherMap key

# 4. Run the script
python weather.py
```

---

## Screenshot


<img width="1487" height="546" alt="image" src="https://github.com/user-attachments/assets/383a86f4-196e-4508-94cb-7c52485a8e8d" />

---

