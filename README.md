# CNN Banana Classifier

A deep learning project that classifies bananas into three categories: **ripe**, **rotten**, and **unripe** using a Convolutional Neural Network (CNN) based on VGG16 architecture with transfer learning.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training Pipeline](#training-pipeline)
- [API Endpoints](#api-endpoints)
- [Results](#results)
- [Project Workflow](#project-workflow)

## Features

- **Transfer Learning**: Utilizes pre-trained VGG16 model for efficient training
- **Data Augmentation**: Implements image augmentation to improve model generalization
- **Pipeline Architecture**: Modular, stage-based training pipeline
- **Web Interface**: Flask-based web application with interactive UI for predictions
- **Version Control**: DVC integration for data and model versioning
- **Monitoring**: TensorBoard integration for training visualization

## Project Structure

```
CNN-classifier/
├── artifacts/                 # Model artifacts and outputs
│   ├── data_ingestion/        # Processed datasets
│   ├── prepare_base_model/    # Base and updated models
│   ├── prepare_callbacks/     # Training checkpoints and logs
│   └── training/              # Trained model
├── config/                    # Configuration files
│   └── config.yaml            # Main configuration
├── research/                  # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb
│   ├── 02_prepare_base_model.ipynb
│   ├── 03_prepare_callbacks.ipynb
│   ├── 04_training.ipynb
│   └── 05_model_evaluation.ipynb
├── src/
│   └── cnnClassifier/         # Main package
│       ├── components/        # Core components
│       ├── config/            # Configuration management
│       ├── entity/            # Data entities
│       ├── pipeline/           # Training pipelines
│       └── utils/             # Utility functions
├── templates/                 # HTML templates
│   └── index.html
├── app.py                     # Flask application
├── main.py                    # Training pipeline runner
├── params.yaml                # Hyperparameters
├── requirements.txt           # Python dependencies
└── setup.py                   # Package setup
```

## Technology Stack

- **Deep Learning**: TensorFlow, Keras
- **Backend**: Flask, Flask-CORS
- **Data Processing**: NumPy, Pandas
- **Version Control**: DVC (Data Version Control)
- **Configuration**: PyYAML, python-box
- **Utilities**: tqdm, joblib, scipy
- **Monitoring**: TensorBoard (for training visualization)

## Installation

### Prerequisites

- Python 3.7+
- pip


## Usage

### Training the Model

Run the complete training pipeline:

```bash
python main.py
```

This will execute all stages:
1. **Data Ingestion**: Downloads and extracts the dataset
2. **Base Model Preparation**: Sets up VGG16 with custom classifier head
3. **Training**: Trains the model with callbacks and augmentation
4. **Evaluation**: Evaluates the model and saves metrics

Alternatively, use DVC to run the pipeline:

```bash
dvc repro
```

### Running the Web Application

Start the Flask server:

```bash
python app.py
```

The application will be available at `http://localhost:8080`

You can use the web interface to:
- Upload banana images
- Get real-time predictions (ripe, rotten, or unripe)
- View classification results with visual feedback


## Model Architecture

- **Base Model**: VGG16 (pre-trained on ImageNet)
- **Input Size**: 224×224×3 (RGB images)
- **Transfer Learning**: Freezes all VGG16 layers
- **Classifier Head**: 
  - Flatten layer
  - Dense layer with 3 units (softmax activation)
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: SGD (Stochastic Gradient Descent)
- **Learning Rate**: 0.01

## Training Pipeline

### Configuration Parameters

Edit `params.yaml` to adjust hyperparameters:

```yaml
AUGMENTATION: True
IMAGE_SIZE: [224, 224, 3]
BATCH_SIZE: 16
INCLUDE_TOP: False
EPOCHS: 10
CLASSES: 3
WEIGHTS: imagenet
LEARNING_RATE: 0.01
```

### Training Features

- **Data Augmentation**: 
  - Rotation (±40°)
  - Horizontal flip
  - Width/height shift (±20%)
  - Shear and zoom transformations
  
- **Callbacks**:
  - Model checkpointing
  - TensorBoard logging
  
- **Validation Split**: 20% of training data

## 🌐 Web Application Routes

The Flask application provides the following routes:

### `GET /`
Returns the main web interface (`index.html`) for uploading images and viewing predictions.

### `POST /predict`
Handles image prediction requests from the web interface. Accepts a base64-encoded image in the request body and returns the classification result.

### `GET/POST /train`
Triggers the training pipeline by running `main.py`.


## Project Workflow

```
Data Ingestion → Base Model Prep → Training → Evaluation
     ↓                ↓                ↓            ↓
Download data    Load VGG16      Train model   Save metrics
Extract data     Add classifier  Augment data  scores.json
                 Freeze layers    Callbacks
```

