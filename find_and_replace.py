def combined_file_operations():
    """
    Performs combined file operations: find and replace, word frequency counting, and file merging.
    """

    try:
        with open("input.txt", "r") as f:
            file_content = f.read()
        new_content = file_content.replace("old", "new")  
        with open("output.txt", "w") as f:
            f.write(new_content)
        print("Find and replace complete.")
    except FileNotFoundError:
        print("Error: input.txt not found for find and replace.")


    try:
        word_counts = {}
        with open("input.txt", "r") as f:
            for line in f:
                for word in line.lower().split():
                    word = word.strip('.,!?"').rstrip() 
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1
        with open("word_frequencies.txt", "w") as f:
            for word, count in word_counts.items():
                f.write(f"{word}: {count}\n")
        print("Word frequency count complete.")
    except FileNotFoundError:
        print("Error: input.txt not found for word frequency counting.")


    try:
        with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f_merged:
            f_merged.write(f1.read())
            f_merged.write(f2.read())
        print("File merging complete.")
    except FileNotFoundError:
        print("Error: file1.txt or file2.txt not found for merging.")

combined_file_operations()