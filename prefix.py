from nltk.tokenize import word_tokenize
import string


class PrefixesExtraction():

    def __init__(self, file, no_pref= 3):

        self.file = file
        self.no_pref = no_pref

    def unique_words(self):
        s = "string. With. Punctuation?"
        table = str.maketrans({key: None for key in string.punctuation})
        content = open(self.file, 'r').read()
        all_words = []
        short_yor = word_tokenize(content)
        for w in short_yor:
            all_words.append(w.lower())
        all_words = set(all_words)
        all_word = [ words.translate(table) for words in all_words]
        return all_word

    def prefixes_extraction(self):
        _word_list = self.unique_words()
        WD = []
        the_collection_of_words_with_same_prefix = {}
        for word in _word_list:
            WD.append(word[:self.no_pref])
            for prefix in WD:
                if WD.count(prefix) > 1:
                    WD.remove(prefix)
            for second_prefix in WD:
                words_with_same_prefix = []
                for words in _word_list:
                    if second_prefix == words[:self.no_pref]:
                        words_with_same_prefix.append(words)
                    the_collection_of_words_with_same_prefix[second_prefix] = words_with_same_prefix
        cleaning_of_prefixes = {}
        for Pref_words in the_collection_of_words_with_same_prefix:
            if len(Pref_words) == self.no_pref:
                cleaning_of_prefixes[Pref_words] = the_collection_of_words_with_same_prefix[Pref_words]
        return cleaning_of_prefixes

y = PrefixesExtraction('Test.txt')
print(y.prefixes_extraction())


