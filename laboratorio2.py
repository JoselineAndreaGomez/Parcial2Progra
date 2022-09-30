from estudiantes import estudiantes
from io import open
listado=[]
#Crear contactos
def nuevoestudiante(nombre,grado, promedio):
    listado.append(estudiantes(nombre,grado,promedio))

#Eliminar estudiantes
def eliminarestudiantes(nombre):
    posicion= None
    for i in range(len(listado)):
        if nombre==listado[i].vernombre():
            posicion=i
            break
    if posicion==None:
        return 'El estudiante no existe en el sistema-----------------------------\n'
    else:
        listado.pop(posicion)
        return 'Estudiante eliminado con éxito del sistema---------------------------- \n'

#crear reporte en html
def crearreporte():
    reporte=open("reporte.html","w")
    reporte.write('<!doctype html>\n')
    reporte.write("<html> \n")
    reporte.write("<head>\n")
    reporte.write("\t<title>SISTEMA ESTUDIANTIL 2022</title>\n")
    reporte.write("</head> \n")
    reporte.write("<body>")
    reporte.write("\t<center>\n")
    reporte.write("\t<h1>ESTUDIANTES REGISTRADOS EN EL SISTEMA ESTUDIANTIL</h1>\n")
    reporte.write('\t<table border="1">\n')
    reporte.write("\t\t<tr>\n")
    reporte.write("\t\t\t<td>Nombre del estudiante</td><td>Grado</td><td>Promedio</td>\n")
    for i in range (len(listado)):
        reporte.write("\t\t<tr>\n")
        reporte.write("\t\t\t<td>"+str(listado[i].vernombre())+"</td><td>"+str(listado[i].vergrado())+"</td><td>"+str(listado[i].verpromedio())+"</td>")
        reporte.write("\t\t</tr>\n")
    reporte.write("\t\t</tr>\n")
    reporte.write("</table>\n")
    reporte.write("\t</center>\n")
    reporte.write("</body>")
    reporte.write("</html> \n")
    reporte.close()
    print('Registro de estudiantes creado con éxito--------------------\n\n')

def main():
    opcion=0
    while opcion!=4:
     print("SISTEMA DE REGISTRO ESTUDIANTIL 2022 \n" 
     ,"1. Registrar nuevo estudiante \n",
     "2. Eliminar estudiante \n",
     "3. Ver registro de todos los estudiantes en HTML \n"
     "4. SALIR DEL SISTEMA ESTUDIANTIL \n\n")
     opcion=int(input('Ingrese el número de opción: '))
     
     if opcion==1:
        nombre=input('Ingrese el nombre del estudiante: ')
        grado=input('Ingrese el grado actual: ')
        promedio=int(input('Ingrese el promedio del estudiante: '))
        nuevoestudiante(nombre,grado,promedio)
        print('--------------------ESTUDIANTE REGISTRADO CON ÉXITO--------------------\n\n')
    
     elif opcion==2:
        nombre=input('Ingrese el nombre del estudiante que desea eliminar: ')
        eliminarestudiantes(nombre)
        print('--------------------ESTUDIANTE ELIMINADO CON ÉXITO--------------------\n\n')
     elif opcion==3:
        crearreporte()
     elif opcion==4:
        print('---------------------SALIENDO DEL PROGRAMA----------------------')

main()