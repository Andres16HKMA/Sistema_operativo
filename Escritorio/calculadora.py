import customtkinter as ctk

def abrir_calculadora():
    # Crear una nueva ventana para la calculadora
    calculadora = ctk.CTkToplevel()
    calculadora.geometry("300x400")
    calculadora.title("Calculadora")
    calculadora.attributes("-topmost", True)

    # Entrada para mostrar los números y operaciones
    global entrada  # Para que sea accesible desde la función calcular()
    entrada = ctk.CTkEntry(calculadora, width=200)
    entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Función para añadir texto a la entrada
    def agregar_a_entrada(simbolo):
        entrada.insert("end", simbolo)

    # Función de cálculo
    def calcular():
        try:
            resultado = eval(entrada.get())  # Realiza el cálculo
            entrada.delete(0, "end")  # Limpia la entrada
            entrada.insert("end", resultado)  # Muestra el resultado
        except Exception as e:
            entrada.delete(0, "end")
            entrada.insert("end", "Error")

    # Función para limpiar la entrada
    def limpiar():
        entrada.delete(0, "end")

    # Botones de la calculadora
    botones = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('-', 4, 3),
    ]

    for (texto, fila, columna) in botones:
        if texto == '=':
            boton = ctk.CTkButton(calculadora, text=texto,width=50, height=50 ,command=calcular)
        elif texto == 'C':  # Limpiar la entrada
            boton = ctk.CTkButton(calculadora, text=texto, width=50, height=50 ,command=limpiar)
        else:
            boton = ctk.CTkButton(calculadora, text=texto, width=50, height=50 ,command=lambda t=texto: agregar_a_entrada(t))
        
        boton.grid(row=fila, column=columna, padx=10, pady=10)

    calculadora.mainloop()