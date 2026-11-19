# Driver Drowsiness Detection

A web app that watches your face through the webcam and sounds an alarm when your eyes stay closed for too long, or when you yawn.

Detection runs **in the browser** using MediaPipe Face Landmarker. The Flask server only serves the page, so no video is uploaded anywhere and the app deploys easily on Render's free tier.

## How it works

- Tracks 468 face landmarks in real time.
- Computes the **Eye Aspect Ratio (EAR)**. When EAR stays below the threshold for longer than the chosen time, the alarm sounds.
- Computes the **Mouth Aspect Ratio (MAR)** to count yawns.
- Thresholds can be adjusted with sliders on the page.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 and click **Start**. Allow camera access when asked.

## Deploy on Render

1. Push this project to a GitHub repository (files at the repository root).
2. On https://render.com choose **New + > Web Service** and connect the repository.
3. Use these settings:
   - Runtime: **Python 3**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Click **Create Web Service**. When it is live, open the `onrender.com` URL.

Camera access needs HTTPS, which Render provides automatically.

## Note

This is an educational project and not a certified safety device. Never rely on it as the only protection against driver fatigue.
