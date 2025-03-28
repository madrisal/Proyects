## Ejercicios - Tamagotchi App en Python

En este ejercicio vamos a intentar replicar el popular juego de tamagotchi de los 90's con python, usando clases y métodos.

El programa le permitirá al usuario crear su propio tamagotchi, darle un nombre y cuidarlo hasta que el tamagotchi deje de existir. El usuario monitoreará el hambre, el aburrimiento, el cansancio y la suciedad de la criatura y deberá tomar acciones para que niguna de estas categorias sea muy alta, si alguna de estas categorias llegan a su limite entonces el tamagotchi morirá.

### Clase:

- Define la clase _**Tamagotchi**_ que tendrá lo siguiente:

1. Define el método _**\_\_init\_\_()**_ que tomé un parámetro, el nombre del tamagotchi (_**nombre**_) y que haga lo siguiente:
    - Inicializa el atributo _**nombre**_.
    - Inicializa los siguientes atributos en 0:
        - _**hambre**_, _**aburrimiento**_, _**cansancio**_ y _**suciedad**_.
    - Inicializa el atributo llamado _**comida**_ que llevará el conteo de cuanta comida tiene disponible la criatura, inicializa esta variable en 2.
    - Inicializa el atributo _**dormido**_ y dale el valor de _**False**_.
    - Inicializa el atributo _**vivo**_ y dale el valor de _**True**_.
    
========================================================================================================================
    
2. Define el método _**comer()**_ que no tome ningun parámetro y que haga lo siguiente:
    - Si el atributo _**comida**_ es mayor que 0:
        - Disminuya el atributo _**comida**_ en 1.
        - Disminuya el hambre de la criatura entre 1 y 4 (aleatoriamente).
        - Imprime un mensaje de que la criatura ha comido.
    - Si el atributo _**comida**_ es igual a 0:
        - Imprime un mensaje de que no hay comida disponible.
    - Si el hambre de la criatura llegase a ser menor que 0, regresa el valor de ese atributo a 0.

========================================================================================================================

3. Define el método _**jugar()**_ que no tome ningun parámetro y que haga lo siguiente:
    - Genere un número aleatorio entre 0 y 2 (num_aleatorio).
    - Imprima un mensaje que diga **_nombre_ quiere jugar... Elige un número entre 0 y 2.**
    - Pida al usuario por pantalla un número entre 0 y 2.
    - Si el input del usuario es igual a _**num_aleatorio**_:
        - Imprima: **Correcto!**.
        - Disminuya el aburrimiento de tamagotchi en 3.
    - Si el input no es igual a _**num_aleatorio**_:
        - Imprima: **Incorrecto!**.
        - Disminuya el aburrimiento de tamagotchi en 1.
    - Si el aburrimiento es menor a 0, regresa el valor de ese atributo a 0.
    
    
========================================================================================================================


4. Defina el método _**dormir()**_ que no tome ningun parámetro y que haga lo siguiente:
    - Cambia el parametro _**dormido**_ a _**True**_.
    - Disminuya el cansancio en 3.
    - Disminuya el aburrimiento en 2.
    - Imprima: **La criatura esta durmiendo...**
    - Si el aburrimiento es menor a 0, regresa el valor de ese atributo a 0.
    - Si el cansancio es menor a 0, regresa el valor de ese atributo a 0.
   
========================================================================================================================
   
   
5. Define el método _**despertar()**_ que no tome ningun parámetro y que haga lo siguiente:
    - Genere un número aleatorio entre 0 y 2.
    - Si el número es 0:
        - Imprima: **_nombre_ se ha despertado.**
        - Cambia el atributo _**dormido**_ a False.
        - Cambia el atributo aburrimiento a 0.
    - Si el número no es 0:
        - Imprima: **_nombre_ sigue durmiendo.**
        - Llama la función _**dormir()**_
        
========================================================================================================================


6. Define el método _**ducha()**_ que no tome ningun parámetro y que haga lo siguiente:

    - Cambia el atributo de suciedad a 0.
    - Imprime: **_nombre_ ha tomado un baño.**
   
========================================================================================================================
   
   
7. Define el método _**buscar_comida()**_ que no tome ningun parámetro y que haga lo siguiente:
    - Genere un número aleatorio entre 0 y 4 y guardala en la variable _**comida_encontrada**_.
    - Incrementa el atributo _**comida**_ usando _**comida_encontrada**_.
    - Incrementa la suciedad en 2.
    - Imprime: **_nombre_ ha encontrado _comida_encontrada_ comidas!**.
    
========================================================================================================================

8. Define el método _**mostrar_valores()**_ que no tome ningun parámetro y que haga lo siguiente:
    - Muestre todos los valores del tamagotchi:
        - nombre, hambre, aburrimiento, cansancio, comida, suciedad y si está dormido o no.
        
========================================================================================================================

