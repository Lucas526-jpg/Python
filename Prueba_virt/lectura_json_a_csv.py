import json,csv,pymsgbox,sys  #importo librerias para trabajar con json y csv

nombre_archivo_json = pymsgbox.prompt("Ingrese el nombre del archivo a convertir(sin el .json)")
nombre_archivo_csv = pymsgbox.prompt("Ingrese el nombre del archivo csv(sin el .csv)")

if nombre_archivo_json == None or nombre_archivo_csv == None:
    pymsgbox.alert("Se cancelo la conversion")
    sys.exit()

try:
    # con with me aseguro de cerrar el archivo de forma automatica
    # abro el archivo llamado arch en modo lectura (r) y paso el objeto de archivo a la variable archivoJSON
    with open(f"{nombre_archivo_json}.json","r") as archivoJSON:
        datos = json.load(archivoJSON) #leo el archivoJSON y lo paso a la variable datos deserealiazado
    nombre_columnas = list(datos[0].keys()) # agarri el primer diccionario y le extraigo las etiquetas para los nombres de columnas, luego lo paso a una lista

    # creo y abro el archivo.csv en modo escritura(w) y lo paso el objeto de archivo a la variable archivoCSV
    with open(f"{nombre_archivo_csv}.csv","w",newline="") as archivoCSV:
        escritor = csv.DictWriter(archivoCSV,fieldnames=nombre_columnas) # con dicWriter para trabajar con diccionarios, le digo donde voy a escribir y el nombre de las columnas
        escritor.writeheader() #escribo las columnas
        escritor.writerows(datos) # escribo unicamente los datos sin las etiquetas del diccionario
except FileNotFoundError:
    pymsgbox.alert(f"error, el archivo {nombre_archivo_json} no fue encontrado")
