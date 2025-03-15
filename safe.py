a = input("read or update")
if a == "update":
    filename = input("Enter the filename to save the input: ")

    try:
        with open(filename, "w") as file:
            while True:
                user_input = input("Enter text to save (type 'done' to finish): ")
                if user_input.lower() == 'done':
                    break
                file.write(user_input + "\n")
        print(f"Input saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
elif a == "read":
    try:
        b = input("enter filename")
        with open(b, "r") as file:
            content = file.read()
            print(f"Content of {b}:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file {b} was not found.")
else:
    print("Rerun and type either read or write")


