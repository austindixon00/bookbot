def main():
    
#    print("Please Enter Book Title")
#    x = input()
#    input_file_path = (f"books/{x}.txt")
#    file_path(input_file_path)
    

#finds book to open
#Path file can be changed to book_name
#def file_path(book_name):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words_in_book(file_contents)
    
def count_words_in_book(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    #print(word_count)


    for letter in words:
        print(words)


#dict 

main()

