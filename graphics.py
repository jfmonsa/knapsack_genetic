#The graphics with complexity comparation of the algorithms
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


ventana = tk.Tk()
ventana.title("Comparación de algoritmos en el problema de la mochila")
ventana.resizable(True, True)
ventana.geometry("300x400")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)


# Data for plotting
x = np.arange(1, 11, 1)
print(x)

# complejidad de la mochila en dinámica: O(nW)
#complejidad de la mochila en un algoritmo evolutivo: O(nP)

def centrar_ventana(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")

centrar_ventana(ventana)

def graficar():
    n_values = np.arange(0, 20, 1)
    y_valuesDina = n_values * int(entry_dinaElement.get())

    y_values_evo = n_values * int(entry_evoTam.get()) * int(entry_evoGen.get())

    plt.plot(n_values, y_valuesDina, label='Dinámica O(n*k)')
    plt.plot(n_values, y_values_evo, label='Genético O(P*G*O(n))')
    plt.xlabel('Tamaño de n')
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.title('Complejidad')
    plt.grid(True)
    plt.text(50, 500, 'Dinámica', fontsize=12, color='red')
    plt.text(50, 2500, 'Genético', fontsize=12, color='blue')
    plt.legend()
    plt.show()




titulo = tk.Label(ventana, text="Problema de la mochila", font=("Bahnschrift", 15), padx=0, pady=2)

label_dinaElement = tk.Label(ventana, text="Número de items:", font=("Bahnschrift", 10), padx=0, pady=20)
entry_dinaElement = tk.Entry(ventana, font=("Bahnschrift", 10), width=10)

label_dinaCapacity = tk.Label(ventana, text="Capacidad de la mochila:", font=("Bahnschrift", 10), padx=0, pady=20)
entry_dinaCapacity = tk.Entry(ventana, font=("Bahnschrift", 10), width=10)

label_evoGen = tk.Label(ventana, text="Número de generaciones:", font=("Bahnschrift", 10), padx=0, pady=20)
entry_evoGen = tk.Entry(ventana, font=("Bahnschrift", 10), width=10)

label_evoTam = tk.Label(ventana, text="Tamaño de la población:", font=("Bahnschrift", 10), padx=0, pady=20)
entry_evoTam = tk.Entry(ventana, font=("Bahnschrift", 10), width=10)

btn_graphic = tk.Button(ventana, text="Graficar", width=30, height=2, padx=0, pady=20, command=graficar)

titulo.grid(column=0, row=0, pady=5, sticky="nsew")
label_dinaElement.grid(column=0, row=1, pady=5, sticky="nsew")
entry_dinaElement.grid(column=1, row=1, pady=5, sticky="nsew")
label_dinaCapacity.grid(column=0, row=2, pady=5, sticky="nsew")
entry_dinaCapacity.grid(column=1, row=2, pady=5, sticky="nsew")
label_evoGen.grid(column=0, row=3, pady=5, sticky="nsew")
entry_evoGen.grid(column=1, row=3, pady=5, sticky="nsew")
label_evoTam.grid(column=0, row=4, pady=5, sticky="nsew")
entry_evoTam.grid(column=1, row=4, pady=5, sticky="nsew")
btn_graphic.grid(column=0, row=5, columnspan=2, pady=5, sticky="nsew")


ventana.mainloop()


