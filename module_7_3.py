class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self) -> dict:
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                lst_words = []
                for line in file:
                    new_line = line.lower()
                    for char in new_line:
                        if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            new_line = new_line.replace(char, '')
                    lst_words.extend(new_line.split())
                all_words[i] = lst_words
        return all_words

    def find(self, word: str) -> dict:
        res = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.index(word.lower()) + 1
        return res

    def count(self, word: str) -> dict:
        res = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.count(word.lower())
        return res

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего