# 📸 Say Cheese — Background-Aware AI Pose Suggestion Engine
 
> *Because nobody should freeze when someone says "smile!"*
 
---
 
## The Problem
 
Most people — especially introverts — freeze when asked to pose for photos. They don't know what to do with their hands, how to angle their body, or what pose fits the environment they're in. Current camera apps offer zero guidance on this.
 
---
 
## What It Does
 
**Say Cheese** analyzes the background/scene of a photo and suggests contextual poses that would look natural and good in that specific environment.
 
Upload a photo → AI detects your scene → Get 3 pose suggestions with step-by-step instructions.
 
**Examples:**
- Photo at a beach → suggests relaxed, candid shoreline poses
- Photo at a café → suggests editorial, lifestyle poses
- Photo in a forest → suggests adventurous, natural poses
- Photo indoors → suggests cozy, portrait-style poses
---
 
## How It Works
 
A 2-step AI pipeline built with Python and FastAPI:
 
```
Image Upload
     ↓
Step 1: Scene Analysis (Claude AI)
     → Detects background, lighting, mood
     ↓
Step 2: Pose Suggestion Engine (Claude AI)
     → Generates 3 contextual poses with step-by-step instructions
     ↓
Results displayed in browser
```
 
---
 
## Tech Stack
 
- **Backend:** Python, FastAPI, Uvicorn
- **AI:** Anthropic Claude API (Vision + Text)
- **Frontend:** HTML, CSS, JavaScript
- **Environment:** python-dotenv
---
 
## Project Structure
 
```
say-cheese/
├── main.py                 # App entry point
├── routes/
│   └── analyze.py          # API endpoint — receives image, returns poses
├── services/
│   └── claude.py           # AI pipeline — scene analysis + pose suggestions
├── static/
│   └── index.html          # Frontend — what the user sees
├── .env                    # API keys (never pushed to GitHub)
└── requirements.txt        # Python dependencies
```
 
---
 
## Getting Started
 
### 1. Clone the repo
```bash
git clone https://github.com/Puzziii/Say-Cheese.git
cd Say-Cheese
```
 
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
 
### 3. Add your API key
Create a `.env` file:
```
ANTHROPIC_API_KEY=your_key_here
```
 
### 4. Run the app
```bash
uvicorn main:app --reload
```
 
### 5. Open in browser
```
http://localhost:8000
```
 
---
 
## Current Features
 
- Upload a photo (JPEG, PNG, WebP)
- AI detects the background scene and environment type
- Returns 3 pose suggestions tailored to the scene
- Each pose includes a name, vibe tags, description, and step-by-step body instructions
- Clean, dark-mode UI
---
 
## Vision — Where This Is Going
 
### Phase 2 — Live Camera Feed
Replace file upload with a real-time camera stream. Get pose suggestions before you even take the photo — just like Huawei's AI camera does natively, but in a browser.
 
### Phase 3 — Pose Overlays
Draw stick-figure silhouettes directly on the camera feed showing exactly how to position your body — visual guidance, not just text.
 
### Phase 4 — Person Detection
Use computer vision to detect where the person is standing in the frame and suggest poses based on both the background AND their current position.
 
### Phase 5 — Mobile App
Convert into a native iOS/Android app so it works directly in your camera — real-time, no browser needed.
 
### Phase 6 — Multi-Person Mode
Pose suggestions for couples, groups, and families — coordinated poses that work together.
 
### Phase 7 — Style Selector
Choose your shoot style before getting suggestions:
- Editorial / Fashion
- Candid / Natural
- Professional Headshot
- Social Media / Lifestyle
---
 
## Inspiration
 
This project was inspired by Huawei's camera AI that recommends poses before you click — the same concept, rebuilt from scratch as a web app using modern AI APIs.
