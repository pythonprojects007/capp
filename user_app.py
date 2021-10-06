import streamlit
import numpy
from PIL import Image
from google.cloud import storage
from firebase import firebase
import os,datetime
from Crypto.PublicKey import RSA
img_file_buffer = streamlit.file_uploader("Upload an image")
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    print(image)
    image.save("upload.jpg")
    streamlit.image(image)
    input_image = numpy.array(image)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cartoonifier-521b7-f1585f752196.json"
    # firebase = firebase.FirebaseApplication('https://plenary-ridge-832.firebaseio.com/')
    firebase = firebase.FirebaseApplication('https://cartoonifier-521b7.firebaseio.com/')
    client = storage.Client()
    bucket = client.get_bucket("cartoonifier-521b7.appspot.com")
    # bucket = client.get_bucket("plenary-ridge-832.appspot.com")
    # imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
    imageBlob = bucket.blob("uploaded_image")
    print(imageBlob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'))
    imageBlob.upload_from_filename('upload.jpg')