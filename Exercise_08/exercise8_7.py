# Kokeile käyttää jotain Pythonille löytyvää kuvantunnistuskirjastoa,
# ja kokeile sen toimintaa erilaisilla valokuvilla
# Tarvittava tekniikka tässä tapauksessa on nimeltään ”image recognition”

# Kun etsit Googlesta "python 3 image recognition module", ensimmäinen linkki sanoo:
# Popular Python Image Recognition Libraries:
# - OpenCV (Open Source Computer Vision Library)
# - TensorFlow
# - Keras
# - PyTorch
# - Pillow (PIL Fork)

#----------------------------------------------------------------------------------------------------
# Esimerkki OpenCV:n käytöstä kasvojentunnistukseen:
import cv2

# Load the pre-trained cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the image
image = cv2.imread('example1.jpg') # Replace with the path to your image

# Convert the image to grayscale (necessary for detection)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use the face detector to find faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show the image with detected faces marked
cv2.imshow('Faces', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------------------
# Esimerkki PyTorchin käyttämisestä eläinten kuvien luokittelemiseen
import torch
from torchvision import models, transforms
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Load the pre-trained Faster R-CNN model
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()  # Switch the model to evaluation mode

# Load and transform the image
img = Image.open('example2.jpg')
img_tensor = transforms.ToTensor()(img).unsqueeze(0)  # Convert to tensor and add batch dimension

# Run the image through the model
with torch.no_grad():
    prediction = model(img_tensor)

# Extract the predictions
boxes = prediction[0]['boxes']
scores = prediction[0]['scores']

# Filter out boxes with low confidence
threshold = 0.5
filtered_boxes = boxes[scores > threshold]

# Draw the bounding boxes on the image
draw = ImageDraw.Draw(img)
for box in filtered_boxes:
    box = box.tolist()  # Convert to list
    draw.rectangle(box, outline="red", width=3)

# Display the image with bounding boxes
plt.imshow(img)
plt.axis('off')
plt.show()
