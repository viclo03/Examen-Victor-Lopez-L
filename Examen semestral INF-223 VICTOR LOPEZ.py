# Improtar librerias necesarias para la ejecución del programa como:
import networkx as nx # Se importa para trabajar con grafos 
import matplotlib.pyplot as plt # Importado para trabajar con graficos 2D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Incrusta figuras dentro de Tkinter
from tkinter import * # IMporta bibliotecas de Tkinter dentro de phyton
from tkinter import ttk #Importa modulo de tkinter.ttk (acceso a widgets)

# Funcion def para capturar nodo inicio (inicio) y nodo destino (final)
def calcular_distancia():
    inicio = combo_inicio.get() #combobox para seleccionar inicio
    destino = combo_destino.get() #combobox para seleccionar destino 

    if nx.has_path(Grafo, inicio, destino): # Busca si hay una ruta (Si hay una ruta procede a calcular distancia)
        distancia_corta = nx.shortest_path_length(Grafo, inicio, destino, weight='weight') # Calcula distancia entre nodos
        # Imprime nombres de los nodos y la distanta entre ellos
        leyenda = "La distancia más corta entre {} y {} es de {} kilómetros".format(inicio, destino, distancia_corta) 
        print(leyenda)
        # De no existir un camino imprime que no existe un camino
    else:
        print("No existe un camino entre {} y {}".format(inicio, destino))

# Da un titulo a la ventana en Tkinter
root = Tk()
root.title("DIAGRAMA DE CAMINO RÁPIDO   POR: VICTOR LOPEZ") # Titulo a mostrar

# Creacion de grafos y nodos
Grafo = nx.Graph() # Crea el grafo
# Nodos Creados
Grafo.add_node("Penonomé") #Nodo 1
Grafo.add_node("Cañaveral") #NOdo2
Grafo.add_node("Coclé") #Nodo 3
Grafo.add_node("Chigurí Arriba") #Nodo 4
# Aristas de los grafos 
Grafo.add_edge("Penonomé", "Cañaveral", weight=13.5)
Grafo.add_edge("Cañaveral", "Chigurí Arriba", weight=41.6)
Grafo.add_edge("Chigurí Arriba", "Coclé", weight=45.2)
Grafo.add_edge("Penonomé", "Chigurí Arriba", weight=31.2)
Grafo.add_edge("Penonomé", "Coclé", weight=11.4)

# Crear el diseño del grafo
pos = nx.spring_layout(Grafo) # Calcula posicion del grafo
nx.draw(Grafo, pos, node_size=1300, node_color='yellow', font_size=8, font_weight='bold', with_labels=True) # Dibuja el grafo de los posiciones calculadas de "pos"
weight = nx.get_edge_attributes(Grafo, "weight") # Distancias entre los nodos 
nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=weight) # Muestra los km en las aristas

# Crear ComboBox para los nodos de inicio y destino
nodos = list(Grafo.nodes()) # Se obtienen todos los nodos
combo_inicio = ttk.Combobox(root, values=nodos) # Se crea un combobox con los valores seleccionados
combo_inicio.set(nodos[0]) # Guarda el nodo seleccionado
combo_inicio.grid(row=0, column=1, padx=10, pady=10) # Establece el espacio entre el borde de la caja y los elementos dentro de ella.
# Se repide lo comentado anteriormente
combo_destino = ttk.Combobox(root, values=nodos)
combo_destino.set(nodos[-1])
combo_destino.grid(row=0, column=2, padx=10, pady=10)

# Botón para calcular distancias
boton_calcular = Button(root, text="Calcular Distancias", command=calcular_distancia) # Texto del botón
boton_calcular.grid(row=1, column=1, columnspan=2, pady=10) # POsicion del botón

# Integra el gráfico de Matplotlib en la interfaz gráfica de Tkinter
canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
canvas.draw() # Obtiene la figura creada con  Matplotlib
canvas.get_tk_widget().grid(row=2, column=1, columnspan=2, pady=10) # Posicion en la que va aparecer el grafo 

# Configuracion ventana principal
root.mainloop() # Mantiene la ventana en espera de acciónes y en funcionamiento 
