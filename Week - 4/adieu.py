def main():
    import sys

    # List to store names
    names = []

    # Prompt user for names until EOF
    print("Enter names, one per line. Press Ctrl-D (Unix/Mac) or Ctrl-Z (Windows) to finish.")
    try:
        while True:
            name = input("Name: ").strip()
            if name:  # Ignore empty inputs
                names.append(name)
    except EOFError:
        pass

    # Generate the farewell message
    farewell = format_farewell(names)
    print(farewell)


def format_farewell(names):
    """
    Format the farewell message based on the number of names.
    """
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        # Join names with commas, except the last one with "and"
        return f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()
