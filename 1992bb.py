def min_operations_to_merge(n, k, a):
    a.sort(reverse=True)
    operations = 0
    pieces = a.copy()

    while len(pieces) > 1:
        largest_piece = pieces.pop(0)
        
        if largest_piece > 1:
            pieces.append(1)
            pieces.append(largest_piece - 1)
            operations += 1
        else:
            next_largest = pieces.pop(0)
            pieces.append(next_largest + 1)
            operations += 1

        pieces.sort(reverse=True)
    
    return operations

# Read the number of test cases
t = int(input())
results = []

for _ in range(t):
    n, k = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    result = min_operations_to_merge(n, k, a)
    results.append(result)

for result in results:
    print(result)
