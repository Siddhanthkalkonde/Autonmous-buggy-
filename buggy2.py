import cv2
import numpy as np
from ultralytics import YOLO

def load_model(model_path):
    """
    Load a YOLOv8 model from a given path.
    """
    return YOLO(model_path)

def process_frame(frame, model, ball_class_id=0):
    """
    Process a frame using the model to detect a ball.

    Args:
        frame: The frame to process.
        model: The loaded YOLOv8 model.
        ball_class_id (int, optional): The class ID of the ball in the model's COCO labels file. Defaults to 0.

    Returns:
        The processed frame with bounding boxes around detected balls.
    """
    results = model(frame)

    # Iterate through detected objects
    for result in results:
        boxes = result.pandas().xyxy[0]  # Extract bounding boxes data
        for box in boxes.itertuples():
            x_min, y_min, x_max, y_max, conf, cls = box

            # Check if confidence is high enough and class ID matches the ball
            if conf > 0.5 and cls == ball_class_id:
                cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 0, 255), 2)

    return frame


def main():
    # Set the path to the YOLOv8n model trained for ball detection
    model_path = 'yolov8n-ball.pt'  # Replace with your model path

    # Load the model
    model = load_model(model_path)

    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 for default camera, change if using a different camera

    # Set lower resolution for faster processing
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Create a window
    cv2.namedWindow('YOLOv8n Ball Detection', cv2.WINDOW_NORMAL)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame
        processed_frame = process_frame(frame, model)

        # Display the processed frame
        cv2.imshow('YOLOv8n Ball Detection', processed_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()