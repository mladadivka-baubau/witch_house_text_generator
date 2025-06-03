import random

def witch_house_transform(text, transformation_chance=0.25):
    """Transform text using witch house character replacements with random application"""
    # Space replacement is always applied
    space_replacement = {'⑊'}
    
    # Other replacements are applied randomly
    random_replacements = {
        'A': 'ᐃ',
        'a': '▲',
        'E': '≣',
        'e': '∃',
        'O': '▒',
        'o': '⋄',
        'S': '$',
        's': '$',
        'T': '†',
        't': '†',
        'V': '▼',
        'v': '▼',
        'U': '∪',
        'u': '∪',
        'W': '∨∨',
        'w': '⋈',
        'X': '✖',
        'x': '✄',
        'y': 'ʎ',
        '0': '⊗',
        '3': '3',
        'eo': '∄∎',
        'oo': '∞',
        'ee': '⺬⺬',
    }
    
    # Always replace spaces
    result = text.replace(' ', '⋮')
    
    # Apply other transformations randomly
    result_chars = list(result)
    for i, char in enumerate(result_chars):
        if char in random_replacements and random.random() < transformation_chance:
            result_chars[i] = random_replacements[char]
    
    return ''.join(result_chars)

def main():
    print("=== Witch House Text Transformer ===")
    print("Enter text to transform using witch house characters")
    print("(Spaces always transform, other characters transform randomly)\n")
    
    while True:
        # Get input from user
        user_input = input("Enter your text: ")
        
        # Optional: let user adjust transformation frequency
        freq_input = input("Transformation frequency (0.1-1.0, default 0.25): ").strip()
        try:
            frequency = float(freq_input) if freq_input else 0.25
            frequency = max(0.1, min(1.0, frequency))  # Clamp between 0.1 and 1.0
        except ValueError:
            frequency = 0.25
        
        # Transform the text
        transformed = witch_house_transform(user_input, frequency)
        
        # Display result
        print(f"\nTransformed: {transformed}\n")
        
        # Ask if user wants to continue
        while True:
            continue_choice = input("Continue? Y/N: ").strip().upper()
            if continue_choice in ['Y', 'N']:
                break
            print("Please enter Y or N")
        
        if continue_choice == 'N':
            print("Goodbye!")
            break
        else:
            print()  # Add blank line for readability

if __name__ == "__main__":
    main()
