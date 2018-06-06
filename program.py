import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

# the quick red fox jumped over the lazy dog
# do red foxes dream of lazy dogs?

# brycexx


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("Cannot search for nothing!")
        return

    matches = search_folder(folder, text)
    match_count = 0
    for i in matches:
        match_count += 1
    print('Found {:,} matches!'.format(match_count))


def print_header():
    print('---------------------')
    print('    File Searcher')
    print('---------------------')


def get_folder_from_user():
    folder = input('What is the folder you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('Input search text [single phrase only]: ')
    return text.lower()


def search_folder(folder, text):

    print('Searching {} for {}...'.format(folder, text))
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folder(full_item, text)
        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    with open(filename, 'r', encoding="ISO-8859-1") as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text = line)
                yield m


if __name__ == '__main__':
    main()
