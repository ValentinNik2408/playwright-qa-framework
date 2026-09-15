# Playwright QA Automation Framework (Python)

A scalable and modern Web Automation testing framework built from scratch using **Python**, **Playwright**, and **Pytest**. This framework implements the industry-standard **Page Object Model (POM)** design pattern to ensure clean, reusable, and maintainable test scripts.

---

## 🛠️ Tech Stack & Environment
* **Language:** Python 3.11+
* **Testing Framework:** Pytest
* **Automation Library:** Playwright (Python)
* **Target Browser:** Chromium
* **OS Environment:** Windows (Local) / Windows Server (CI/CD Pipeline)

---

## 📂 Project Structure
```text
playwright-qa-framework/
│
├── .github/workflows/      # Continuous Integration (CI) configuration
│   └── playwright.yml      # Automated pipeline triggering on pushes/PRs
│
├── pages/                  # Page Object Classes (UI Element & Action isolation)
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── tests/                  # Test Suites & Framework Configuration
│   ├── __init__.py
│   ├── conftest.py         # Pytest fixtures (Setup & Teardown lifecycles)
│   └── test_login.py       # Core test scripts
│
├── .gitignore              # Safeguards local caches (__pycache__) and venv
├── pytest.ini              # Default execution configurations (Chromium, Headed)
├── README.md               # Framework documentation
└── requirements.txt        # Managed Python dependencies
```

---

## 🚀 Getting Started (Windows Setup)

Follow these steps to spin up and run this testing framework on your local Windows machine:

### 1. Clone the Repository
```powershell
git clone https://github.com
cd playwright-qa-framework
```

### 2. Create and Activate Virtual Environment
```powershell
# Create venv
python -m venv venv

# Activate venv
.\venv\Scripts\activate
```

### 3. Install Dependencies & Browsers
```powershell
# Install required libraries
pip install -r requirements.txt

# Download only the Chromium binaries to save space
playwright install chromium
```

---

## 🧪 Running Tests Locally

Thanks to the integrated `pytest.ini` setup, executing tests is streamlined. Ensure your `venv` is active and run:

```powershell
# Executes tests using the pre-configured Chromium Headed mode
pytest
```

### Useful Pytest Flags:
* Run text-only execution (Headless): `pytest --headless`
* Capture visual traces for debugging: `pytest --tracing on`

---

## 🔄 CI/CD Pipeline (GitHub Actions)
This repository includes an automated pipeline that checks your code build on every push or pull request to the `master` branch.
* It provisions a fresh **`windows-latest`** environment host.
* Restricts dependencies specifically to **Chromium** for rapid, cost-efficient pipeline processing.
