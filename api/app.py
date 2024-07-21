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
    '(86922.5, 98201.0]': 2,
    '(30057.999, 86922.5]': 1,
    '(98201.0, 1479620.0]': 3
}
mapeamento_spending = {
    '(43.0, 52.495]': 2,
    '(0.999, 43.0]': 1,
    '(61.4, 100.0]': 3,
    '(52.495, 61.4]': 2
}

mapeamento_purchase_frequency ={
    '(25.5, 26.019]': 2,
    '(0.999, 25.5]': 1,
    '(27.0, 50.0]': 3,
    '(26.019, 27.0]': 3
}

mapeamento_membership_years = {
    '(5.0, 5.529]': 2,
    '(0.999, 5.0]': 1,
    '(6.0, 10.0]': 3,
    '(5.529, 6.0]': 3}

mapeamento_last_purchase_amount = {
    '(498.877, 502.135]': 2,
    '(10.399000000000001, 498.877]': 1,
    '(502.135, 998.51]': 3
}

mapeamento_score_final = {
    '(5.999, 9.0]': 'bronze',
    '(9.0, 11.0]': 'prata',
    '(11.0, 15.0]': 'ouro'
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
