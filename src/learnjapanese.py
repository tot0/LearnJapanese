from random import choice
from functools import reduce

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

definitions = {
    # Lesson 1
    "no": "の", "he": "へ", "ke": "け", "i": "い",
    "a": "あ", "ku": "く", "ko": "こ", "ni": "に",

    # Lesson 2
    "ri": "り", "tsu": "つ", "u": "う", "chi": "ち",
    "ra": "ら", "ta": "た", "sa": "さ", "ki": "き",

    # Lesson 3
    "ha": "は", "ho": "ほ", "ma": "ま", "yo": "よ", "na": "な", "o": "お",

    # Lesson 4
    "me": "め", "nu": "ぬ", "ro": "ろ", "ru": "る", "wa": "わ", "re": "れ",
    "ne": "ね", "su": "す", "mu": "む",

    # Lesson 5
    "shi": "し", "mo": "も", "te": "て", "so": "そ", "yu": "ゆ", "to": "と",
    "e": "え",
}

# Add reverse definitions to dict
definitions.update({hiragana: romanji for romanji, hiragana in definitions.items()})

lessons = [
    # Lesson 1
    ["の", "へ", "け", "い", "あ", "く", "こ", "に"],

    # Lesson 2
    ["り", "つ", "う", "ち", "ら", "た", "さ", "き"],

    # Lesson 3
    ["は", "ほ", "ま", "よ", "な", "お"],

    # Lesson 4
    ["め", "ぬ", "ろ", "る", "わ", "れ", "ね", "す", "む"],

    # Lesson 5
    ["し", "も", "て", "そ", "ゆ", "と", "え"],
]

def d(japanese_letters="", sep=""):
    """
    Take string of Hiragana characters and return the Romanji for each
    """
    return sep.join([definitions[letter] for letter in japanese_letters])

def l(n=5, start=0, end=len(lessons)):
    """
    Take n random japanese letters from the chosen lessons
    """
    combined_list = []
    for l in lessons[start:end]:
        for i in l:
            combined_list.append(i)
    return "".join([choice(combined_list) for i in range(n)])

def g(japanese_letters="", romanji_guesses="", sep=""):
    """
    Take string of guesses and determines if correct, prints results
    '-' inidicates no guess,
    """
    answers = d(japanese_letters, ' ').split(' ')
    guesses = romanji_guesses.split(sep)
    results = []
    for idx, guess in enumerate(guesses):
        if guess != '-' and guess == answers[idx]:
            results.append(bcolors.OKGREEN + guess + bcolors.ENDC)
        else:
            results.append(bcolors.FAIL + answers[idx] + bcolors.ENDC)

    print(sep.join(results))

print("Welcome to learn japanese!\n")
print("Run l() to get some random Hiragana.")
print("Run d(_, ' ') to get the Romanji for those Hiragana.")
print("Run g(_, '<guesses>', ' '), where <guesses> is a space seperated string of Romanji guesses for the previous Hiragana, to get marked.")
print("Press Alt+P or up arrow to quickly jump back statements to repeat :)")
