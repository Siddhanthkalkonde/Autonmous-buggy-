import cv2
import numpy as np
from ultralytics import YOLO

def load_model(model_path):
    """
    Load a YOLOv8 model from a given path.
    """
    return YOLO(model_path)

def process_frame(frame, model):
    """
    Perform semantic segmentation on a single frame using the given model.
    """
    # Perform segmentation
    results = model(frame, task='segment')
    
    # Get the segmentation mask
    if results[0].masks is not None and len(results[0].masks) > 0:
        mask = results[0].masks.data[0].cpu().numpy()
        mask = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
        mask = (mask * 255).astype(np.uint8)
        
        # Create a color mask
        color_mask = cv2.applyColorMap(mask, cv2.COLORMAP_JET)
        
        # Blend the original frame with the color mask
        blended = cv2.addWeighted(frame, 0.6, color_mask, 0.4, 0)
    else:
        blended = frame
    
    return blended

def main():
    # Set the path to the YOLOv8n-seg model
    model_path = 'yolov8n-seg.pt'

    # Load the model
    model = load_model(model_path)

    # Initialize the camera
    # cap = cv2.VideoCapture('/home/sid/trial/Autonomous buggy/Pedestrian Crosswalk Signal Improperly Timed, Elmhurst, Queens, New York.mp4')  # 0 for default camera, change if using a different camera
    cap = cv2.VideoCapture(0)  # 0 for default camera, change if using a different camera

    # Set lower resolution for faster processing
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Create a window
    cv2.namedWindow('YOLOv8n Real-time Semantic Segmentation', cv2.WINDOW_NORMAL)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame
        processed_frame = process_frame(frame, model)

        # Display the processed frame
        cv2.imshow('YOLOv8n Real-time Semantic Segmentation', processed_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()