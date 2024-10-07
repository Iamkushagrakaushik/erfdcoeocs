def minimum_rotations(s):
    total_rotations = 0
    current_char = 'a'
    
    for char in s:
        clockwise_distance = (ord(char) - ord(current_char)) % 26
        counterclockwise_distance = (ord(current_char) - ord(char)) % 26
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        current_char = char
    
    return total_rotations

# Input
exhibit_name = input().strip()

# Output
print(minimum_rotations(exhibit_name))
