from typing import List


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
    n: int = len(weights)
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
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )

            else:
                # If the weight of the current item is greater than the capacity,
                # we cannot take it, so we just use the value of the knapsack without the current item
                dp[i][w] = dp[i - 1][w]

    # The maximum value will be stored in the bottom-right cell of the table
    return dp[n][capacity]


# Driver Code
if __name__ == "__main__":
    # expmaple 1
    weights = [60, 100, 120]
    values = [10, 20, 30]
    capacity = 5
    print("Maximum value 1:", knapsack(weights, values, capacity))

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print("Maximum value 2:", knapsack(weights, values, capacity))
