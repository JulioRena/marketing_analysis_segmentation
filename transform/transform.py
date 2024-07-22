from transform_functions import *
import pandas as pd

df = pd.read_csv(r'C:\Users\julio\marketing_analysis\customer_data_2.csv')

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
    '(60038.5, 92031.0]':2,
    '(30003.999, 60038.5]':1,
    '(92031.0, 115854.0]':3,
    '(115854.0, 1329680.0]':4
}

map_score(df, 'income_level', 'income_qcut', mapeamento)


#spending score: bins=3, com 2 valores
transform_qcut(df, 'spending_qcut', 'spending_score', 4)
mapeamento = {
'(27.0, 54.932]': 2,
'(0.999, 27.0]':1,
'(75.0, 100.0]':4,
'(54.932, 75.0]':3
}
map_score(df, 'spending_score_level', 'spending_qcut', mapeamento)


#purchase frequency: bins=3, com 2 valores
transform_qcut(df, 'purchase_frequency_qcut', 'purchase_frequency', 4)
mapeamento = {
    '(15.5, 26.514]':2, 
    '(0.999, 15.5]':1,  
    '(26.514, 38.0]':3,   
    '(38.0, 50.0]': 4
}
map_score(df, 'purchase_frequency_level', 'purchase_frequency_qcut', mapeamento)


#membership_years: bins=3, com 2 valores
transform_qcut(df, 'membership_years_qcut', 'membership_years', 4)
mapeamento = {
    '(3.0, 5.46]':2,
    '(0.999, 3.0]':1,
    '(5.46, 8.0]':3,
    '(8.0, 10.0]':4
}

map_score(df, 'membership_years_level', 'membership_years_qcut', mapeamento)


#last_purchase_amount: bins=4, com 4 valores
transform_qcut(df, 'last_purchase_amount_qcut', 'last_purchase_amount', 4)
mapeamento = {
    '(232.75, 492.32]':2,
    '(10.399000000000001, 232.75]': 1,
    '(492.32, 736.37]': 3,
    '(736.37, 998.98]':4
}

map_score(df, 'last_purchase_amount_qcut_level', 'last_purchase_amount_qcut', mapeamento)




df['score_final'] = df['last_purchase_amount_qcut_level'] + df['membership_years_level'] + df['purchase_frequency_level'] + df['spending_score_level'] + df['income_level']


transform_qcut(df, 'score_final_qcut', 'score_final', 3)


mapeamento = {
    '(5.999, 11.0]': 'bronze',
    '(11.0, 13.0]': 'prata',
    '(13.0, 20.0]':'ouro'
}

map_score(df, 'score_final_qcut_level', 'score_final_qcut', mapeamento)



df = df.drop('id', axis=1)
df.to_csv('base_tratada.csv',index=False)





