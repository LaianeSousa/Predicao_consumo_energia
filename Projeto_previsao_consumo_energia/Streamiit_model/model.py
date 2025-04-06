# Importando pacotes necessários
import pandas as pd
import numpy as np
import math #fornece funções matemáticas e constantes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score # calcula o error do modelo
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.ensemble import RandomForestRegressor

warnings.filterwarnings("ignore")

def model_predictions(type_model, predictions):
    df = pd.read_csv('Energy_consumption_dataset.csv')
    df_copy = df.copy()

    # Mapeamento dos dias para valores numéricos
    day_mapping = {
        'Monday': 2,
        'Tuesday': 3,
        'Wednesday': 4,
        'Thursday': 5,
        'Friday': 6,
        'Saturday': 7,
        'Sunday': 1
    }

    df_copy['DayOfWeek'] = df['DayOfWeek'].map(day_mapping)
    df_copy['Holiday'] = df['Holiday'].map({'Yes': 1, 'No': 0})
    df_copy['HVACUsage']= df['HVACUsage'].map({'On': 1, 'Off': 0})
    df_copy['LightingUsage']= df['LightingUsage'].map({'On': 1, 'Off': 0})
    df_copy = df_copy.drop(columns=['RenewableEnergy', 'HVACUsage', 'SquareFootage' , 'Humidity'])  # apagando essas colunas      

    X = df_copy.iloc[:,:-1] # selecionar todas as colunas, exceto a ultima
    y = df_copy.iloc[:,-1] # selecionar a ultima coluna


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    if type_model == 'LinearRegression':
        model = LinearRegression()
        # Treinar o modelo com os dados de treino
        model.fit(X_train, y_train)

        # Fazer previsões nos dados de teste
        y_pred = model.predict(X_test)

        #new_data = np.array([[1,1,7,0,27.73,1,1]])
        new_prediction = model.predict(predictions)
        return new_prediction
    
   
    elif type_model == 'RandomForestRegressor':
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        #new_data = np.array([[1,1,7,0,27.73,1,1]])
        new_prediction = model.predict(predictions)
        return new_prediction
    
    else:
        return "Invalid model type. Please choose 'LinearRegression' or 'RandomForestRegressor'."
    