import copy
import concurrent.futures

import numpy as np


# Función objetivo
def funcion(x, y, z):
    """funcion objetivo

    Args:
        x (int) : una dimension en x
        y (int): segunda dimension en y
        z (int): tercera dimension en z

    Returns:
        decimal: el resultado de evaluar la funcion objetivo con sus dimensiones
    """
    return x ** 2 + (y / z)


# Clase para implementar la evolución diferencial
class EvolucionDiferencial:
    def __init__(self, pop_size, bounds, dim, Cr):
        self.pop_size = pop_size  # Tamaño de la población
        self.bounds = bounds  # Intervalo para las variables
        self.dim = dim  # Número de dimensiones (x, y, z)
        self.Cr = Cr  # Tasa de recombinación
        self.population = self.initialize_population()  # Población inicial

    # Generación de población inicial
    def initialize_population(self):
        """
        Recibe un intervalo[-N,+N] con el número de población n
        y sus dimensiones: x, y, z, ...,n
        """
        return np.random.randint(self.bounds[0], self.bounds[1], (self.pop_size, self.dim))

    # Algoritmo de maximización
    def maximization(self, num_generations):
        generations = [self.population]

        for i in range(num_generations):
            # Evaluamos la población actual en paralelo
            with concurrent.futures.ThreadPoolExecutor() as executor:
                fitness = list(executor.map(self.evaluate_vector, generations[i]))
            new_generation = copy.deepcopy(generations[i])
            for j in range(self.pop_size):
                mutation = self.mutate(generations[i], generations[i][j])
                # Evaluamos la mutación en paralelo
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    mutation_fitness = executor.submit(self.evaluate_vector, mutation).result()
                if mutation_fitness > fitness[j]:
                    new_generation[j] = mutation
                    fitness[j] = mutation_fitness
            generations.append(new_generation)

        return generations

    # Algoritmo de minimización
    def minimization(self, num_generations):
        generations = [self.population]

        for i in range(num_generations):
            # Evaluamos la población actual en paralelo
            with concurrent.futures.ThreadPoolExecutor() as executor:
                fitness = list(executor.map(self.evaluate_vector, generations[i]))
            new_generation = copy.deepcopy(generations[i])
            for j in range(self.pop_size):
                mutation = self.mutate(generations[i], generations[i][j])
                # Evaluamos la mutación en paralelo
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    mutation_fitness = executor.submit(self.evaluate_vector, mutation).result()
                if mutation_fitness < fitness[j]:
                    new_generation[j] = mutation
                    fitness[j] = mutation_fitness
            generations.append(new_generation)
        return generations

    def mutate(self, generation, objective):
        used_pos = []

        positions = np.where(generation == objective)[0]

        if len(positions) > 0:
            used_pos.append(positions[0])

        for i in range(3):
            while True:
                pos = np.random.randint(0, self.pop_size)
                if pos not in used_pos:
                    used_pos.append(pos)
                    break

        v1 = generation[used_pos[1]]
        v2 = generation[used_pos[2]]
        v3 = generation[used_pos[3]]

        return v1 + self.Cr * (v2 - v3)

    # Evaluar a los individuos de la población
    @staticmethod
    def evaluate_population(population):
        fitness_values = []  # Son los resultados de evaluar cada individuo con la función objetivo
        """
        Evalua en la Función Objetivo la población con sus dimensiones: 
        x, y, z
        """
        for individual in population:
            fitness = funcion(individual[0], individual[1], individual[2])
            fitness_values.append(fitness)
        return fitness_values

    # Evaluar un vector
    @staticmethod
    def evaluate_vector(vector):
        return funcion(vector[0], vector[1], vector[2])


if __name__ == '__main__':
    # Parámetros del problema
    pop_size = 4  # Tamaño de la población
    bounds = [-10, 10]  # Intervalo para los valores de x, y, z
    dim = 3  # Número de dimensiones (x, y, z)
    Cr = 0.5  # Tasa de recombinación

    # Crear la clase y ejecutar el proceso de evolución
    ed = EvolucionDiferencial(pop_size, bounds, dim, Cr)
    print(f"Solución: {ed.maximization(2)}")
