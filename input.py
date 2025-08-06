def get_user_input():
    """Get plaintext input from the user with error handling."""
    try:
        plaintext = input("Enter the plaintext: ")
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")
        return plaintext
    except ValueError as ve:
        print(f"Input error: {ve}")
        return None



