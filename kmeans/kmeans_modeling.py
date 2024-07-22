import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from transform.transform_functions import *
import joblib

df = pd.read_csv(r'C:\Users\julio\marketing_analysis\customer_data_2.csv')
df = df.drop('id', axis=1)

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



numeric_features = ['age', 'membership_years', 'income', 'purchase_frequency', 'last_purchase_amount', 'spending_score']
categorical_features = ['gender', 'preferred_category']



numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(sparse_output=False)


preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Criando o modelo KMeans em um pipeline
kmeans = Pipeline(steps=[('preprocessor', preprocessor),
                         ('clusterer', KMeans(n_clusters=3, random_state=42))])


kmeans.fit(df)

df['cluster'] = kmeans['clusterer'].labels_


numeric_summary = df.groupby('cluster')[numeric_features].mean()


cluster_labels = {0: 'ouro', 1: 'prata', 2: 'bronze'}
df['cluster_label'] = df['cluster'].map(cluster_labels)

print(df[['age', 'gender', 'preferred_category', 'membership_years', 'income', 'purchase_frequency', 'last_purchase_amount', 'spending_score', 'cluster_label']])

joblib.dump(kmeans, 'kmeans_pipeline.pkl')