9. Define el método _**dificultad()**_ que tome un parametro (_**nivel**_) que sea un entero entre 1 y 5:
    - Incremente el hambre aleatoriamente entre los numeros 0 y _**nivel**_.
    - Incremente la suciedad aleatoriamente entre los numeros 0 y _**nivel**_.
    - Si la criatura NO está durmiendo:
        - Incremente el aburrimiento aleatoriamente entre los numeros 0 y _**nivel**_.
        - Incremente el cansancio aleatoriamente entre los numeros 0 y _**nivel**_.

========================================================================================================================

10. Define el método _**morir()**_ que no tome ningun parámetro y que haga lo siguiente:
    - Si el hambre de la criatura es igual o mayor a 10:
        - Imprime: **_nombre_ murio de hambre.**
        - Cambia el atributo _**vivo**_ a _**False**_.
    - Si la suciedad de la criatura es igual o mayor a 10:
        - Imprime: **_nombre_ murio de una infección.**
        - Cambia el atributo _**vivo**_ a _**False**_.
    - Si el aburrimiento de la criatura es igual o mayor a 10:
        - Imprime: **_nombre_ está muy aburrido.**
        - Cambia el atributo _**aburrimiento**_ a 10.
        - Cambia el atributo _**dormido**_ a _**True**_.
    - Si el cansancio de la criatura es igual o mayor a 10:
        - Imprime: **_nombre_ está muy cansado y se acaba de dormir.**
        - Cambia el atributo _**cansancio**_ a 10.
        - Cambia el atributo _**dormido**_ a _**True**_.

### Funciones:

1. Define la función _**mostrar_menu()**_ que tome un parametro (_**tamagotchi**_) y que sea un objeto de la clase _**Tamagotchi**_ y que haga lo siguiente:
- Si el atributo dormido es _**False**_:
    - Imprimir:
    ```python
    """
    Presiona 1: Comer
    Presiona 2: Jugar
    Presiona 3: Dormir
    Presiona 4: Ducha
    Presiona 5: Buscar Comida
    """
    ```
- Tome por pantalla la opción del usuario. (_**opcion**_)
- Retorne el string _**opcion**_.

- Si el atributo dormido es _**True**_:
    - Imprima: **_nombre_ esta dormido... Presiona 6**
    - Tome por pantalla el input del usuario. (_**opcion**_)
    - Si _**opcion**_ es diferente de 6, cambia el valor de opción a 6.
    - Retorne el string _**opcion**_.
        
        
========================================================================================================================


2. Define la función _**llamar_accion()**_ que tome dos parametros, (_**tamagotchi**_) un objeto de clase _**Tamagotchi**_ y un string (_**opcion**_) que es el _**return**_ de la función _**mostrar_menu()**_ y que haga lo siguiente:
    - Si _**opcion**_ es 1, llama el método _**comer()**_ del objeto _**Tamagotchi**_.
    - Si _**opcion**_es 2, llama el método _**jugar()**_ del objeto _**Tamagotchi**_.
    - Si _**opcion**_ es 3, llama el método _**dormir()**_ del objeto _**Tamagotchi**_.
    - Si _**opcion**_ es 4, llama el método _**ducha()**_ del objeto _**Tamagotchi**_.
    - Si _**opcion**_ es 5, llama el método _**buscar_comida()**_ del objeto _**Tamagotchi**_
    - Si _**opcion**_ es 6, llama el método _**despertar()**_ del objeto _**Tamagotchi**_.
    - Si _**opcion**_ no es ninguna de las opciones validas, que imprima: **OPCION NO VALIDA.**


### Codigo Principal

1. Imprime un mensaje con el nombre del proyecto y otro que describa el proyecto.

========================================================================================================================

2. Pide al usuario el nivel de dificultad, este debe ser un número entre 1 y 5, guarda este número como entero en la variable _**nivel_dificultad**_.

========================================================================================================================

3. Pide al usuario el nombre del _**Tamagotchi**_ y guarda este string en la variable _**nombre_tamagotchi**_.

========================================================================================================================

4. Inicializa un objeto de clase _**Tamagotchi**_ usando el nombre _**nombre_tamagotchi**_ y asigna esta instancia a la variable _**mi_tamagotchi**_.

========================================================================================================================

5. Inicializa una variable _**ronda**_ e igualala a 1.

========================================================================================================================

6. Crea un bucle _**while**_ que se ejecute mientras la criatura este con vida:
    - Imprima: **Esta es la ronda numero _ronda_**.
    - Llame al método _**mostrar_valores()**_ de la criatura.
    - LLame la función _**mostrar_menu()**_.
    - LLama la función _**llamar_accion()**_.
    
    - Imprima: _**Ronda nº: ronda**_
    - Llama el método _**mostrar_valores()**_ de la criatura.
    - Haz que la celda se detenga por 3 segundos.
    
    - Llama el método _**dificultad()**_ de la criatura.
    - LLama el método _**morir()**_ de la criatura.
    - Incrementa en 1 la variable _**ronda**_.
    
========================================================================================================================

7. Si la criatura muere que imprima el mensaje: **_nombre_ ha fallecido :(**

========================================================================================================================

8. Imprima el número de rondas que se jugaron.