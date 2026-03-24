def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
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
        shift = int(input("Shift: ")) % 26
        if choice == "2":
            shift = -shift
        print(f"Result: {caesar(msg, shift)}")
    else:
        print("Invalid choice")