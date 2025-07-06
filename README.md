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
# Create a new .env file
touch .env

# Open it in your editor and add your SDK key like this:
LD_SDK_KEY=your-server-sdk-key-here
Note: Your key is loaded automatically in flags.py using python-dotenv.

5. Run the app
python app.py
# Open http://localhost:5050 in your browser

6. Test
curl http://localhost:5050/api/feature
# Or click the Get Started button on the homepage

Flag is evaluated using the following context:
Context.builder("user-key-123")
    .kind("user")
    .name("Jorge")
    .set("plan", "premium")
    .build()
```

---

## 📈 CTA Button Metric

When the “Get Started” button is clicked:

- A `POST` request is sent to `/api/cta-click`
- The backend uses `ld_client.track()` to record the metric event
- This feeds into the experiment set up in LaunchDarkly

---

## 📊 Experimentation (Extra Credit)

- **Metric created**: `"CTA Clicks"`
- **Experiment created**: Targeted users are split by the feature flag to measure impact
- **Objective**: Understand how many users engage with the new feature via the CTA

---

## 🙌 Author

**Jorge C.R.**  
GitHub: [@yoshi128](https://github.com/yoshi128)
