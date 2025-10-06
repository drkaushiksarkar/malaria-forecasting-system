# Contributing to Malaria Forecasting System

Thank you for your interest in improving the **Malaria Forecasting System**!  
Your time and expertise are appreciated.

---

## 🧭 Project Maintainer
**Primary Developer:** Kaushik Sarkar  
GitHub: [@drkaushiksarkar](https://github.com/drkaushiksarkar)

All proposed changes must respect the repository protection rules:
- Only approved pull requests are merged.
- `DEVELOPERS.md` cannot be modified without Code Owner approval.

---

## 🛠️ How to Contribute

### 1. Fork and Clone
Fork the repository and clone it locally:
```bash
git clone https://github.com/drkaushiksarkar/malaria-forecasting-system.git
cd malaria-forecasting-system
```

### 2. Create a Branch
Use a descriptive branch name:
```bash
git checkout -b feature/add-verification-metrics
```

### 3. Install Dependencies
Create a virtual environment and install requirements:
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### 4. Make Your Changes
Follow project conventions:
- Keep code clean, modular, and commented.
- Use **type hints** and **docstrings**.
- Ensure **no hard-coded paths** or credentials.

### 5. Run Tests and Linters
All PRs must pass CI checks:
```bash
pytest -v
ruff check .
black --check .
```

To auto-format:
```bash
black .
ruff check . --fix
```

### 6. Commit Convention
Use clear, conventional commits:
```
feat: add new forecasting metric
fix: correct SMAPE calculation
docs: update API documentation
refactor: optimize fine-tuning loop
```

### 7. Push and Open a Pull Request
```bash
git push origin feature/add-verification-metrics
```
Then open a pull request on GitHub:
- Provide a meaningful **title and description**
- Reference related issues (e.g. “Fixes #12”)
- Wait for review from the maintainer

---

## 🧪 Testing

Tests live under `/tests/` and `/tests/integration/`.  
Ensure all tests pass before submitting your PR.

```bash
pytest
```

To run only integration tests:
```bash
pytest tests/integration/
```

---

## 🧩 Code Review & Merge Policy

- Every PR requires review by **@drkaushiksarkar** (Code Owner).
- CI must pass (tests, lint, name verification).
- Protected branches (`main`) cannot be pushed directly.
- After approval, the PR will be squashed and merged.

---

## 🧾 Reporting Issues

Found a bug or have a feature idea?
1. Check [existing issues](../../issues)
2. If not present, open a **new issue**
   - Provide details, reproduction steps, logs, and screenshots if applicable.

---

## ⚖️ License

By contributing, you agree that your contributions are licensed under the **MIT License** and that the repository maintainer (Kaushik Sarkar) retains authorship of the base system.

---

## 🙏 Thank You

Your contributions help strengthen malaria surveillance and predictive modeling.  
Every fix, test, and improvement helps improve global health forecasting.