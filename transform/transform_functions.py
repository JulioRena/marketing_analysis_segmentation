import pandas as pd


#df = pd.read_csv(r'C:\Users\julio\marketing_analysis\customer_dataset.csv')



def tratar_nulos_media(df, colunas):
    for i in colunas:
        df[i] = df[i].fillna(df[i].mean())
        #return df[i].info()
        
#tratar_nulos_media(df=df, colunas=['income','spending_score','membership_years','purchase_frequency','last_purchase_amount','age'])

#transformando valores categoricos
#female = ['female', 'F']
#male = ['male', 'M', 'M ']

def padronizar_cat(df, coluna, lista_valores, valor):
    for i in lista_valores:
        df[coluna] = df[coluna].replace(i, valor)
        return df[coluna].value_counts()
    
#padronizar_cat(df, 'gender', female, 'Female')

#padronizar_cat(df,'gender', male, 'Male')

def fillna_cat(df,coluna,valor):
    df[coluna] = df[coluna].fillna(valor)
    return df[coluna].info()
    
def round_coluna(df, coluna):
    df[coluna] = df[coluna].round()
    return df[coluna].info()

def transform_int(df,coluna):
    df[coluna] = df[coluna].astype(int)
    return df[coluna].info()
  
  

 
def transform_qcut(df, coluna_nova, coluna, n_bins, lista_categoria):
    df[coluna_nova],bins = pd.qcut(df[coluna], q=n_bins, labels=lista_categoria,retbins=True, duplicates='drop')
    df[f'{coluna_nova}_val'] = pd.qcut(df[coluna], q=n_bins, duplicates='drop')
    
def map_score(df, coluna_nova, coluna, mapeamento):
    df[coluna_nova] = df[coluna].astype(str).map(mapeamento)
    
# def qcut_transform(df, coluna_nova, coluna, n_bins):
#     df[coluna_nova] = pd.qcut(df[coluna], q=n_bins, labels=False,duplicates='drop')
#     if df[coluna_nova].shape[0] == 3:
#         label_map = {0:'baixo', 1:'médio', 2: 'alto'}
#         df[coluna_nova] = df[coluna_nova].map(label_map)
#         mapeamento = {'baixo': 0,'médio': 1,'alto': 2}
#         df[f'{coluna_nova}_map'] = df[coluna_nova].astype(str).map(mapeamento)



