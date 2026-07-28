"""
coin_converter_sprint1.py

IT 3883 Final Exam - Sprint 1
Program: Coin Sentence to Dollar Amount Converter

Description:
    Reads one or more pseudo-English sentences describing an amount of
    money in coins (e.g. "4 dimes and 7 quarters") and prints the
    equivalent dollar amount for each sentence.

Author: Jonathan Cruz
Sprint: 1 (Initial Implementation)
"""

# Dictionary mapping each recognized coin word (singular and plural)
# to its value in dollars.
COIN_VALUES = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25,
}


def parse_sentence(sentence):
    """
    Parses a single sentence of the form:
        "<quantity> <denomination> and <quantity> <denomination> ..."
    and returns the total value in dollars as a float.
    """
    total = 0.0

    # Sentences join each quantity/denomination pair with the word "and".
    clauses = sentence.split(" and ")

    for clause in clauses:
        # Each clause should contain exactly two words: a quantity and
        # a denomination, e.g. "4 dimes".
        words = clause.strip().split()
        quantity_word = words[0]
        denomination_word = words[1]

        quantity = int(quantity_word)
        value = COIN_VALUES[denomination_word]

        total += quantity * value

    return total


def process_sentences(sentences):
    """
    Given a list of sentences, prints the dollar amount for each one.
    """
    for sentence in sentences:
        amount = parse_sentence(sentence)
        print(amount)


def main():
    # Sample input corresponding to the exam's test cases.
    test_sentences = [
        "1 penny and 2 nickels",
        "4 dimes and 7 quarters",
        "1 quarter and 3 pennies",
        "21 pennies and 17 dimes and 52 quarters",
        "95 dimes and 73 quarters and 22 nickels and 36 pennies",
        "1 nickel and 17 quarters",
        "21 nickels and 15 pennies",
        "1 dime and 1 nickel and 1 penny and 1 quarter",
    ]

    process_sentences(test_sentences)


if __name__ == "__main__":
    main()
