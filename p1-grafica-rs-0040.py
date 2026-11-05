import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Hugo Fabian NC 0040
#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por fila
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# crea,os una lista de lista (conformado la tabla)
lista_redes_sociales=[fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# utilizar panda para organizar la tabla(dataframe o marco de datos)
df_redes_sociales=pd.DataFrame(lista_redes_sociales, columns=("nombre","cantidad","Es_FB", "año" ))
print(df_redes_sociales)
# creamos el archivo    CSV y lo guardamos en CSV
# df_redes_sociales.to_csv("redessociales.csv", index=False)
# crear grafica de lineas 
# donde x es nombre en el eje horizontal
# donde y es cantidad en el eje vertical
plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.title("grafica redes sociales 0040")
plt.xlabel("nombre de las redes")
plt.ylabel("cantidad de usuarios")
plt.show()
# creamos una grafica de puntos
plt.scatter(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.show()
# grafica de barras
plt.bar(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
# etiquetas y titulos
plt.title("redes sociales 0040")
plt.xlabel("las redes")
plt.ylabel("catidad de usuario")
# mostrar graficas
plt.show()
# ordenar grafica de barras de manera descendente
# de la mas grande a la pequeña
df_rs_ordenar=df_redes_sociales.sort_values("cantidad",ascending=False)
plt.bar(df_rs_ordenar["nombre"], df_rs_ordenar["cantidad"])
plt.show()
# coloreando la grafica
df_rs_ordenar=df_redes_sociales.sort_values("cantidad",ascending=False)
plt.bar(df_rs_ordenar["nombre"], df_rs_ordenar["cantidad"],
        color=["b","g", "c", "m", "y", "r"])
plt.show()

# grafica de pastel
# plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.pie(df_redes_sociales["cantidad"],
        labels=df_redes_sociales["nombre"])
plt.show()