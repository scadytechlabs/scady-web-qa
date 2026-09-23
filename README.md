# Scady Web QA Automation Framework

A professional web UI test automation framework developed by **Scady Tech Labs** using Python, Playwright, and Pytest.

This portfolio project demonstrates how Scady Tech Labs approaches scalable, maintainable, and CI-ready Quality Engineering automation.

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Pytest HTML
- Pytest-xdist
- GitHub Actions

## Automation Coverage

The framework currently covers:

- Successful login
- Invalid login scenarios
- Mandatory-field validation
- Product selection
- Add product to cart
- Multiple-product cart validation
- Remove product from cart
- Checkout workflow
- End-to-end purchase
- Logout

## Framework Features

- Page Object Model architecture
- Positive and negative testing
- Data-driven testing
- Smoke and regression markers
- Externalized test data
- Automatic screenshots on test failure
- HTML execution reports
- Parallel test execution
- GitHub Actions CI
- Automated regression execution on every push

## Project Structure

```text
scady-web-qa/
├── .github/
│   └── workflows/
├── config/
├── data/
├── pages/
├── reports/
├── tests/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/scadytechlabs/scady-web-qa.git
cd scady-web-qa
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

Run the complete regression suite:

```bash
pytest
```

Run smoke tests:

```bash
pytest -m smoke
```

Run negative tests:

```bash
pytest -m negative
```

Run tests in parallel:

```bash
pytest -n 2
```

Run with the browser visible:

```bash
pytest --headed
```

## Reporting

An HTML execution report is automatically generated at:

```text
reports/report.html
```

When a test fails, screenshot evidence is automatically stored under:

```text
reports/screenshots/
```

## CI/CD

GitHub Actions automatically executes the automation suite when code is pushed to the `main` branch or when a pull request targets `main`.

Execution reports are uploaded as workflow artifacts for test evidence.

## Test Application

This portfolio framework uses SauceDemo, a publicly available demonstration application, as the system under test.

This repository is a **Scady Tech Labs portfolio demonstration** and does not represent a client engagement with or endorsement by Sauce Labs.

## About Scady Tech Labs

**Scady Tech Labs** provides Quality Engineering and software automation services focused on:

- QA Automation
- Web Testing
- API Testing
- CI/CD Quality Engineering
- AI-assisted Automation
- Software Quality Solutions

---

**Scady Tech Labs — Ship Faster. Test Smarter. Automate More.**