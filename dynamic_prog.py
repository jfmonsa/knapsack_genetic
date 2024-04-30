from typing import List
import time


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:

    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def measure_execution_time_knapsack(examples: List[dict]) -> List[float]:
    execution_times = []
    for example in examples:
        weights = example['weights']
        values = example['values']
        capacity = example['capacity']
        
        start_time = time.time()
        max_value = knapsack(weights, values, capacity)
        end_time = time.time()
        
        execution_times.append((end_time - start_time) * 1000)
    return [execution_times, max_value]



# Driver Code
if __name__ == "__main__":
    print("Algoritmo Dinámico")
    # examples
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 20000
    example = [{'weights': weights, 'values': values, 'capacity': capacity}]
    print("Ej 1:", measure_execution_time_knapsack(example))

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    example = [{'weights': weights, 'values': values, 'capacity': capacity}]
    print("Ej 2:", measure_execution_time_knapsack(example))

    weights = [1, 2, 4, 5, 7, 8]
    values = [2, 5, 6, 10, 13, 16]
    capacity = 8
    example = [{'weights': weights, 'values': values, 'capacity': capacity}]
    print("Ej 3:", measure_execution_time_knapsack(example))
