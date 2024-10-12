import numpy as np
# Clase para implementar la evolución diferencial
class EvolucionDiferencial:
    def __init__(self, pop_size, bounds, dim, Cr):
        self.pop_size = pop_size  # Tamaño de la población
        self.bounds = bounds  # Intervalo para las variables
        self.dim = dim  # Número de dimensiones (x, y, z)
        self.Cr = Cr  # Tasa de recombinación
        self.population = self.initialize_population()  # Población inicial
    
    # Función objetivo
    def funcion(self, x, y, z):
        """funcion objetivo

        Args:
            x (int) : una dimension en x
            y (int): segunda dimension en y
            z (int): tercera dimension en z

        Returns:
            decimal: el resultado de evaluar la funcion objetivo con sus dimensiones
        """
        return x**2 + (y / z)
    
    # Generación de población inicial
    def initialize_population(self):
        """
        Recibe un intervalo[-N,+N] con el número de población n
        y sus dimensiones: x, y, z, ...,n
        """
        return np.random.uniform(self.bounds[0], self.bounds[1], (self.pop_size, self.dim))

    # Evaluar a los individuos de la población
    def evaluate_population(self):
        fitness_values = [] # Son los resultados de evaluar cada individuo con la función objetivo
        """
        Evalua en la Función Objetivo la población con sus dimensiones: 
        x, y, z
        """
        for individual in self.population:
            fitness = self.funcion(individual[0], individual[1], individual[2])
            fitness_values.append(fitness)
        return fitness_values

    # Algoritmo para realizar la evolución diferencial
    def evolve(self):
        for generation in range(1):  # En el rango de la población inicial (4)
            fitness_values = self.evaluate_population()
            print(f"Generación {generation}:")
            print("Población:", self.population) #Genera 4 diferentes "Individuos en [-10,10] "
            print("Valores de fitness:", fitness_values) #resultado después de evaluar F.O


if __name__ == '__main__':
    # Parámetros del problema
    pop_size = 4  # Tamaño de la población
    bounds = [-10, 10]  # Intervalo para los valores de x, y, z
    dim = 3  # Número de dimensiones (x, y, z)
    Cr = 0.5  # Tasa de recombinación
    
    # Crear la clase y ejecutar el proceso de evolución
    ed = EvolucionDiferencial(pop_size, bounds, dim, Cr)
    ed.evolve()