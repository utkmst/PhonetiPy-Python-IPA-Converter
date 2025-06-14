# PhonetiPy - Python IPA Converter
## 📝 Description

The Python IPA Converter is a simple yet effective command-line tool that translates English words and sentences into their International Phonetic Alphabet (IPA) representation. Built using Python and the nltk library (specifically the CMU Pronouncing Dictionary), this program helps linguists, language learners, or anyone curious about phonetics visualize how words are pronounced.

# ✨ Features

#### Word Conversion: Get the IPA for individual English words.
#### Sentence Conversion: Transcribe entire sentences into IPA, with spaces correctly separating word pronunciations.
#### Robust Lookup: Leverages the comprehensive CMU Pronouncing Dictionary for accurate phonetic data.
#### User-Friendly Interface: Interactive prompts guide you through the conversion process.
#### Handles Unknown Words: Graciously indicates words not found in the dictionary.
#### "Exit" / "Quit" Handling: Smartly distinguishes between converting the words "exit" or "quit" and exiting the program.

# 🚀 Installation

To get this converter up and running on your local machine, follow these simple steps:

## Clone the Repository (or Download):
If you're using Git, clone the repository to your local machine:

```
bash
git clone https://github.com/utkmst/PhonetiPy-Python-IPA-Converter.git
cd PhonetiPy-Python-IPA-Converter
```

## Create a Virtual Environment (Recommended):
It's good practice to use a virtual environment to manage project dependencies.
```
Bash

python3 -m venv .venv
```
### Activate the Virtual Environment:

#### On macOS/Linux:
```
bash
 
source .venv/bin/activate
```
#### On Windows:
```
bash

.venv\Scripts\activate
```

## Install Dependencies:
Install the required Python packages using pip:
```
bash

pip install -r requirements.txt
```
This will install nltk.

### Download CMU Pronouncing Dictionary:
The program relies on NLTK's CMU Pronouncing Dictionary. You'll need to download it once.
Open a Python interpreter or run your script, and if it's not already downloaded, the program will prompt you, or you can run this command:
```
python

import nltk
nltk.download('cmudict')
```
## 💻 Usage

### Once installed, you can run the program from your terminal:
```
# Activate your virtual environment (if not already active):
Bash

source .venv/bin/activate # macOS/Linux
.venv\Scripts\activate    # Windows
```
### Run the script:
```
bash

python ipa.py
```
### Follow the on-screen prompts:
  The program will guide you to choose between converting a word or a sentence, and then ask for your input.

## Example Interaction:
```
Welcome to the IPA Converter!
This program converts words to their International Phonetic Alphabet (IPA) representation.
Please enter a word to get its IPA representation.
Type 'exit' or 'quit' to quit the program.
Would you like to convert a word or a sentence? (word/sentence): word
Enter a word: hello
IPA for 'hello': hɛloʊ
Would you like to convert a word or a sentence? (word/sentence): sentence
Or enter a sentence to convert: i shot the cupid
IPA for 'i shot the cupid': aɪ ʃɑt ðə kjupɪd
Would you like to convert a word or a sentence? (word/sentence): word
Enter a word: exit
Do you want to exit the program or convert the word 'exit'? (exit/convert): convert
IPA for 'exit': ɛɡzɪt
Would you like to convert a word or a sentence? (word/sentence): exit
Exiting the IPA Converter. Goodbye!
```
## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

#### - Fork the repository.
#### - Create a new branch (git checkout -b feature/your-feature-name).
#### - Make your changes.
#### - Commit your changes (git commit -m 'Add new feature').
#### - Push to the branch (git push origin feature/your-feature-name).
#### - Open a Pull Request.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.

## 📧 Contact

If you have any questions or feedback, feel free to open an issue on this repository.
