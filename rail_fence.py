def rail_fence(text, rails, mode):
    if mode == -1:  # decrypt
        cycle = 2 * (rails - 1)
        result = [''] * len(text)
        pos, step = 0, 1
        for r in range(rails):
            p = r
            while p < len(text):
                result[p] = text[pos]
                pos += 1
                p += cycle - 2 * r if r != 0 and r != rails - 1 else cycle
        return ''.join(result)
    else:  # encrypt
        fence = [[] for _ in range(rails)]
        row, step = 0, 1
        for char in text:
            fence[row].append(char)
            row += step
            if row == 0 or row == rails - 1:
                step = -step
        return ''.join(''.join(r) for r in fence)

while True:
    print("\n1. Encrypt\n2. Decrypt\n3. Exit")
    choice = input("Choice: ")
    if choice == "3":
        print("Goodbye!")
        break
    elif choice in ("1", "2"):
        msg = input("Message: ")
        rails = int(input("Number of rails: "))
        mode = 1 if choice == "1" else -1
        print(f"Result: {rail_fence(msg, rails, mode)}")
    else:
        print("Invalid choice")