from funciones import Tamagotchi, mostrar_menu, llamar_accion
from time import sleep

# Código principal

print('=========================')
print("Tamagotchi App en Python")
print('=========================')
print("""En este ejercicio vamos a intentar replicar el popular juego de tamagotchi de los 90's con python, usando clases y métodos.""")

nivel_dificultad = int(input('Elige un nivel de dificultad (1 - 5): '))
nombre_tamagotchi = input('Ponle nombre al Tamagotchi: ')
mi_tamagotchi = Tamagotchi(nombre_tamagotchi)
ronda = 1 
while mi_tamagotchi.vivo:
      print("-"*100)
      print(f'Esta es la ronda número {ronda}')
      mi_tamagotchi.mostrar_valores()
      opcion = mostrar_menu(mi_tamagotchi)
      if opcion == '0':
            print('¡Bye! 👋')
            break           
      llamar_accion(mi_tamagotchi, opcion)
      mi_tamagotchi.mostrar_valores()
      sleep(3)
      mi_tamagotchi.dificultad(nivel_dificultad)
      mi_tamagotchi.morir()
      
      ronda +=1
if not mi_tamagotchi.vivo:
      print(f'Se jugaron {ronda - 1} rondas.')
      # Elimino la frase {mi_tamagotchi.nombre} ha fallecido :(' porque se duplica por el método morir.
      input("Presiona Enter para salir...")  # Para que no se cierre la ventana