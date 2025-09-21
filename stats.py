def get_book_text(filepath):
    with open(filepath) as f:
        my_book_text = f.read()
    return my_book_text

def word_count(my_book_text):
    return len(my_book_text.split())

def per_cha_count(my_book_text):
    my_book_text = my_book_text.lower()
    my_per_cha_count = {}
    for cha in my_book_text:
        if cha in my_per_cha_count:
            my_per_cha_count[cha] += 1
        else:
            my_per_cha_count[cha] = 1
    return my_per_cha_count


def sort_on(items):
    return items["num"]

def book_report(my_cha_count):
    my_dict_list=[]
    for cha_entry in my_cha_count.keys():
        my_dict_list.append({"cha": cha_entry, "num": my_cha_count[cha_entry]})

    my_dict_list.sort(reverse=True, key=sort_on)
    return my_dict_list
