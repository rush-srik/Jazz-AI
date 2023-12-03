# Given a string x, check if it is an integer
def is_integer(x):
    try: 
        int(x)
    except ValueError:
        return False
    return True

# Outputs a pattern throughout a scale's degrees given a pattern input starting from the first scale degree
def shift_pattern(pattern):
    pattern = list(pattern)
    degree_idx = [i for i, j in enumerate(pattern) if is_integer(j)]
    degrees = [i for i in pattern if is_integer(i)]
    output = f'{"".join(map(str, pattern))}\n'
    for i in range(1, 7):
        pattern_copy = pattern
        new_degrees = [int(j)+i for j in degrees]
        for j, k in enumerate(degree_idx):
            pattern_copy.pop(k)
            pattern_copy.insert(k, new_degrees[j])
        output += f'{"".join(map(str, pattern_copy))}\n'
    return output

while True:
    print(shift_pattern(input('>')))
