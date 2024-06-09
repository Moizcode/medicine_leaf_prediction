# Medicine Leaf Prediction

Welcome to the Medicine Leaf Prediction project! This project uses a Convolutional Neural Network (CNN) built with PyTorch to classify 30 different classes of medicinal leaves. The application is served using a Django backend and a Bootstrap frontend. Docker is used for containerization to ensure consistency across different deployment environments.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

This project aims to classify medicinal leaves into 30 different categories using a deep learning model. The core components of the project include:

- A CNN model built with PyTorch for leaf classification.
- A Django backend that serves the model and handles requests.
- A Bootstrap-based frontend for a user-friendly interface.
- Docker for containerization, ensuring a consistent environment for deployment.

## Features

- **Accurate Classification**: Utilizes a CNN for high-accuracy classification of medicinal leaves.
- **Web Interface**: User-friendly web interface built with Django and Bootstrap.
- **Containerization**: Dockerized application for easy deployment and scalability.

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- Docker

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Moizcode/medicine-leaf-prediction.git
   cd medicine-leaf-prediction
   ```

2. **Build and run the Docker container:**
   ```bash
   docker build -t "leafimagename" .
   docker run -p 8000:8000 "leafimagename"
   ```

3. **Access the application:**
   Open your web browser and go to `http://localhost:8000`.

## Usage

1. **Upload an Image**: Use the web interface to upload an image of a medicinal leaf.
2. **Get Prediction**: The model will process the image and provide a classification result.
3. **View Results**: The classification result will be displayed on the web interface.

## Model Details

The CNN model is built using PyTorch and trained on a dataset of medicinal leaf images. The model architecture includes several convolutional layers, pooling layers, and fully connected layers to achieve high accuracy in classification tasks.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please ensure your code adheres to our coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the PyTorch team for creating an excellent deep learning framework.
- Special thanks to the Django and Bootstrap communities for their robust tools and documentation.
- Credit to all contributors and users who have helped improve this project.
