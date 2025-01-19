def main():
    
#   print("Please Enter Book Title")
#    x = input()
#    input_file_path = (f"books/{x}.txt")
#    file_path(input_file_path)
    

#finds book to open
#ath file can be changed to book_name
#def file_path(book_name):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words_in_book(file_contents)
    extracting_letters(file_contents, word_count)
    
def count_words_in_book(text):
    word_count = len(text.split())
    return word_count

def extracting_letters(text, word_count):
    letter_count = {}
    for char in text:
        if char.isalpha() or char.isspace():
            low_char = char.lower()
            if low_char in letter_count:
                letter_count[low_char] += 1
            else:
                letter_count[low_char] = 1

    print("---Begin report of books/franekstein.txt ---")
    print(f"{word_count} words found in the document")
    sorted_dict = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    for char, count in sorted_dict.items():
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_dict[char]} times")
    print("--- End report ---")    


main()

