# :book:  Text Translation Glasses  :eyeglasses:
<h2>:memo:  Abstract</h2>

This project is an attempt in this direction to build a novel smart glass which has the ability to extract and recognize text captured from an image and convert it to speech. **_OpenCV_** is an open source Computer Vision Library in which we can use many image related operations, in this project it is used to capture and modify real-time text from external camera. The text captured and modified is then processed by **_Tesseract-OCR_** and Efficient and Accurate Scene Text Detector (EAST) based on Deep Learning techniques to give output as coputer generated text. For actual Translation of text in many different languages is done by **_Natural Language Processing (NLP)_** a part of ML in which data sets of different language translations are given to train the model. After all this IoT part kicks in (It consists of a **_Raspberry Pi Zero_** microcontroller which processes the image captured from a **_Pi camera_** superimposed on the glasses of the person) as the actual hardware takes care of all the operations and algorithms to perform in small computer and can be wear as regular glasses. The recognized text is further processed by **_Google's Text to Speech (GTTS) API_** to convert to an audible signal for the user.   

<h2>:man_technologist:  Technologies and Hardware we are using</h2>

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/OpenCV-0099E5?style=for-the-badge&logo=opencv&logoColor=white"/> <img src="https://img.shields.io/badge/Raspberry Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi&logoColor=white"/> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google-Colab&logoColor=white"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/> <img src="https://img.shields.io/badge/PyCharm-76B900?style=for-the-badge&logo=pycharm&logoColor=white"/>

<h2>:scroll:  Project Illustrations</h2>


<br>    

> Input of the image captured by the camera (here Pi Cam).        
<br>   
<img src="https://github.com/ShubhamGupta577/Text-Translation-Glasses/blob/main/Assets/Image_1.png" alt="Illustration1"/>      
<br>

> Removing noise from the image using OpenCV and converting it to Text using pyTesseract.       
<br>
<img src="https://github.com/ShubhamGupta577/Text-Translation-Glasses/blob/main/Assets/Image_2.png" alt="Illustration2"/>    
<br>

> Translating the text using NLP trained dataset to other languages (here Spanish).          
<br>    
<img src="https://github.com/ShubhamGupta577/Text-Translation-Glasses/blob/main/Assets/Image_3.png" alt="Illustration3"/>    
<br>  

> Conversion of translated text using GTTS to speech.          
<br>    
<img src="https://github.com/ShubhamGupta577/Text-Translation-Glasses/blob/main/Assets/Image_4.png" alt="Illustration4" width="1000px"/>    
<br>  

[```Back to Top```](#)
