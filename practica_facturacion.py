import pandas as pd

df= pd.read_excel('datos_facturacion.xlsx')
print(df.head())

filtro1=df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
print(filtro1)
filtro1.to_csv('practica_facturacion_1.csv')

filtro2 = df[~(df["CVE_VEND"] == 5.0 ) & ~(df["CVE_VEND"] == 4.0)]
print(filtro2)
filtro2.to_csv('practica_facturacion_2.csv')

filtro3=df[df["FECHA_ENT"] == '2022-28-2']
print(filtro3)
filtro3.to_csv('practica_facturacion_3.csv')

filtro4=df[(df["CAN_TOT"] < 5951.7)| (df["STATUS"] == "E")]
print(filtro4)
filtro4.to_csv('practica_facturacion_4.csv')

filtro5 = df.iloc[ : , [0, 6, 7,9]]  
print(filtro5)
filtro5.to_csv('practica_facturacion_5.csv')