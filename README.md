# Flask OpenCV Image Analyzer

## Overview

Flask OpenCV Image Analyzer is a lightweight REST API built using Python, Flask, OpenCV, and NumPy. The application accepts a JPEG image through an HTTP POST request, processes the image using OpenCV, calculates its average brightness, draws a 100×100 bounding box at the center of the image, and returns the analysis result in JSON format.

This project was developed as part of a backend and computer vision learning exercise focused on API development, image processing, and server-side vision computation.


## Features

* REST API built with Flask
* JPEG image upload support
* Image decoding using OpenCV
* Grayscale image conversion
* Average brightness calculation
* Center-based 100×100 bounding box generation
* JSON response output
* Error handling for invalid or missing image uploads


## Tech Stack

### Backend

* Python 3.x
* Flask

### Computer Vision

* OpenCV

### Numerical Computing

* NumPy

### API Testing

* Postman


## Project Structure

flask-opencv-image-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/

> Note: The `venv` directory is excluded from version control using `.gitignore`.

## API Endpoint

### Analyze Image

**Endpoint**

POST /api/analyze

**Content Type**

multipart/form-data


**Request Parameter**

| Parameter | Type | Description     |
| --------- | ---- | --------------- |
| image     | File | JPEG image file |


## Sample Request

Using Postman:

1. Select POST method.
2. Enter the URL:

http://127.0.0.1:5000/api/analyze

3. Navigate to Body → form-data.
4. Add a key named `image`.
5. Set the type to `File`.
6. Upload a JPEG image.
7. Click Send.

## Sample Response

{
    "status": "processed",
    "brightness": 142.5
}


## Image Processing Workflow

Client Upload
      ->
Flask API Endpoint
      ->
Receive JPEG File
      ->
Convert Bytes to NumPy Array
      ->
Decode Image using OpenCV
      ->
Convert Image to Grayscale
      ->
Calculate Average Brightness
      ->
Draw Center Bounding Box
      ->
Return JSON Response


## Installation and Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd flask-opencv-image-analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
.\venv\Scripts\Activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
python app.py
```

Server starts at:

```text
http://127.0.0.1:5000
```


## Learning Outcomes

Through this project, the following concepts were explored:

* Flask application development
* REST API design
* HTTP POST requests
* File upload handling
* JSON response generation
* NumPy array manipulation
* OpenCV image processing
* Brightness analysis
* Bounding box generation
* API testing using Postman

## Future Enhancements

* Save processed images to disk
* Return annotated images to clients
* Integrate YOLOv8 object detection
* Add image quality metrics
* Containerize using Docker
* Deploy on cloud platforms


## Author

Anwesha Panda

B.Tech Computer Science and Engineering

Backend Development | Computer Vision | Machine Learning
