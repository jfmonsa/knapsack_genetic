import random
from typing import List

# Función de aptitud
def fitness(individual: List[int], weights: List[int], values: List[int], capacity: int) -> int:
    total_value = 0
    total_weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_value += values[i]
            total_weight += weights[i]
            if total_weight > capacity:
                return 0
    return total_value

# Operador de selección
def selection(population: List[List[int]], weights: List[int], values: List[int], capacity: int) -> List[List[int]]:
    fitness_scores = [fitness(individual, weights, values, capacity) for individual in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    selected_population = random.choices(population, probabilities, k=len(population))
    return selected_population

# Operador de cruce
def crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Operador de mutación
def mutation(individual: List[int], mutation_rate: float) -> List[int]:
    mutated_individual = individual.copy()
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = 1 - mutated_individual[i]
    return mutated_individual

# Algoritmo genético
def genetic_algorithm(weights: List[int], values: List[int], capacity: int, population_size: int, num_generations: int, mutation_rate: float) -> int:
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(len(weights))]
        #ejemplo de individuo: 
        #donde la mochila es de espacio 11
        #[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        population.append(individual)
        #un conjunto de soluciones es una población
        #una solución es un individuo

    for _ in range(num_generations):
        population = selection(population, weights, values, capacity)
        new_population = []
        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            child = mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population

    best_individual = max(population, key=lambda individual: fitness(individual, weights, values, capacity))
    return fitness(best_individual, weights, values, capacity)


import time

def measure_execution_time(examples: List[dict]) -> List[float]:
    execution_times = []
    for example in examples:
        weights = example['weights']
        values = example['values']
        capacity = example['capacity']
        population_size = example['population_size']
        num_generations = example['num_generations']
        mutation_rate = example['mutation_rate']
        
        start_time = time.time()
        total_value = genetic_algorithm(weights, values, capacity, population_size, num_generations, mutation_rate)
        end_time = time.time()
        
        execution_times.append((end_time - start_time) * 1000)
    return [execution_times, total_value]



capacity = 50
population_size = 20
num_generations = 10
mutation_rate = 0.05




if __name__ == "__main__":
    print("Algoritmo genético")
    # ejemplos
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 20000
    example = [{'weights': weights, 'values': values, 'capacity': capacity, 'population_size': population_size, 'num_generations': num_generations, 'mutation_rate': mutation_rate}]
    print("Ej 1:", measure_execution_time(example))

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    example = [{'weights': weights, 'values': values, 'capacity': capacity, 'population_size': population_size, 'num_generations': num_generations, 'mutation_rate': mutation_rate}]
    print("Ej 2:", measure_execution_time(example))

    weights = [1, 2, 4, 5, 7, 8]
    values = [2, 5, 6, 10, 13, 16]
    capacity = 8
    example = [{'weights': weights, 'values': values, 'capacity': capacity, 'population_size': population_size, 'num_generations': num_generations, 'mutation_rate': mutation_rate}]
    print("Ej 3:", measure_execution_time(example))