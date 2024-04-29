from typing import List
import time

# Time complexity of this DP algo: O(n*W), where n is the number of items,
# and W is the knapsack capicity
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
        max_value = knapsack(weights, values, capacity)
        end_time = time.time()
        
        execution_times.append((end_time - start_time) * 1000)
    return [execution_times, max_value]






# Driver Code
if __name__ == "__main__":
    # examples
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
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
