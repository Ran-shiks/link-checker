# link-checker 🔗

[![Codecov](https://codecov.io/gh/Ran-shiks/link-checker/graph/badge.svg?token=YOUR_CODECOV_TOKEN)](https://codecov.io/gh/Ran-shiks/link-checker)
[![PyPI Version](https://badge.fury.io/py/link-checker.svg)](https://badge.fury.io/py/link-checker) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple yet powerful command-line (CLI) tool to find broken links in local files or web pages.

This project serves as a complete exercise for implementing a professional-grade CI/CD pipeline using GitHub Actions, including testing, security checks, and automated deployment to PyPI.

---

## ✨ Features

* Parses local files (like `.md`, `.txt`) and extracts all URLs.
* Scans a remote URL and extracts all links (from `<a>` tags).
* Asynchronously (quickly!) checks every link to verify its status (OK, Broken, Timeout).
* Generates a clear report of good and broken links.
* Gracefully handles network errors and timeouts.
* Fully tested and validated by an automated pipeline.

---

## 🚀 Installation

Once published to PyPI, the tool will be installable via `pip`:

```bash
pip install link-checker
````

-----

## Usage

The tool can be used directly from your terminal.

**To check a local file:**

```bash
link-checker README.md
```

**To check a web page:**

```bash
link-checker [https://www.google.com](https://www.google.com)
```

**To get only the broken links (recommended):**

```bash
link-checker README.md --only-broken
```

**To see all options:**

```bash
link-checker --help
```

-----

## 🛠️ Development & Contributing

This section describes how to set up the development environment and how to run the pipeline locally before pushing.

### 1\. Environment Setup

It is highly recommended to use a virtual environment.

```bash
# 1. Clone the repository
git clone [https://github.com/Ran-shiks/link-checker.git](https://github.com/Ran-shiks/link-checker.git)
cd link-checker

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 3. Install project AND development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt # File for test tools (see below)
```

### 2\. Running the Pipeline Locally

Before you `git push`, run these commands to ensure the pipeline won't fail. This is the same set of checks that GitHub Actions will run.

```bash
# 1. Run Tests and Coverage (Pytest + Codecov)
python -m pytest --cov=application

# 2. Quality Check (Flake8) - Checks for bugs, not style
flake8 application/ --count --select=E9,F,W6 --show-source --statistics

# 3. Type Checking (MyPy)
mypy application/

# 4. Code Security Scan (Bandit)
bandit -r application/

# 5. Dependency Security Scan (Safety)
safety check -r requirements.txt
```

If all these commands pass without error, you are ready to push\!

### 3\. Contribution Process

1.  Create a new branch (`git checkout -b feature/my-new-thing`).
2.  Make your changes.
3.  Run the local pipeline (see above).
4.  Commit and push your branch.
5.  Open a **Pull Request** to `main`.

The pipeline will automatically run on your Pull Request. Merging will only be allowed if all checks (`quality-checks` and `test`) pass.

-----

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
