# LaunchDarkly SE Exercise – Jorge C.R.

## 🚀 Overview
This project showcases feature flagging, targeting, and metric tracking using LaunchDarkly.

## 🧰 Stack
- Flask (Python)
- LaunchDarkly Server SDK
- HTML & JavaScript

## 🧪 What It Does
- Adds a feature flag around a new UI component.
- Targets users based on `plan` (e.g., premium).
- Tracks CTA button clicks using a custom LaunchDarkly metric.

## 📂 Project Structure
├── app.py # Flask app with / and /api/feature routes
├── flags.py # LaunchDarkly SDK setup + flag evaluation
├── test_plan.py # Testing rule-based targeting
├── templates/index.html
├── static/script.js
├── .env.example
├── requirements.txt

## 🛠️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yoshi128/launchdarkly-se-exercise.git
cd launchdarkly-se-exercise

2. Create virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Add your LaunchDarkly SDK key:
cp .env .env
# Edit .env and replace your-server-sdk-key-here with your real SDK key

5. Run the app
python app.py
# Open http://localhost:5050 in your browser

6. Test
curl http://localhost:5050/api/feature
# Or click the Get Started button on the homepage


🙌 Author
GitHub: yoshi128


---

## 🌐 Part 3: Upload to GitHub

### ✅ 1. Initialize Git (in your project folder)

```bash
cd /path/to/launchdarkly-se-exercise
git init


