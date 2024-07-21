#%%
import sys
import os

# Adicione o diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora você deve conseguir importar o módulo
from transform.transform_functions import *

def encontrar_valor_intervalo(valor, mapeamento):
    # Ordena os intervalos por ordem crescente do limite inferior
    intervalos = sorted(mapeamento.keys(), key=lambda x: float(x.split(',')[0][1:]))
    
    for intervalo in intervalos:
        lim_inf, lim_sup = intervalo[1:-1].split(', ')
        lim_inf, lim_sup = float(lim_inf), float(lim_sup)
        if lim_inf < valor <= lim_sup:
            return mapeamento[intervalo]

    # Se o valor não estiver em nenhum intervalo, determina o menor ou maior intervalo
    menor_intervalo = intervalos[0]
    maior_intervalo = intervalos[-1]
    
    lim_inf_menor, lim_sup_menor = menor_intervalo[1:-1].split(', ')
    lim_inf_menor = float(lim_inf_menor)
    
    lim_inf_maior, lim_sup_maior = maior_intervalo[1:-1].split(', ')
    lim_sup_maior = float(lim_sup_maior)
    
    if valor <= lim_inf_menor:
        return mapeamento[menor_intervalo]
    else:
        return mapeamento[maior_intervalo]

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'income': [90000],
    'spending_score': [90, 85, 75, 65, 55],
    'membership_years': [5, 6, 7, 8, 9],
    'purchase_frequency': [12, 15, 18, 20, 25],
    'last_purchase_amount': [200, 250, 300, 350, 400],
    'score_final': [10, 11, 12, 13, 14]
})

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

valor = 1000
df['teste'] = encontrar_valor_intervalo(valor, mapeamento_last_purchase_amount)
