import random
from random import randint

class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.aburrimiento = 0
        self.cansancio = 0
        self.suciedad= 0
        self.comida = 2
        self.dormido= False
        self.vivo= True
    
    def comer(self):
        if self.comida > 0:
            self.comida = self.comida -1
            self.hambre = self.hambre - randint(1,4)
            print(f'{self.nombre} ha comido! 🥣')
        else:
            print(f'No queda comida')
        self.hambre = 0 if self.hambre < 0 else self.hambre
    
    def jugar(self):
        while True:
            print(f'{self.nombre} quiere jugar 🎲 ... Elige una opción: piedra, papel o tijera:')
            compu = random.choice(['piedra', 'papel', 'tijera'])
            player = input().lower()
            if player not in ['piedra', 'papel', 'tijera']:
                print('Elige una opción válida.')
                continue
            print(f"Tú elegiste: {player}")
            print(f"{self.nombre} eligió: {compu}")
            if player == compu:
                print(f'¡Empate! 😑')
                self.aburrimiento = self.aburrimiento -1
            elif ((player == 'piedra' and compu == 'tijera')
                or (player == 'papel' and compu == 'piedra')
                or (player == 'tijera' and compu == 'papel')):
                print(f'¡Ganaste! 🏆')
                self.aburrimiento = self.aburrimiento -1
            else:
                print (f'¡Ganó {self.nombre}! 😄')
                self.aburrimiento = self.aburrimiento -3

            self.aburrimiento = 0 if self.aburrimiento < 0 else self.aburrimiento
            again = input('¿Quieres jugar otra vez? (si/no): ').lower()
            if again != 'si':
                print ('¡Hasta la próxima! 👋 ')
                break

    def dormir(self):
        self.dormido = True
        self.cansancio = self.cansancio -3
        self.aburrimiento = self.aburrimiento -2
        print (f'{self.nombre} está durmiendo...💤')
        self.aburrimiento = 0 if self.aburrimiento < 0 else self.aburrimiento
        self.cansancio = 0 if self.cansancio < 0 else self.cansancio

    def despertar(self): # Cambio la variable para que dependa del cansancio
        if self.cansancio < 5:
            print (f'{self.nombre} se ha despertado.')
            self.dormido = False
            self.aburrimiento= 0
        else:
            print (f'{self.nombre} está muy cansado y sigue durmiendo.')
            self.dormir()
            
    def ducha(self):
        self.suciedad = 0
        print(f'{self.nombre} ha tomado un baño 🛀')

    def buscar_comida(self):
        comida_encontrada = randint(0,4)
        self.comida = self.comida + comida_encontrada
        self.suciedad = self.suciedad +2
        print(f'{self.nombre} ha encontrado {comida_encontrada} comidas!')
    
    def mostrar_valores(self):
        print(f"Nombre: {self.nombre}")
        print(f"Hambre: {self.hambre}")
        print(f"Aburrimiento: {self.aburrimiento}")
        print(f"Cansancio: {self.cansancio}")
        print(f"Comida: {self.comida}")
        print(f"Suciedad: {self.suciedad}")
        print(f"Dormido: {self.dormido}")
        
    def dificultad(self, nivel):
        self.hambre = self.hambre + randint(0, nivel)
        self.suciedad = self.suciedad + randint(0, nivel)
        if self.dormido == False:
            self.aburrimiento = self.aburrimiento + randint(0, nivel)
            self.cansancio = self.cansancio + randint(0, nivel)
            
    def morir(self):
        if self.hambre >= 10:
            print(f'{self.nombre} ha muerto de hambre :(')
            self.vivo = False
        elif self.suciedad >= 10:
            print(f'{self.nombre} murió de una infección :(')
            self.vivo = False
        elif self.aburrimiento >=10:
            print(f'{self.nombre} está muy aburrido... se ha dormido.')
            self.aburrimiento = 10
            self.dormido = True
        elif self.cansancio >= 10:
            print(f'{self.nombre} está muy cansado y se acaba de dormir')
            self.cansancio = 10
            self.dormido= True
            
            
# Funciones

def mostrar_menu(tamagotchi):
    if not tamagotchi.dormido:
        print("""
              =====================
                      MENÚ
              =====================
              1: Comer
              2: Jugar
              3: Dormir
              4: Ducha
              5: Buscar comida
              0: Salir
        """)
        opcion = input("Selecciona una acción\n")
        return opcion
    else:
        print("\n********************")
        print(f"{tamagotchi.nombre} está dormido...")
        print("********************")
        print("Presiona 6 para despertarlo")
        opcion = input("Selecciona una acción: ")
        opcion = "6" if opcion != "6" else opcion
        return opcion
    
def llamar_accion(tamagotchi, opcion):
    if opcion == '1':
        tamagotchi.comer()
    elif opcion == '2':
        tamagotchi.jugar()
    elif opcion== '3':
        tamagotchi.dormir()
    elif opcion == '4':
        tamagotchi.ducha()
    elif opcion =='5':
        tamagotchi.buscar_comida()
    elif opcion =='6':
        tamagotchi.despertar()
    else:
        print(f'Opción no válida')