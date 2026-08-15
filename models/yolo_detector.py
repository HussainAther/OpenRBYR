from ultralytics import YOLO

def load_yolo_model():
    model = YOLO('models/yolov8n.pt')
    return model

