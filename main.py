def main():
        content = get_contents();
        print_report(content)

def get_contents():
    with open('books/frankenstein.txt') as f:
        return f.read()

def get_wordcount(content):
     return len(content.split())

def letter_count(content):
    letters = {}
    for letter in content.lower():
        if letter in letters:
             letters[letter] += 1
        else:
             letters[letter] = 0
    return letters


def sort_on(dict):
     return dict["num"]

def print_report(content):
     print("--- Begin report of books/frankenstein.txt ---")
     print(f"{get_wordcount(content)} words found in the document\n\n")
     letter_count_dict = letter_count(content)
     sorter_letter_count_dict = []
     for letter in letter_count_dict:
          sorter_letter_count_dict.append({"name": letter, "num": letter_count_dict[letter]})
     sorter_letter_count_dict.sort(reverse=True, key=sort_on)
     for letter in sorter_letter_count_dict:
          if letter["name"].isalpha():
            print(f"The {letter["name"].replace("\n","\\n")} character was found {letter["num"]} times")
     print("--- End report ---")

main()