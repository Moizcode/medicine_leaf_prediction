import torch
from torchvision import transforms
from PIL import Image
import pickle as pkl
import torch.nn.functional as F
import torch.nn as nn
import os

# Load the model
class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3)
        self.bn1 = nn.BatchNorm2d(32)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2 = nn.Conv2d(32, 32, kernel_size=3)
        self.bn2 = nn.BatchNorm2d(32)

        self.conv3 = nn.Conv2d(32, 64, kernel_size=5)
        self.bn3 = nn.BatchNorm2d(64)

        self.conv4 = nn.Conv2d(64, 64, kernel_size=5)
        self.bn4 = nn.BatchNorm2d(64)

        self._to_linear = None
        self.convs = nn.Sequential(
            self.conv1,
            self.bn1,
            nn.ReLU(),
            self.pool,
            self.conv2,
            self.bn2,
            nn.ReLU(),
            self.pool,
            self.conv3,
            self.bn3,
            nn.ReLU(),
            self.pool,
            self.conv4,
            self.bn4,
            nn.ReLU()
        )
        self._get_conv_output_shape()

        self.fc1 = nn.Linear(self._to_linear, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, num_classes)

    def _get_conv_output_shape(self):
        with torch.no_grad():
            x = torch.randn(1, 3, 300, 400)
            x = self.convs(x)
            self._to_linear = x.shape[1] * x.shape[2] * x.shape[3]

    def forward(self, x):
        x = self.convs(x)
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


NUM_CLASSES = 30
model = CNN(NUM_CLASSES)
model.load_state_dict(torch.load(
    r'/app/Model/best_model.pth'))
model.eval()

# Load class to number mapping
with open(r"/app/Model/class_to_number.pkl", 'rb') as file:
    clss_to_number = pkl.load(file)

# Inverse mapping
number_to_class = {v: k for k, v in clss_to_number.items()}

# Preprocessing function


def preprocess_image(image, target_size=(400, 300)):
    preprocess = transforms.Compose([
        transforms.Resize(target_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                             0.229, 0.224, 0.225]),
    ])
    image = preprocess(image).unsqueeze(0)  # Add batch dimension
    return image


def leaf_recognition(image_path):
    image = Image.open(image_path)  # Ensure the image is loaded as a PIL image
    image = preprocess_image(image)
    with torch.no_grad():
        outputs = model(image)
        _, predicted_class_index = torch.max(outputs, 1)
        predicted_label = number_to_class[predicted_class_index.item()]
        prediction_score = F.softmax(outputs, dim=1)[
            0][predicted_class_index].item()
    return predicted_label, prediction_score
