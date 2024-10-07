# Read the number of test cases
t = int(input())

# Initialize the list to store results
results = []

# Process each test case
for _ in range(t):
    # Read the list of integers
    l = list(map(int, input().split()))
    
    # Initialize the result of XOR as 0
    xor_result = 0
    
    # Perform XOR on all elements
    for num in l:
        xor_result ^= num
    
    # Append the result (the distinct element) to the results list
    results.append(xor_result)

# Print all results
for result in results:
    print(result)
