import requests
import json
import pandas as pd

####### Lectura de API y almacenamiento de datos en Data Frame ###### 
response = requests.get(url="https://data.sfgov.org/resource/wr8u-xric.json")
datos = json.loads(response.text)
df = pd.DataFrame(datos)


####### Dimension Distrito ###### 
df_distrito = df.loc[:,['neighborhood_district','point']]
df_distrito = df_distrito.reset_index(drop=True)
df_distrito.reset_index(level=0, inplace=True)
df_distrito['index']+=1
df_distrito=df_distrito.rename(columns={'index':'Id_code_distrito'})
print(df_distrito)

####### Dimension Batallon ###### 
df_batallon = df.loc[:,['battalion','station_area']]
df_batallon = df_batallon.reset_index(drop=True)
df_batallon.reset_index(level=0, inplace=True)
df_batallon['index']+=1
df_batallon=df_batallon.rename(columns={'index':'Id_code_batallon'})
print(df_batallon)

####### Dimension Periodo Tiempo ###### 
df_periodo_tiempo = df.loc[:,['incident_date','alarm_dttm','arrival_dttm','close_dttm']]
print(df_periodo_tiempo)

####### Tabla de Hechos Incidente ###### 
df_incidente = df.loc[:,['neighborhood_district','battalion','incident_date']]
df_incidente = pd.merge(df_incidente,df_distrito, on ='neighborhood_district', how='right')
df_incidente = pd.merge(df_incidente,df_batallon, on ='battalion', how='right')
df_incidente = df_incidente[['Id_code_distrito','Id_code_batallon','incident_date']]
print(df_incidente)

####### Exportar Dimensiones y tabla de hechos(Datawarehouse) a CSV ###### 
df_distrito.to_csv('C:/fire-incidents/Datawarehouse/dim_distrito.csv', index = False, sep=';', encoding='utf-8')  #Cambiar ruta en donde almacenen el proyecto para la exportación del archivo.
df_batallon.to_csv('C:/fire-incidents/Datawarehouse/dim_batallon.csv', index = False, sep=';', encoding='utf-8')  #Cambiar ruta en donde almacenen el proyecto para la exportación del archivo.
df_periodo_tiempo.to_csv('C:/fire-incidents/Datawarehouse/dim_periodo_tiempo.csv', index = False, sep=';', encoding='utf-8') #Cambiar ruta en donde almacenen el proyecto para la exportación del archivo.
df_incidente.to_csv('C:/fire-incidents/Datawarehouse/Hechos_incidente.csv', index = False, sep=';', encoding='utf-8') #Cambiar ruta en donde almacenen el proyecto para la exportación del archivo.

