import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in punctuation:
                        line = line.replace(symbol, '' if symbol != ' - ' else ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        return {file_name: words.index(word) + 1
                for file_name, words in self.get_all_words().items()
                if word in words}

    def count(self, word):
        word = word.lower()
        return {file_name: words.count(word)
                for file_name, words in self.get_all_words().items()}


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
