# Face Emotion Detector

This project captures live video from your webcam, detects faces, and classifies the user's emotion (happy, sad, neutral, angry, etc.) in real-time. The video feed is mirrored (like a real mirror).

## Requirements
- Python 3.7+ (or 3.8+)
- OpenCV
- fer

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/face-emotion-detector.git
   ```

2. Navigate into the project directory:
    ```bash
    cd face-emotion-detector
    ```
2. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script:

    ```bash
    python emotion_detector.py
    ```

The webcam window will open.
Press `q` to quit.
