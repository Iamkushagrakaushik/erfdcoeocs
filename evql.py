def compute_cumulative_sum(n):
    cumulative_sum = '0'
    current_num = '0'
    for i in range(len(n)):
        current_num = str(int(current_num) * 10 + int(n[i]))
        cumulative_sum = str(int(cumulative_sum) + int(current_num))
    return cumulative_sum

if __name__ == "__main__":
    n = int(input().strip())
    results = []
    for _ in range(n):
        m = int(input().strip())  # Read the integer input (not used in current logic)
        s = input().strip().lstrip('0')  # Read the string and remove leading zeros
        results.append(compute_cumulative_sum(s))
    
    for result in results:1
        print(result)
