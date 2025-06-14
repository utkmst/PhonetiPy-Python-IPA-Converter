import nltk
# nltk.download('cmudict')
from nltk.corpus import cmudict

class IPAConverter:
    def __init__(self):
        self.cmudict = cmudict.dict()
        self.ipa_conversion = {
            "AA": "ɑ", "AE": "æ", "AH": "ʌ", "AH0": "ə", "AO": "ɔ", "AW": "aʊ",
            "AH0": "ə", "AO": "ɔ", "Q": "ʔ", "AY": "aɪ", "DX": "ɾ",
            "AY": "aɪ", "B": "b", "CH": "tʃ", "D": "d", "DH": "ð",
            "EE": "i:", "EH": "ɛ", "ER": "ɝ", "EY": "eɪ", "F": "f", "G": "ɡ",
            "HH": "h", "IH": "ɪ", "IY": "i", "JH": "dʒ", "K": "k",
            "L": "l", "M": "m", "N": "n", "NG": "ŋ", "OW": "oʊ",
            "OY": "ɔɪ", "P": "p", "R": "ɹ", "S": "s", "SH": "ʃ",
            "T": "t", "TH": "θ", "UH": "ʊ", "UW": "u:", "V": "v",
            "W": "w", "Y": "j", "Z": "z", "ZH": "ʒ", "DX": "ɾ", "Q": "ʔ"
        }

    def get_ipa(self, word):
        word = word.lower()
        if word not in self.cmudict:
            return None
        a_list = self.cmudict[word][0]
        ipa_list = []
        for ph in a_list:
            base_ph = ph.rstrip('012')
            ipa = self.ipa_conversion.get(base_ph)
            if ipa:
                ipa_list.append(ipa)
            else:
                print(f"Warning: No IPA mapping found for CMU phoneme '{base_ph}' (original: '{ph}')")
                ipa_list.append(ph) # Append the original phoneme if no IPA conversion exists
        
        ipa_string = ''.join(ipa_list)
        return ipa_string
    
    def get_ipa_sentence(self, sentence):
        words = sentence.split()
        ipa_sentence_parts = []
        for word in words:
            ipa_for_word = self.get_ipa(word) 
            if ipa_for_word:
                ipa_sentence_parts.append(ipa_for_word)
            else:
                print(f"Warning: No IPA found for word '{word}'")
                ipa_sentence_parts.append(f"[{word}]")
        
        return ' '.join(ipa_sentence_parts)
    
if __name__ == "__main__":
    converter = IPAConverter()
    print("Welcome to the IPA Converter!")
    print("This program converts words to their International Phonetic Alphabet (IPA) representation.")
    print("Please enter a word to get its IPA representation.")
    print("Type 'exit' or 'quit' to quit the program.")
    while True:
        user_selection = input("Would you like to convert a word or a sentence? (word/sentence): ").strip().lower()
        
        if user_selection == "exit" or user_selection == "quit":
            print("Exiting the IPA Converter. Goodbye!")
            break
        
        if user_selection == "word":
            word_input = input("Enter a word: ")
            
            if word_input.lower() in ['exit', 'quit']:
                exit_or_word = input(f"Do you want to exit from program or convert the word '{word_input}'? (exit/convert): ").strip().lower()
                
                if exit_or_word == "exit":
                    print("Exiting the IPA Converter. Goodbye!")
                    break

                elif exit_or_word == "convert":
                    ipa = converter.get_ipa(word_input)
                    if ipa:
                        print(f"IPA for '{word_input}': {ipa}")
                    else:
                        print(f"No IPA found for '{word_input}'.")
                    continue
                else:
                    print("Invalid input. Please type 'exit' or 'quit' to exit the program.")
                    continue
            
            ipa = converter.get_ipa(word_input)       
            
            if ipa:
                print(f"IPA for '{word_input}': {ipa}")
            
            else:
                print(f"No IPA found for '{word_input}'.")
                print("Please try another word.")
            
        
        elif user_selection == "sentence":
            sentence_input = input("Or enter a sentence to convert: ")
            if sentence_input.lower() in ['exit', 'quit']:
                print("Exiting the IPA Converter. Goodbye!")
                break
            
            if sentence_input:
                ipa_sentence = converter.get_ipa_sentence(sentence_input)
                print(f"IPA for '{sentence_input}': {ipa_sentence}")
            else:
                print("No input provided. Please enter a valid sentence.")
        else:
            print("Invalid selection. Please enter 'word' or 'sentence'.")
            
            
        
       

        
