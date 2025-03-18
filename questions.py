import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Inicializo la variable puntaje en 0 para luego sumar y restar
puntos = float(0)
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))  
        # Se corrobora que sea un numero entero
        if(not user_answer.isdigit() ): 
            # Si no es un entero imprime lo pedido y termina con el programa
            print("Respuesta no valida")
            exit(1)
        # Si se ingresa un numero entero a este se le resta uno para asi poder comparar con el rango de respuestas 
        user_answer = int(user_answer)-1
        # Se corrobora que el numero entero ingresado este en el rango de  0=<ans<=3
        if user_answer < 0 or user_answer > 3:
            print("Respuesta no valida")
            exit(1)
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index[question_index]:
            print("¡Correcto!")
            # Se le suma uno a la variable puntaje 
            puntos = puntos + 1
            break
        else:
            # Se le resta cero punto cinco a la variable Puntaje ya que es una respuesta incorrecta
            puntos = puntos - 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    print()
# Se imprimen la cantidad de puntos totales que obtubo al final del quizz
print("Su puntaje final es ",puntos)