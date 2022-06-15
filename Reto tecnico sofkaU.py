# JUAN
"""
Created on Wed 07 17:33:01 2022

@author: JUAN
"""
totalAcumulado = 0

print(                                                                                        )
print(                                                                                        )
print(                                                                                        )
print("                                                           HAZTE MILLONARIO SI CONOCES DE NUESTRO PAIS                       ")
print("")
print("Dinamica del juego")
print("Este reto pretende medir tus conocimientos en 5 areas del saber en las cuales iras escalando de nivel; cada que respondas una pregunta buena obtendras una recompensa de $ 100.000  pesos colombianos.")
def menu():
    print()
    print("                                                                        Comencemos")
    print("escriba SI para comenzar el juego")
    menu = input("¿Quieres jugar?: ")
    return menu
import random

#serie de preguntas
class Preguntas:
    
    categoriaciudades = ["¿cual es la capital del choco? ",
                          "¿Cual es la cuidad mas grande de Colombia? ",
                          "¿En cual de las siguientes ciudades se celebra el carnaval de negros y blancos?",
                          "¿Cual fue la primera ciudad de Colombia? ",
                          "¿cual es la ciudad considerada la sucursal del cielo?",]
    
    categoriaFutbol = ["¿cual fue el primer equipo campeon de colombia?",
                       "cuál es el equipo que actualmente tiene mas estrellas?",
                        "¿cual es el equipo mas grande de colombia?",
                        "Cual fue el primer equipo colombiano en ganar la copa libertadores?",
                        "Nombre de la liga actual de futbol? "]

    categoriaPresidentes = ["¿cuantos presidentes ha tenido Colombia en toda su historia?",
                            "Cual fue el primer presidente de Colombia",
                            "¿cual fue el presidente en el año 1980?",
                            "¿Cual ha sido el presindete mas joven de Colombia?",
                            "¿Cual era el presidente cuando derrotaron a Pablo Escobar?"]
    
    categoriaHistoria = ["¿Cual fue el primer nombre de Colombia?",
                         "¿ En que año nacio Gabriel Garcia Marquez?",
                         "¿ En que año se construyo el metro de Medellin ?",
                         "¿cual de los siguientes paises pertecia a la Gran colombia",
                         "¿En que año colombia gano la primera medalla de oro en unos olimpicos?” "]
    
    categoriaPersonajes = ["¿Quien aparece en el billete de 100 mil?",
                            "¿Que vacuna invento Manuel Elkin Patarroyo",
                            "¿Cual fue el primer atleta colombiano en ganar la primera medalla olimpica?",
                            "¿Quien escribio la novela colombiana Delirio?",
                            "¿Quien fundo Cartagena de indias? "]
    
    
    

class Respuestas:
    
    respuesciudades = ["C","D","D","B","A"]
    
    respuestaFutbol = ["A","A","D","C","A"]
    
    respuestaPresidentes = ["B","A","A","C","A"]
    
    respuestaHistoria = ["D","C","C","D","A"]
    
    respuestaPersonajes = ["A","C","B","C","D"]
    
    
class Opciones:
    
    opcionesciudades = ["A. Arauca  B. leticia  C. Quibdo  D. Cucuta  ",
                         "A. Medellin  B. Bucaramanga C.  Pasto  D.	Bogota",
                         "A. Armenia B.	Pereira C.	Caqueta D.	Pasto ",
                         "A. Bogota B. Santa Maria C. Cartegena D. Boyaca",
                         "A. Cali B. Tumaco C. Popayan D.	Medellin "]
    
    opcionesFutbol = ["A. Santa fe B. Leones C.	Medellin D.	Nacional",
                     "A.	Millonarios   B.	Nacional C.	Cali	D. America ",
                     "A.	Bucaramanga B.	Millonario  C.	Santafe  D.	Nacional",
                     "A.	Junior  B.	Once caldas  C.	Nacional  D. America ",
                     "A.	Betplay B. Aguila C. Postobon D. suramericana"]
    
    opcionesPresidentes = ["A.	55 B.	60 C.	130 D.72",
                           "A.	Simon Bolivar B. Santander C. Cristobal Colon  D. Joaquin Mosquera",
                            "A.	Julio Cesar Turbay B. Carlos lleras  C.	Belizario Betancur D. Andres Pastrana",
                            "A.	Ivan Duque B.	Cesar Gaviria C.	Austorgio Salgar D. Galan",
                            "A.	Cesar Gaviria B.	Alvaro Uribe C.	Jorge Luis Ochoa D.	Andres Pastrana "]
    
    opcionesHistoria = ["A.	Boyaca B.	Colon C.	Gran colombia  D. Nueva granada ",
                        "A.	1950 B.	1930 C.	1927 D.	1962 ",
                        "A.	1960 B.1999	 C.	1995 D.	1930",
                        "A.	Venezuela B. Panama	 C.	Ecuador D.	Todas las anteriores",
                        "A.	2000  B. 1996 C.	1950 D.	2004"]
    
    opcionesPersonajes = ["A.	Carlos LLeras B. Gabriel Garcia Marquez C.	El pibe Valderrama D.	Cristobal Colon",
                          "A.	Contra el COVI19  B.	contra la rubeola  C.	contra la malaria  D.	Contra la tos ",
                          "A.	Julio Rocha B. Helmut Bellingrodt C. Mariana pajon D.	Azael Henao ",
                          "A.	Debora Arango B.	Camila Ochoa C.	Laura Restrepo D.	Guillermina Ospina",
                          "A.	Rodrigo de bastidas B. Alonso de Ojeda C.	Venedito Bolivar D. Pedro de heredia"]


