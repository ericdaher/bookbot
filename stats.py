def count_words(str):
  return len(str.split())
  
def count_chars(str):
  char_count = {}
  for char in str:
    lowered_char = char.lower()
    if lowered_char in char_count:
      char_count[lowered_char] += 1
    else:
      char_count[lowered_char] = 1
  
  return char_count

def sort_char_dict(dict):
  dict_list = []
  for kv_pair in dict:
    dict_list.append({ "char": kv_pair, "num": dict[kv_pair]})

  dict_list.sort(key=lambda dict: dict["num"], reverse=True)
  return dict_list