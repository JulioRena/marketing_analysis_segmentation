from transform_functions import *
import pandas as pd

df = pd.read_csv(r'C:\Users\julio\marketing_analysis\customer_dataset.csv')

tratar_nulos_media(df=df, colunas=['income','spending_score','membership_years','purchase_frequency','last_purchase_amount','age'])
#print(df['age'].value_counts())
round_coluna(df,'age')
#print(df['age'].value_counts())
#print(df['age'].info())

transform_int(df,'age')
transform_int(df,'income')

# female = ['female', 'F']
# male = ['male', 'M', 'M ']

# padronizar_cat(df, 'gender', female, 'Female')

# padronizar_cat(df,'gender', male, 'Male')


df['gender'] = df['gender'].replace('female', 'Female')
df['gender'] = df['gender'].replace('F', 'Female')
df['gender'] = df['gender'].replace('M', 'Male')
df['gender'] = df['gender'].replace('male', 'Male')

fillna_cat(df,'gender','Unknown')
fillna_cat(df,'preferred_category','Unknown')


df = df[df['spending_score'] <= 100]



#income:  bins=4, com 3 valores
transform_qcut(df, 'income_qcut', 'income', 4, ['baixo','médio','alto'])
mapeamento = {
    'baixo': 1,
    'médio': 2,
    'alto': 3
}
map_score(df, 'income_level', 'income_qcut', mapeamento)

#spending score: bins=3, com 2 valores
transform_qcut(df, 'spending_qcut', 'spending_score', 3, ['baixo','alto'])
mapeamento = {
    'baixo': 1,
    'alto': 2
}
map_score(df, 'spending_score_level', 'spending_qcut', mapeamento)


#purchase frequency: bins=3, com 2 valores
transform_qcut(df, 'purchase_frequency_qcut', 'purchase_frequency', 3, ['baixo','alto'])
mapeamento = {
    'baixo': 1,
    'alto': 2
}
map_score(df, 'purchase_frequency_level', 'purchase_frequency_qcut', mapeamento)


#membership_years: bins=3, com 2 valores
transform_qcut(df, 'membership_years_qcut', 'membership_years', 3, ['baixo','alto'])
mapeamento = {
    'baixo': 1,
    'alto': 2
}
map_score(df, 'membership_years_level', 'membership_years_qcut', mapeamento)


#last_purchase_amount: bins=3, com 2 valores
transform_qcut(df, 'last_purchase_amount_qcut', 'last_purchase_amount', 2, ['baixo','alto'])
mapeamento = {
    'baixo': 1,
    'alto': 2
}
map_score(df, 'last_purchase_amount_qcut_level', 'last_purchase_amount_qcut', mapeamento)


df['score_final'] = df['last_purchase_amount_qcut_level'] + df['membership_years_level'] + df['purchase_frequency_level'] + df['spending_score_level'] + df['income_level']



#transformando coluna final de segmentação de clientes

transform_qcut(df, 'score_final_qcut', 'score_final', 3, ['bronze','prata','ouro'])

df = df.drop('id', axis=1)
df.to_csv('base_tratada.csv')





