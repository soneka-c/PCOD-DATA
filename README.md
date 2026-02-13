# PCOD Risk Calculator (Python)

##  Overview

This project was created as part of my learning journey in Python and healthcare AI after completing my PharmD degree. This project is a simple Python-based PCOD (Polycystic Ovarian Disease) risk score calculator. It collects basic clinical indicators from the user and estimates a risk score using rule-based logic. The project is built as a beginner-friendly healthcare + Python + Git workflow practice project.

##  Purpose

I wanted to practice Python programming and GitHub workflow by building a small healthcare-related tool. Since PCOD is a common clinical condition, I chose it as a sample use case.
* Practice Python scripting
* Learn Git & GitHub workflow
* Build healthcare-oriented mini tools
* Create an AI/health portfolio starter project

##  Inputs Used

The calculator asks for:

* BMI value
* Irregular menstrual cycles (yes/no)
* Acne presence (yes/no)
* Excess hair growth (yes/no)

##  How It Works

Each risk factor contributes to a score.
Higher total score → higher PCOD risk category.

Risk categories:

* Low risk
* Moderate risk
* High risk (clinical evaluation recommended)

##  How to Run

### Step 1 — Install Python

Make sure Python is installed and added to PATH.

### Step 2 — Run Script

```bash
python pcod_risk.py
```

### Step 3 — Enter Inputs

Provide values when prompted in the terminal.

##  Example Run

```
PCOD Risk Score Calculator
Enter BMI: 29
Irregular cycles? (y/n): y
Acne present? (y/n): n
Excess hair growth? (y/n): y

Risk Score: 8
High PCOD risk — clinical evaluation recommended
```

##  Project Structure

```
pcod_risk.py
README.md
```

##  Disclaimer

This tool is for educational and demonstration purposes only.
It is not a medical diagnostic system and should not be used for clinical decision-making.

##  Future Improvements

* Dataset-based risk model
* Machine learning prediction
* GUI or web app interface
* Clinical dataset integration
* Visualization dashboard

## 👤 Author

Sonika— PharmD graduate with experienced profile exploring Healthcare AI and Data Science. Beginner healthcare-AI project — Python + GitHub practice.
