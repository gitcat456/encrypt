def create_table(key):
    chars = [c for c in (key.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ") if c != 'J' and c not in locals()['seen']] or (seen := set())
    return [chars[i:i+5] for i in range(0, 25, 5)]

def playfair(text, key, mode):
    table = create_table(key)
    pos = {table[r][c]: (r, c) for r in range(5) for c in range(5)}
    
    text = text.upper().replace('J', 'I')
    pairs = [text[i:i+2] if i+1 < len(text) else text[i] + 'X' for i in range(0, len(text), 2)]
    
    result = ""
    for a, b in pairs:
        r1, c1 = pos[a]
        r2, c2 = pos[b]
        if r1 == r2: result += table[r1][(c1 + mode) % 5] + table[r2][(c2 + mode) % 5]
        elif c1 == c2: result += table[(r1 + mode) % 5][c1] + table[(r2 + mode) % 5][c2]
        else: result += table[r1][c2] + table[r2][c1]
    return result

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
        print(f"Result: {playfair(msg, key, mode)}")
    else:
        print("Invalid choice")