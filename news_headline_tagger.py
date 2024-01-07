import ttkbootstrap as ttk
import tkinter as tk
import pandas as pd
from tkinter import Tk
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
import os

model = tf.keras.models.load_model('D:/Web Development/News_Headline_Tagger/news_headlines.keras',{'KerasLayer':hub.KerasLayer})


def predict():
    
    prediction = model.predict([headline.get()])
    
    classes = ['business', 'entertainment', 'environment', 'health', 'politics','space', 'sports', 'technology']
    
    result.config(text=classes[prediction.argmax()])
    result.update()
    

root = ttk.Window(title="News Headline Tagger")

root.geometry('700x300')

headline_frame = ttk.Labelframe(root, text='Headline')
headline_frame.place(x=50,y=50)
headline = ttk.Entry(headline_frame,font=('Helvetica',14),width=40)
headline.pack(padx=5,pady=5)

submit = ttk.Button(text="Predict",style='primary',command=predict)
submit.place(x=550,y=70)

tag_frame = ttk.Labelframe(root, text='Tag')
tag_frame.place(x=50,y=150)
result = ttk.Label(tag_frame,font=('Helvetica',24), width=10)
result.pack(padx=5,pady=5)

root.mainloop()