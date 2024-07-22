import joblib
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from transform.transform_functions import *
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer



new_data = pd.read_csv('new_data.csv')

new_data = new_data.drop('id', axis=1)

round_coluna(new_data,'age')
transform_int(new_data,'age')
transform_int(new_data,'income')

new_data = new_data[new_data['spending_score'] <= 100]


# Carregar o modelo salvo
kmeans_loaded = joblib.load('kmeans_pipeline.pkl')



numeric_features = ['age', 'membership_years', 'income', 'purchase_frequency', 'last_purchase_amount', 'spending_score']
categorical_features = ['gender', 'preferred_category']



numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(sparse_output=False)


preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])


# Supondo que novos dados são recebidos em um DataFrame 'new_data'
# Processar e classificar novos dados
cluster_labels = {0: 'ouro', 1: 'prata', 2: 'bronze'}

new_data['cluster'] = kmeans_loaded.predict(new_data)
new_data['cluster_label'] = new_data['cluster'].map(cluster_labels)

# Exibir os resultados
print(new_data)
