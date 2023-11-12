Solución Fire-Incidents Esta solución fue creada en base al requerimiento solicitado, en el cual se extrajo información de la API obtenida de fire-incidents, en donde se desarrolló un modelo ELT, el cual extrae información de la API y luego los distribuye en Data Frames los cuales están compuestos de la siguiente manera:

  df_distrito
  df_batallon
  df_periodo_tiempo
  df_incidente
Luego cada uno de estos Data Frames son exportados a CSV en la carpeta Data Warehouse y son equivalentes a lo siguiente:

  df_distrito = Dim_distrito
  df_batallon = Dim_Batallon
  df_periodo_tiempo = dim_periodo_tiempo
  df_incidente = Hechos_incidente
*Para la ejecución del programa, se debe descargar la carpeta directamente al disco C , y se debe importar al programador de tareas de Windows el archivo "Ejecutar_Script_ELT.xml", el cual permite realizar una ejecución diaria a las 08:00 am.

*También el script puede ser ejecutado directamente desde la carpeta output, en donde se encuentra almacenado el archivo ejecutable llamado "API"
