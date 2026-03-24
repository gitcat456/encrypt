def row_transposition(text, key, mode):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    order = sorted(range(cols), key=lambda i: key[i])
    
    if mode == 1:  # encrypt
        text += 'X' * (rows * cols - len(text))
        grid = [text[i*cols:(i+1)*cols] for i in range(rows)]
        return ''.join(''.join(row[col] for row in grid) for col in order)
    else:  # decrypt
        cols_order = sorted(range(cols), key=lambda i: order[i])
        full = len(text) // rows
        extra = len(text) % rows
        grid = [[''] * cols for _ in range(rows)]
        pos = 0
        for c in range(cols):
            height = rows if c < extra else rows - 1 if mode == -1 else rows
            for r in range(height):
                grid[r][cols_order[c]] = text[pos]
                pos += 1
        return ''.join(''.join(row) for row in grid).rstrip('X')

while True:
    print("\n1. Encrypt\n2. Decrypt\n3. Exit")
    choice = input("Choice: ")
    if choice == "3":
        print("Goodbye!")
        break
    elif choice in ("1", "2"):
        msg = input("Message: ")
        key = input("Key: ")
        mode = 1 if choice == "1" else -1
        print(f"Result: {row_transposition(msg, key, mode)}")
    else:
        print("Invalid choice")