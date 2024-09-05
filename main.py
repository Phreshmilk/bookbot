
def word_count(book):
    words = book.split()
    return len(words)

def each_char(book):
    words = list(book)
    charmap = {}
    for i in range(len(words)):
        words[i] = words[i].lower()
    for r in range(len(words)):
        if words[r] in charmap.keys():
            charmap[words[r]] += 1
        else:
            charmap.update({words[r] : 1})
    return charmap

def gen_report(my_dict):
    my_dict = {k : v for k,v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
    no_alpha = {}
    for i in my_dict.keys():
        if i.isalpha() == True:
            no_alpha.update({i : my_dict[i]})
        else:
            pass
    return (no_alpha)

if __name__ == "__main__":

    with open("/Users/tre/workspace/bookbot/books/frankenstein.txt", "r") as f:
        file_contents = f.read()

    # print(file_contents
    print("---Begin report of books.frankenstein.txt---\n")
    print(f"{word_count(file_contents)} words found in the document\n")   
    dunnies = gen_report(each_char(file_contents))
    for i in dunnies.keys():
          print(f" The  \"{str(i)} \" character was found {dunnies[i]} times ")
    print("\n --- End report ---")