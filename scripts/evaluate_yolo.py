# evaluate_yolo.py
import time
import torch
from ultralytics import YOLO
from pathlib import Path

def evaluate(model_path="models/yolov8n_defect.onnx", data_path="synthetic_phantoms/demo_data", imgsz=256):
    model = YOLO(model_path)
    results = model.val(data=f"{data_path}/yolo_dataset.yaml", imgsz=imgsz, save=False)

    print("📊 Evaluation Results:")
    print(f"mAP@0.5: {results.results_dict['metrics/mAP50']:.3f}")
    print(f"Precision: {results.results_dict['metrics/precision']:.3f}")
    print(f"Recall: {results.results_dict['metrics/recall']:.3f}")

    # Inference speed
    dummy_input = torch.randn(1, 3, imgsz, imgsz)
    start = time.time()
    model.predict(dummy_input)
    end = time.time()
    print(f"⚡ Inference Time: {(end - start) * 1000:.2f} ms/image")

if __name__ == "__main__":
    evaluate()

