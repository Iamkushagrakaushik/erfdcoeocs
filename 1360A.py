def minimal_square_area(t, test_cases):
    results = []
    for a, b in test_cases:
        side1 = max(a + a, b)  # Placing rectangles side by side horizontally
        side2 = max(b + b, a)  # Placing rectangles side by side vertically
        min_side = min(side1, side2)
        results.append(min_side * min_side)  # Minimal square area
    return results

# Input reading and execution
t = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Solve and print results
results = minimal_square_area(t, test_cases)
for result in results:
    print(result)