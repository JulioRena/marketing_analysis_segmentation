import pandas as pd

def tratar_nulos_media(df, colunas):
    for i in colunas:
        df[i] = df[i].fillna(df[i].mean())

def padronizar_cat(df, coluna, lista_valores, valor):
    for i in lista_valores:
        df[coluna] = df[coluna].replace(i, valor)
        return df[coluna].value_counts()
    
def fillna_cat(df,coluna,valor):
    df[coluna] = df[coluna].fillna(valor)
    return df[coluna].info()
    
def round_coluna(df, coluna):
    df[coluna] = df[coluna].round()
    return df[coluna].info()

def transform_int(df,coluna):
    df[coluna] = df[coluna].astype(int)
    return df[coluna].info()
 
def transform_qcut(df, coluna_nova, coluna, n_bins):
    df[coluna_nova],bins = pd.qcut(df[coluna], q=n_bins,retbins=True, duplicates='drop')
    #df[f'{coluna_nova}_val'] = pd.qcut(df[coluna], q=n_bins, duplicates='drop')
 
    
def map_score(df, coluna_nova, coluna, mapeamento):
    df[coluna_nova] = df[coluna].astype(str).map(mapeamento)

 