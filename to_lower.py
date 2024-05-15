#https://chat.openai.com/share/32f97de9-8681-4ef7-8ce3-d670600faf15

def to_lowercase(input_string):
    """
    Convert a string to lowercase without using built-in string methods.
    
    Args:
    input_string (str): The string to convert.
    
    Returns:
    str: A new string where all uppercase letters have been converted to lowercase.
    """
    lowercased_string = []
    for char in input_string:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            # Convert uppercase letter to lowercase by adding 32 to its ASCII value
            lowercased_char = chr(ord(char) + 32)
        else:
            # Leave the character as it is
            lowercased_char = char
        lowercased_string.append(lowercased_char)
    
    # Join the list of characters into a string
    return ''.join(lowercased_string)



