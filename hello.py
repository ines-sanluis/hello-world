def greet(name="World"):
    """
    A simple greeting function that returns a hello message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def main():
    # Example usage
    print(greet())  # Prints: Hello, World!
    print(greet("GitHub"))  # Prints: Hello, GitHub!

if __name__ == "__main__":
    main()