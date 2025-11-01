# 🍌 CNN Banana Classifier

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

## ✨ Features

- **Transfer Learning**: Utilizes pre-trained VGG16 model for efficient training
- **Data Augmentation**: Implements image augmentation to improve model generalization
- **Pipeline Architecture**: Modular, stage-based training pipeline
- **Web Interface**: Flask-based web application for real-time predictions
- **Version Control**: DVC integration for data and model versioning
- **Monitoring**: TensorBoard integration for training visualization
- **RESTful API**: Easy-to-use API endpoints for predictions

## 📁 Project Structure

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

## 🛠 Technology Stack

- **Deep Learning**: TensorFlow, Keras
- **Backend**: Flask, Flask-CORS
- **Data Processing**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn
- **Version Control**: DVC (Data Version Control)
- **Configuration**: PyYAML, python-box
- **Utilities**: tqdm, joblib, scipy

## 📦 Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vineeth-john/CNN-classifier.git
   cd CNN-classifier
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package**
   ```bash
   pip install -e .
   ```

## 🚀 Usage

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

### Making Predictions via API

**POST** `/predict`
- **Body**: JSON with base64-encoded image
  ```json
  {
    "image": "base64_encoded_image_string"
  }
  ```
- **Response**: 
  ```json
  [{"image": "ripe_1"}]
  ```
  Possible values: `ripe_1`, `rotten_1`, `unripe_1`, `unknown`

### Making Predictions via Command Line

```bash
python src/cnnClassifier/pipeline/predict.py path/to/image.jpg
```

## 🏗 Model Architecture

- **Base Model**: VGG16 (pre-trained on ImageNet)
- **Input Size**: 224×224×3 (RGB images)
- **Transfer Learning**: Freezes all VGG16 layers
- **Classifier Head**: 
  - Flatten layer
  - Dense layer with 3 units (softmax activation)
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: SGD (Stochastic Gradient Descent)
- **Learning Rate**: 0.01

## 📊 Training Pipeline

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

## 🌐 API Endpoints

### `GET /`
Returns the web interface for image upload and prediction.

### `POST /predict`
Accepts a base64-encoded image and returns classification result.

### `GET/POST /train`
Initiates model training (runs `main.py`).

## 📈 Results

Current model performance (from `scores.json`):
- **Loss**: 6.88
- **Accuracy**: ~60.6%

*Note: Performance can be improved by adjusting hyperparameters, increasing epochs, or fine-tuning the model architecture.*

## 🔄 Project Workflow

```
Data Ingestion → Base Model Prep → Training → Evaluation
     ↓                ↓                ↓            ↓
Download data    Load VGG16      Train model   Save metrics
Extract data     Add classifier  Augment data  scores.json
                 Freeze layers    Callbacks
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vineeth John**
- GitHub: [@Vineeth-john](https://github.com/Vineeth-john)

## 🙏 Acknowledgments

- TensorFlow team for the Keras API
- VGG16 pre-trained weights from ImageNet
- The open-source community for amazing tools and libraries

---

⭐ If you found this project helpful, please consider giving it a star!
