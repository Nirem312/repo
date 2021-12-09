import os
import re
import io

"""
DISCLAIMER
PARA UTILIZAR EL SCRIPT ASEGURARSE DE QUE EL PATH DONDE SE ENCUENTRAN LOS ARCHIVOS ES CORRECTO
"""

### IMPRIME LOS NOMBRES DE LOS ARCHIVOS EN UNA CARPETA ###

# USAR CON "python renombrar.py > names.txt" EN TERMINAL
path = 'C:/Users/Haha yes/Desktop/New folder (2)/'
files = os.listdir(path)
for f in files:
	print(f)


### REMUEVE TODO DE UN TXT DADO EXCEPTO NUMEROS Y RENOMBRA LOS ARCHIVOS (CUYO TIPO ES SOPORTADO) A LOS NOMBRES EN EL TXT###

#CARGA LAS LINEAS DEL TXT A UNA LISTA
with open("C:/Users/Haha yes/Desktop/New folder (3)/names.txt") as f:
    mylist = f.read().splitlines()
    #LE DA A LA VARIABLE J EL VALOR DE LA CANTIDAD DE OBJETOS (QUE ES EL LARGO DE LA LISTA PREVIAMENTE CREADA)
    j=len(mylist)
    #MIENTRAS HAYAN OBJETOS EN LA LISTA
    while j > 0:
        #SI EL TIPO DEL ARCHIVO ES SOPORTADO (EN ESTE CASO JPEG, PNG, JPG O MP4)
        if 'jpeg' in mylist[j-1]:
            #LA VARIABLE "PARSEO" CONTIENE EL NUEVO NOMBRE QUE ESTA COMPUESTO DE NUMEROS
            parseo = re.sub('[a-z._A-Z ]', '', mylist[j-1],) 
            #CAMBIA EL NOMBRE DEL ARCHIVO (EN ESTE CASO LOCALIZADO EN C:/Users/Haha yes/Desktop/New folder (2)/) POR EL STRING QUE CONTIENE LA VARIABLE "PARSEO"
            os.rename("C:/Users/Haha yes/Desktop/New folder (2)/"+mylist[j-1], "C:/Users/Haha yes/Desktop/New folder (2)/"+parseo+".jpeg")
        #REPITE EL PROCESO PARA EL RESTO DE TIPOS SOPORTADOS
        elif 'png' in mylist[j-1]:
            parseo = re.sub('[a-z._A-Z ]', '', mylist[j-1],)
            os.rename("C:/Users/Haha yes/Desktop/New folder (2)/"+mylist[j-1], "C:/Users/Haha yes/Desktop/New folder (2)/"+parseo+".png")
        elif 'jpg' in mylist[j-1]:
            parseo = re.sub('[a-z._A-Z ]', '', mylist[j-1],)
            os.rename("C:/Users/Haha yes/Desktop/New folder (2)/"+mylist[j-1], "C:/Users/Haha yes/Desktop/New folder (2)/"+parseo+".jpg")
        elif 'mp4' in mylist[j-1]:
            parseo = re.sub('[a-z._A-Z ]', '', mylist[j-1],)
            os.rename("C:/Users/Haha yes/Desktop/New folder (2)/"+mylist[j-1], "C:/Users/Haha yes/Desktop/New folder (2)/"+parseo+".mp4")
        #MUEVE LA LISTA AL SIGUIENTE OBJETO
        j=j-1
    #ELIMINA EL TXT UNA VEZ FINALIZADO EL SCRIPT (LOCALIZADO EN EL PATH)
    os.remove("C:/Users/Haha yes/Desktop/New folder (3)/names.txt")



