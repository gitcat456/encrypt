def vigenere(text, key, mode):
    result = ""
    key = key.upper()
    key_len = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            if mode == -1:  # decrypt
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
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
        print(f"Result: {vigenere(msg, key, mode)}")
    else:
        print("Invalid choice")