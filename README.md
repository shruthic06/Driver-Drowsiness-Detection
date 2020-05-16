# Driver Drowsiness Detection


## Overview

This project implements a **driver drowsiness detection system** that monitors facial features and eye movements in real-time using computer vision techniques. By leveraging Haar Cascade classifiers, CNN models, and image-based heuristics, the system alerts drivers when signs of fatigue or drowsiness are detected.

The application combines **classical vision methods** (Haar Cascades) with **deep learning (CNN)** for robust detection. An alarm is triggered when the driver’s eyes remain closed for a prolonged period, enhancing road safety and minimizing risks of accidents caused by fatigue.

---

## Project Objectives

- Detect facial landmarks, particularly eyes, in real-time video streams.
- Use CNN-based classification to detect open/closed eyes.
- Trigger an **audio alarm** (`alarm.wav`) when drowsiness is detected.
- Provide a modular design for future integration with **vehicle monitoring systems**.

---

## Core Features

- **Face & Eye Detection**  
  - Haar cascades for left eye, right eye, and frontal face.
- **Deep Learning Model**  
  - Pre-trained CNN (`cnnCat2.h5`) to classify eye states.
- **Alert Mechanism**  
  - Audible alarm triggered if eyes remain closed.
- **Supportive Utilities**  
  - Scripts for traffic light detection, vehicle detection, and mapping for integration with larger safety applications.

---

## Project Structure

```
.
├── models/                   # Pre-trained models & resources
│   ├── haarcascade_lefteye_2splits.xml
│   ├── haarcascade_righteye_2splits.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── cnnCat2.h5
│   └── alarm.wav
├── data/                     # Sample data for testing
│   ├── frames/               # Example image frames
│   ├── map.PNG
│   ├── map1.JPG
│   └── map2.JPG
├── src/                      # Source code
│   ├── main.py               # Main entry point for drowsiness detection
│   ├── vehicle_detection.py  # Vehicle detection logic
│   ├── traffic_color_detection.py # Traffic light color recognition
│   ├── maps.py               # Mapping functions
│   ├── haversine_formula.py  # Distance calculation utilities
│   └── trial.py              # Experimental scripts
├── requirements.txt          # Python dependencies
├── README.md
└── LICENSE.md
```

---

## Installation

Clone the repository and install requirements:

```bash
git clone https://github.com/<your-username>/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection
pip install -r requirements.txt
```

---

## Usage

Run the main script to start detection:

```bash
python src/main.py
```

> The webcam will activate, and real-time drowsiness monitoring will begin.  
> If the driver’s eyes stay closed, the alarm will sound.


---

## Sample Data

- **`data/frames/`** contains pre-collected driver images for testing.
- Maps and traffic-related images (`map.PNG`, `map1.JPG`, `map2.JPG`) support additional modules (traffic detection).

---

## Future Scope

- Integration with vehicle telemetry and IoT systems.
- Support for multi-class classification (e.g., yawning, head pose).
- Deploy on **edge devices** like Raspberry Pi for real-time applications.
- Enhance CNN with transfer learning (e.g., MobileNet, EfficientNet).

---

## Configuration & Training

The system uses a pre-trained CNN model (`cnnCat2.h5`) for eye state classification.  
If you want to retrain the model:

1. Collect labeled eye images (open/closed) and organize them into training and validation sets.
2. Modify the training script (to be created under `src/`) to load the dataset and train a CNN.
3. Save the trained model as `cnnCat2.h5` inside the `models/` directory.

This allows flexibility for improving accuracy with larger or custom datasets.

---

## License

This project is licensed under the [MIT License](./LICENSE.md).
