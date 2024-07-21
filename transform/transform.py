from transform_functions import *
import pandas as pd

df = pd.read_csv(r'C:\Users\julio\marketing_analysis\customer_dataset.csv')

tratar_nulos_media(df=df, colunas=['income','spending_score','membership_years','purchase_frequency','last_purchase_amount','age'])

round_coluna(df,'age')
transform_int(df,'age')
transform_int(df,'income')

df['gender'] = df['gender'].replace('female', 'Female')
df['gender'] = df['gender'].replace('F', 'Female')
df['gender'] = df['gender'].replace('M', 'Male')
df['gender'] = df['gender'].replace('male', 'Male')

fillna_cat(df,'gender','Unknown')
fillna_cat(df,'preferred_category','Unknown')

df = df[df['spending_score'] <= 100]

transform_qcut(df, 'income_qcut', 'income', 4)
mapeamento = {
    '(86922.5, 98201.0]':2,
    '(30057.999, 86922.5]':1,
    '(98201.0, 1479620.0]':3
}

map_score(df, 'income_level', 'income_qcut', mapeamento)


#spending score: bins=3, com 2 valores
transform_qcut(df, 'spending_qcut', 'spending_score', 5)
mapeamento = {
'(43.0, 52.495]': 2,
'(0.999, 43.0]':1,
'(61.4, 100.0]':3,
'(52.495, 61.4]':2
}
map_score(df, 'spending_score_level', 'spending_qcut', mapeamento)


#purchase frequency: bins=3, com 2 valores
transform_qcut(df, 'purchase_frequency_qcut', 'purchase_frequency', 4)
mapeamento = {   
    '(25.5, 26.019]':2, 
    '(0.999, 25.5]':1,  
    '(27.0, 50.0]':3,   
    '(26.019, 27.0]': 3
}
map_score(df, 'purchase_frequency_level', 'purchase_frequency_qcut', mapeamento)


#membership_years: bins=3, com 2 valores
transform_qcut(df, 'membership_years_qcut', 'membership_years', 5)
mapeamento = {
    '(5.0, 5.529]':2,
    '(0.999, 5.0]':1,
    '(6.0, 10.0]':3,
    '(5.529, 6.0]':3
}

map_score(df, 'membership_years_level', 'membership_years_qcut', mapeamento)


#last_purchase_amount: bins=3, com 2 valores
transform_qcut(df, 'last_purchase_amount_qcut', 'last_purchase_amount', 4)
mapeamento = {
    '(498.877, 502.135]':2,
    '(10.399000000000001, 498.877]': 1,
    '(502.135, 998.51]': 3
}

map_score(df, 'last_purchase_amount_qcut_level', 'last_purchase_amount_qcut', mapeamento)




df['score_final'] = df['last_purchase_amount_qcut_level'] + df['membership_years_level'] + df['purchase_frequency_level'] + df['spending_score_level'] + df['income_level']


transform_qcut(df, 'score_final_qcut', 'score_final', 3)

#%%
mapeamento = {
    '(5.999, 9.0]': 'bronze',
    '(9.0, 11.0]': 'prata',
    '(11.0, 15.0]':'ouro'
}

map_score(df, 'score_final_qcut_level', 'score_final_qcut', mapeamento)



df = df.drop('id', axis=1)
df.to_csv('base_tratada.csv',index=False)





