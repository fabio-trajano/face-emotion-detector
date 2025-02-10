import cv2
from fer import FER

def main():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    detector = FER()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting...")
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        detections = detector.detect_emotions(rgb_frame)

        for detection in detections:
            (x, y, w, h) = detection["box"]
            emotions = detection["emotions"]

            dominant_emotion = max(emotions, key=emotions.get)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.putText(
                frame,
                dominant_emotion,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2,
                cv2.LINE_AA
            )

        cv2.imshow("Face Emotion Detector (press 'q' to quit)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