while menu()=="SI":

    #Ciudades
    if(totalAcumulado == 0):
       print("PRIMERA PREGUNTA CATEGORIA CIUDADES")
       iten = random.randint(0,4)
       print("")
       print(Preguntas.categoriaciudades[iten])
       print(Opciones.opcionesciudades[iten])
       print("")
    
       respuesta = input("INGRESE SU RESPUESTA EN MAYUSCULA: ")
       if(respuesta == Respuestas.respuesciudades[iten]):
           print("RESPUESTA CORRETACA: ", Respuestas.respuesciudades[iten])
           totalAcumulado = 100000
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("RESPUESTA INCORRETACA:",Respuestas.respuesciudades[iten])
           totalAcumulado = 0
           break
       
    #Futbol
    if(totalAcumulado == 100000):
       print("SEGUNDA PREGUNTA CATGORIA futbol")
       iten = random.randint(0, 4)
       print("")
       print(Preguntas.categoriaFutbol[iten])
       print(Opciones.opcionesFutbol[iten])
       print("")
    
       respuesta = input("INGRESE SU RESPUESTA EN MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaFutbol[iten]):
           print("RESPUESTA CORRETACA: ",  Respuestas.respuestaFutbol[iten])
           totalAcumulado = totalAcumulado + 100000
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("RESPUESTA INCORRETACA:", Respuestas.respuestaFutbol[iten])
           totalAcumulado = 0
           break
       
    #Presidentes
    if(totalAcumulado == 200000):
       print("TERCERA PREGUNTA CATGORIA Presidentes")
       iten = random.randint(0, 4)
       print("")
       print(Preguntas.categoriaPresidentes[iten])
       print(Opciones.opcionesPresidentes[iten])
       print("")
    
       respuesta = input("INGRESE SU RESPUESTA EN MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaPresidentes[iten]):
           print("RESPUESTA CORRETACA: ", Respuestas.respuestaPresidentes[iten])
           totalAcumulado = totalAcumulado + 100000
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("RESPUESTA INCORRETACA:", Respuestas.respuestaPresidentes[iten])
           totalAcumulado = 0
           break
       
    #Historia
    if(totalAcumulado == 300000):
       print("CUARTA PREGUNTA CATGORIA Historia")
       iten = random.randint(0, 4)
       print("")
       print(Preguntas.categoriaHistoria[iten])
       print(Opciones.opcionesHistoria[iten])
       print("")
    
       respuesta = input("INGRESE SU RESPUESTA EN MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaHistoria[iten]):
           print("RESPUESTA CORRETACA: ", Respuestas.respuestaHistoria[iten])
           totalAcumulado = totalAcumulado + 100000
           print("Total Acumulado: ", totalAcumulado)
       else:
           print("RESPUESTA INCORRETACA:", Respuestas.respuestaHistoria[iten])
           totalAcumulado = 0
           break
       
    #Personajes
    if(totalAcumulado == 400000):
       print("SEGUNDA PREGUNTA CATGORIA Personajes")
       iten = random.randint(0, 4)
       print("")
       print(Preguntas.categoriaPersonajes[iten])
       print(Opciones.opcionesPersonajes[iten])
       print("")
    
       respuesta = input("INGRESE SU RESPUESTA EN MAYUSCULA: ")
       if(respuesta ==  Respuestas.respuestaPersonajes[iten]):
           print("RESPUESTA CORRETACA: ", Respuestas.respuestaPersonajes[iten])
           totalAcumulado = totalAcumulado + 100000
           print("Total Acumulado: ", totalAcumulado)
           break
       else:
           print("RESPUESTA INCORRETACA:", Respuestas.respuestaPersonajes[iten])
           totalAcumulado = 0
           break 
    
       
        
    if(menu()=="0"):
        totalAcumulado = totalAcumulado
        break
    menu()
    
    
print("Su Acumulado fue de: ",totalAcumulado)

















