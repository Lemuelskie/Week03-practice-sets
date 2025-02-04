def analyze_file(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()  
            print("File content:")
            for line in lines:
                print(line, end='')  
            
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines) 
            char_count = sum(len(line) for line in lines)  

            print(f"\n\nThe file has {line_count} lines.")
            print(f"The file contains {word_count} words.")
            print(f"The file contains {char_count} characters.")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
