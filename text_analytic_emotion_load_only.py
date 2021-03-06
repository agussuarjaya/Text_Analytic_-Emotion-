# -*- coding: utf-8 -*-
"""Text Analytic (Emotion) - load_only.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ec4JMQZ5zoj-PB_a0mUkJWRKotgQSd9f
"""

"""

  Text Analytic (Emotion) with TensorFlow
 
  Copyright 2020  I Made Agus Dwi Suarjaya
                  Gede Ocha Dipa Ananda
                  Ni Luh Putu Diah Putri Maheswari

  Description     : Try to analyze Tweets with TensorFlow and classify into 5 emotions (anger, happiness, sadness, love, fear)
  Dataset source  : https://raw.githubusercontent.com/meisaputri21/Indonesian-Twitter-Emotion-Dataset/master/Twitter_Emotion_Dataset.csv

"""

#Setup
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

import csv
import time
import ast

import numpy as np
import pandas as pd

#--------------------------------------------------------------------------------------------------------------------------
model_path = './1585378332_model'
encoder_path = './1585378332_encoder'
dict_path = './1585378332_dict'

#--------------------------------------------------------------------------------------------------------------------------

#Load the model (Optional for Transfer Learning)
reloaded_model = tf.keras.models.load_model(model_path)
model = reloaded_model

#Load the encoder (Optional for Transfer Learning)
encoder = tfds.features.text.TokenTextEncoder.load_from_file(encoder_path)

#Load the dictionary (Optional for Transfer Learning)
with open(dict_path) as dict_file:
    d = ast.literal_eval(dict_file.readline())

#Classify some tweets with model predict
tweet = []
tweet.append('Tahukah kamu, bahwa saat itu papa memejamkan matanya dan menahan gejolak dan batinnya. Bahwa papa sangat ingin mengikuti keinginanmu tapu lagi-lagi dia HARUS menjagamu?')
tweet.append('[Idm] My, masa gua tadi ketemu tmn SD yg pas SD ngejar gua dan ngasih surat tiap minggunya, asdfghjkl bgt, gk tau knp ngerasa takut gua :v hadeuh jaman SD ngerti apa coba :v')
tweet.append('Sedih bny penulisan resep yg tidak baku sdm, sdt, ruas, sejumput, secukupnya, even biji/buah termasuk tidak baku :(')
tweet.append('Paling nyampah org suka compare kan aku dgn org lain, dia dia ah aku aku ah. Tak suka boleh blah lah -__-')
tweet.append('Agak telat ramai nya ya dok...sudah paham sejak lama banget jadi geli aja baru pada ramai sekarang hehehe...')

for text in range(len(tweet)):
  predictions = model.predict(encoder.encode(tweet[text]))
  predictions[0]
  print(d[np.argmax(predictions[0])], ' <- ', tweet[text])
