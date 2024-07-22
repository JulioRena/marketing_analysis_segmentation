import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from transform.transform_functions import *
from .maping import encontrar_valor_intervalo

from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
import numpy as np
app = FastAPI()

class InputData(BaseModel):
    income: float
    spending_score: float
    membership_years: float
    purchase_frequency: float
    last_purchase_amount: float

mapeamento_income ={
    '(60038.5, 92031.0]':2,
    '(30003.999, 60038.5]':1,
    '(92031.0, 115854.0]':3,
    '(115854.0, 1329680.0]':4
}
mapeamento_spending = {
    '(27.0, 54.932]': 2,
    '(0.999, 27.0]':1,
    '(75.0, 100.0]':4,
    '(54.932, 75.0]':3
}

mapeamento_purchase_frequency ={
    '(15.5, 26.514]':2, 
    '(0.999, 15.5]':1,  
    '(26.514, 38.0]':3,   
    '(38.0, 50.0]': 4
}

mapeamento_membership_years = {
    '(3.0, 5.46]':2,
    '(0.999, 3.0]':1,
    '(5.46, 8.0]':3,
    '(8.0, 10.0]':4
}

mapeamento_last_purchase_amount = {
    '(232.75, 492.32]':2,
    '(10.399000000000001, 232.75]': 1,
    '(492.32, 736.37]': 3,
    '(736.37, 998.98]':4
}

mapeamento_score_final = {
    '(5.999, 11.0]': 'bronze',
    '(11.0, 13.0]': 'prata',
    '(13.0, 20.0]':'ouro'
}

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    
    df['last_purchase_amount_qcut_level'] = encontrar_valor_intervalo(df['last_purchase_amount'][0], mapeamento_last_purchase_amount)
    df['membership_years_level'] = encontrar_valor_intervalo(df['membership_years'][0], mapeamento_membership_years)
    df['purchase_frequency_level'] = encontrar_valor_intervalo(df['purchase_frequency'][0], mapeamento_purchase_frequency)
    df['spending_score_level'] = encontrar_valor_intervalo(df['spending_score'][0], mapeamento_spending)
    df['income_level'] = encontrar_valor_intervalo(df['income'][0], mapeamento_income)

    df['score_final'] = (df['last_purchase_amount_qcut_level'] + 
                        df['membership_years_level'] + 
                        df['purchase_frequency_level'] + 
                        df['spending_score_level'] + 
                        df['income_level'])

    df['score_final_qcut_level'] = encontrar_valor_intervalo(df['score_final'][0], mapeamento_score_final)
    
    return {"Cluster": df['score_final_qcut_level'][0]}
