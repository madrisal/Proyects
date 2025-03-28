import random

def jugar():
    player = input(f'Elige una opción: piedra, papel o tijera ').lower()
    if player not in ['piedra', 'papel', 'tijera']:
        print('Elige una opción válida.')
        return
    
    compu = random.choice(['piedra', 'papel', 'tijera'])
    
    print(f"Tú elegiste: {player}")
    print(f"La computadora eligió: {compu}")
    
    if player == compu:
        print(f'¡Empate!')
    elif ((player == 'piedra' and compu == 'tijera')
        or (player == 'papel' and compu == 'piedra')
        or (player == 'tijera' and compu == 'papel')):
        print(f'¡Ganaste!')
    else:
        print (f'¡Perdiste!')

while True:
    jugar()
    continuar = input('¿Quieres jugar otra vez? (si/no): ').lower()
    if continuar != 'si':
        print('¡Hasta la próxima!')
        break
