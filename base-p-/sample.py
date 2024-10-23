# Try subtracting from Unicode points
with open('based.txt', encoding='utf-8') as f:
    content = f.read()
    for char in content:
        code_point = ord(char)
        # Example: Subtract a value like 1000 from each code point and see the results
        adjusted_code = code_point - 1000
        if 32 <= adjusted_code <= 126:  # ASCII printable range
            print(chr(adjusted_code), end='')
