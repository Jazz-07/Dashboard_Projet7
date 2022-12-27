# Librairie 

import os, sys, time
import numpy as np
import pandas as pd
import streamlit as st


import re

st.title('Realiser un Dashboard')
# Données sur les caracterisques d'un client
st.subheader('Echantillon des données ')
df_client=pd.read_csv('data')
st.write(df_client.head())

from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve,confusion_matrix

# Classification Report
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score,accuracy_score

