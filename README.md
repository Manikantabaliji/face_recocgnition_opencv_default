# face_recocgnition_opencv_default


Face Recognition System

This repository contains scripts for training a face recognition model and using it for face recognition on images.

Prerequisites:

- Python 3.x
- OpenCV (cv2 package)

Getting Started:

1. Clone this repository to your local machine:
   git clone https://github.com/Manikantabaliji/face_recocgnition_opencv_default/your-repo.git
   cd your-repo

2. Install the required dependencies:
   pip install opencv-python

3. Prepare your dataset:
   - Organize your face images in the 'images' directory located at 'D:/Face_rec'.
   - Each person's images should be placed in a separate subdirectory under the 'images' directory, named after the person.

   Example directory structure:
   D:/Face_rec/images/
   ├── person1/
   │   ├── image1.jpg
   │   ├── image2.jpg
   │   └── ...
   ├── person2/
   │   ├── image1.jpg
   │   ├── image2.jpg
   │   └── ...
   └── ...

Training (train.py):

1. Open the 'train.py' script and update the following variables if needed:
   - DIR: The directory containing your images.
   - haar_cascade: Path to the Haar Cascade XML file for face detection.

2. Run the training script:
   python train.py
   This script will process the images, detect faces, and train the LBPH face recognition model. The trained model will be saved as 'face_trained.yml'.

Face Recognition (face_recognition.py):

1. Open the 'face_recognition.py' script and make sure you've trained the model using the previous step.

2. Update the path to the trained model YAML file 'face_trained.yml'.

3. Run the face recognition script:
   python face_recognition.py
   This script will load the trained model and perform face recognition on a sample image provided in the script. Detected faces will be labeled with the recognized person's name.

Notes:

- Each subdirectory under the 'images' directory is assumed to correspond to a unique person, with the images inside representing that person.
- You can modify the sample image path in 'face_recognition.py' to test the face recognition on your own images.


