import time
import matplotlib.pyplot as plt
import numpy as np
import random
from typing import List


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
        population.append(individual)

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
        total = genetic_algorithm(weights, values, capacity, population_size, num_generations, mutation_rate)
        end_time = time.time()
        
        execution_times.append((end_time - start_time) * 1000)
    return [execution_times, total]

# Dynamic programming solution
def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    A function to solve the 0/1 knapsack problem using dynamic programming.

    Parameters:
    + weights (List[int]): List of weights of items.
    + values (List[int]): List of values of items.
    + capacity (int): Maximum capacity of the knapsack.

    Returns:
    + int: Maximum value that can be obtained.
    """

    # Number of items
    n = len(weights)
    # Creating DP matrix
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Iterate through each item
    for i in range(1, n + 1):
        # Iterate through each capacity
        for w in range(1, capacity + 1):
            # If the weight of the current item is less than or equal to the capacity
            if weights[i - 1] <= w:
                # We have two choices:
                # 1. Take the current item and add its value to the value of the knapsack with reduced capacity
                # 2. Do not take the current item
                # -> We chose the option that maximizes the total output
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )

            else:
                # If the weight of the current item is greater than the capacity,
                # we cannot take it, so we just use the value of the knapsack without the current item
                dp[i][w] = dp[i - 1][w]

    # The maximum value will be stored in the bottom-right cell of the table
    return dp[n][capacity]


def measure_execution_time_knapsack(examples: List[dict]) -> List[float]:
    execution_times = []
    for example in examples:
        weights = example['weights']
        values = example['values']
        capacity = example['capacity']
        
        start_time = time.time()
        total = knapsack(weights, values, capacity)
        end_time = time.time()
        
        execution_times.append((end_time - start_time) * 1000)
    return [execution_times, total]

capacity = 50
population_size = 20
num_generations = 10
mutation_rate = 0.05


def generate_sequence(start, end, step):
    sequence = []
    for i in range(start, end+1, step):
        avg = 50 // i
        remainder = 50 % i
        numbers = [avg + (1 if j < remainder else 0) for j in range(i)]
        counts = list(range(1, i+1))
        sequence.append([numbers, counts])
    return sequence

sequence = generate_sequence(100, 1000, 100)

examplesDina =  [
    {'weights': sequence[i][0], 'values': sequence[i][1], 'capacity': capacity} for i in range(len(sequence))
]
execution_timesDina = measure_execution_time_knapsack(examplesDina)
print(execution_timesDina)

examplesEvo =  [
    {'weights': sequence[i][0], 'values': sequence[i][1], 'capacity': capacity, 'population_size': population_size, 'num_generations': num_generations, 'mutation_rate': mutation_rate} for i in range(len(sequence))
]


# print(len(sequence[1][0]))

execution_timesEvolutivo = measure_execution_time(examplesEvo)
print(execution_timesEvolutivo)


x_values = [len(sequence[i][0]) for i in range(len(sequence))]

plt.plot(x_values, execution_timesDina[0], label='Dinámico O(n*w)')
plt.plot(x_values, execution_timesEvolutivo[0], label='Evolutivo O(P*G*O(n))')
plt.xlabel('Número de elementos para elegir')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Comparación de tiempos de ejecución')
plt.text(50, 30, f'Solución Dinámica: {int(execution_timesDina[1])}')
plt.text(50, 25, f'Solución Genético: {int(execution_timesEvolutivo[1])}')
plt.grid(True)
plt.legend()
plt.show()