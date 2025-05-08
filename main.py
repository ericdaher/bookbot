from stats import count_words, count_chars, sort_char_dict
import sys

def get_book_text(filepath):
  try:
    with open(filepath) as f:
      file_contents = f.read();
      return True, file_contents
  except FileNotFoundError:
    return False, "File not found"

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  file_path = sys.argv[1]
  success, txt = get_book_text(file_path)
  if not success:
    print("Could not open the book! Is the path correct?")
    sys.exit(1)

  word_count = count_words(txt)
  char_count = count_chars(txt)
  sorted_char_count = sort_char_dict(char_count)

  print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

  for char_count in sorted_char_count:
    if char_count["char"].isalpha():
      print(f"{char_count['char']}: {char_count['num']}")

  print("============= END ===============")

main()