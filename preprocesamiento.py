import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta)

def limpiar_datos(df):
    return df.dropna()

def normalizar(df):
    return (df - df.min()) / (df.max() - df.min())

def preprocesar(ruta):
    df = cargar_datos(ruta)
    df = limpiar_datos(df)
    df = normalizar(df)
    return df
