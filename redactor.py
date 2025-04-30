


import re

def remove_words_from_file(filepath, selected_words):
    """
    Reads a text file, replaces specified words with asterisks, and saves the modified content
    back to the same file.  Handles punctuation and case sensitivity.

    Args:
        filepath (str): The path to the text file.
        selected_words (list): A list of words to remove (replace with asterisks).
    """
    try:
        with open(filepath, 'r+', encoding='utf-8') as file:
            text = file.read()  # Read the entire content of the file

            # Create a regular expression that matches any of the words in selected_words,
            # ignoring case and embedded in word boundaries.
            pattern = r'\b(?:' + '|'.join(re.escape(word) for word in selected_words) + r')\b'

            # Replace the matched words with asterisks
            modified_text = re.sub(pattern, '******', text, flags=re.IGNORECASE)

            # Go to the start of the file to overwrite it
            file.seek(0)
            file.write(modified_text)  # Write the modified text back to the file
            file.truncate()           # Remove any remaining characters if the new content is shorter

        print(f"Words removed and file updated: {filepath}")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to execute the word removal process.
    """
    filepath = 'my_text_file.txt'  # Replace with the actual path to your text file
    selected_words = ['cloud', 'copilot','copilot+','microsoft','Microsoft',
                      'windows', 'window','apple','mac','linux',
                      'the', 'a', 'is', 'are',''
                      ]  # Example list of words to remove

    # Create a dummy text file for demonstration if it doesn't exist
    try:
        with open(filepath, 'x', encoding='utf-8') as f:
            f.write("")
    except FileExistsError:
        pass # The file already exists, no need to create it.

    remove_words_from_file(filepath, selected_words)

if __name__ == "__main__":
    main()
