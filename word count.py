# Function to count words in a given text
def count_words(text):
    # Remove leading/trailing whitespaces and split the text into words
    words = text.strip().split()
    # Return the number of words
    return len(words)

# Function to get input from the user
def get_input():
    print("Enter the text you want to count words for:")
    # Take input from the user
    text = input()
    if text=="":
        print("Input is empty Try to give a sentence")
    return text

# Function to display the word count
def display_word_count(word_count):
    
    print(f"The number of words in the given text is: {word_count}")

# Main function to run the program
def main():
    # Get the input text from the user
    text = get_input()
    # Count the words in the text
    word_count = count_words(text)
    # Display the word count
    display_word_count(word_count)

# Run the program
if __name__ == "__main__":
    main()
