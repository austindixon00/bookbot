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
    count_words_in_book(file_contents)
    
def count_words_in_book(text):
    word_count = len(text.split())
    print(word_count)
    extracting_letters(text)

def extracting_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha() or char.isspace():
            low_char = char.lower()
            if low_char in letter_count:
                letter_count[low_char] += 1
            else:
                letter_count[low_char] = 1
    print(letter_count)



#dict 

main()

