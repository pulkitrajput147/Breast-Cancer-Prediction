# -*- coding: utf-8 -*-
"""Breast_cancer.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HmGE3r_f5jJb-oA5TRF_SOw3IMWor4x6
"""

pip install streamlit

!pip install pyngrok

import streamlit as st

import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("/content/breast_cancer_detection.pickle", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"


def predict_note_authentication(mean radius,mean texture,mean perimeter,mean area,mean smoothness,mean compactness,mean concavity,mean concave points,mean symmetry,mean fractal dimension,radius error,texture error,perimeter error,area error,smoothness error,compactness error,concavity error,concave points error,symmetry error,fractal dimension error,worst radius,worst texture,worst perimeter,worst area,worst smoothness,worst compactness,worst concavity,worst concave points,worst symmetry,worst fractal dimension):
    prediction = classifier.predict([[mean radius,mean texture,mean perimeter,mean area,mean smoothness,mean compactness,mean concavity,mean concave points,mean symmetry,mean fractal dimension,radius error,texture error,perimeter error,area error,smoothness error,compactness error,concavity error,concave points error,symmetry error,fractal dimension error,worst radius,worst texture,worst perimeter,worst area,worst smoothness,worst compactness,worst concavity,worst concave points,worst symmetry,worst fractal dimension]])
    print(prediction)
    return prediction


def main():
    st.title("Breast Cancer Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Breast Cancer Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    mean radius = st.text_input("mean radius", "Type Here")
    mean texture = st.text_input("mean texture", "Type Here")
    mean perimeter = st.text_input("mean perimeter", "Type Here")
    mean area = st.text_input("mean area", "Type Here")
    mean smoothness = st.text_input("mean smoothness", "Type Here")
    mean compactness = st.text_input("mean compactness", "Type Here")
    mean concavity = st.text_input(" mean concavity", "Type Here")
    mean concave points = st.text_input("mean concave points", "Type Here")
    mean symmetry  = st.text_input("mean symmetry", "Type Here")
    mean fractal dimension = st.text_input("mean fractal dimension", "Type Here")
    radius error = st.text_input("radius error", "Type Here")
    texture error= st.text_input("texture error", "Type Here")
    perimeter error= st.text_input("perimeter error", "Type Here")
    area error  = st.text_input("area error", "Type Here")
    smoothness error  = st.text_input("smoothness error", "Type Here")
    compactness error = st.text_input(" compactness error ", "Type Here")
    concavity error = st.text_input("concavity error", "Type Here")
    concave points error = st.text_input("concave points error ", "Type Here")
    symmetry error= st.text_input("symmetry error", "Type Here")
    fractal dimension error = st.text_input("fractal dimension error", "Type Here")
    worst radius = st.text_input("worst radius", "Type Here")
    worst texture  = st.text_input("worst texture", "Type Here")
    worst perimeter  = st.text_input("worst perimeter", "Type Here")
    worst area = st.text_input("worst area", "Type Here")
    worst smoothness = st.text_input("worst smoothness", "Type Here")
    worst compactness= st.text_input("worst compactness", "Type Here")
    worst concavity = st.text_input("worst concavity", "Type Here")
    worst concave points  = st.text_input("worst concave points", "Type Here")
    worst symmetry= st.text_input("worst symmetry", "Type Here")
    worst fractal dimension	 = st.text_input("worst fractal dimension", "Type Here")

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(mean radius,mean texture,mean perimeter,mean area,mean smoothness,mean compactness,mean concavity,mean concave points,mean symmetry,mean fractal dimension,radius error,texture error,perimeter error,area error,smoothness error,compactness error,concavity error,concave points error,symmetry error,fractal dimension error,worst radius,worst texture,worst perimeter,worst area,worst smoothness,worst compactness,worst concavity,worst concave points,worst symmetry,worst fractal dimension)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()

