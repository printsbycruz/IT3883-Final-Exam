"""
coin_converter_sprint2.py

IT 3883 Final Exam - Sprint 2
Program: Coin Sentence to Dollar Amount Converter (Corrected Version)

Description:
    Reads one or more pseudo-English sentences describing an amount of
    money in coins (e.g. "4 dimes and 7 quarters") and prints the
    equivalent dollar amount for each sentence, formatted to two
    decimal places.

Changes from Sprint 1 (see Sprint 2 Testing document for details):
    1. Coin values are now stored and summed as whole CENTS (integers)
       instead of dollar amounts (floats). This eliminates floating
       point rounding errors that occurred in Sprint 1
       (e.g. 0.41000000000000003 instead of 0.41).
    2. Output is now formatted with two decimal places using an
       f-string ("{:.2f}"), so amounts such as 4.3 and 1.2 are
       correctly displayed as 4.30 and 1.20.
    3. Denomination words are lower-cased before being looked up, so
       the program no longer crashes on capitalized input such as
       "1 Penny and 2 Nickels".
    4. Unrecognized denomination words now raise a clear, descriptive
       error instead of an unhandled KeyError.

Author: Jonathan Cruz
Sprint: 2 (Corrected Implementation)
"""

# Dictionary mapping each recognized coin word (singular and plural,
# lowercase) to its value in whole CENTS. Using integer cents avoids
# the floating point precision errors seen in Sprint 1.
COIN_VALUES_IN_CENTS = {
    "penny": 1,
    "pennies": 1,
    "nickel": 5,
    "nickels": 5,
    "dime": 10,
    "dimes": 10,
    "quarter": 25,
    "quarters": 25,
}


def parse_sentence(sentence):
    """
    Parses a single sentence of the form:
        "<quantity> <denomination> and <quantity> <denomination> ..."
    and returns the total value in dollars as a float, rounded to the
    nearest cent.

    Raises:
        ValueError: if a denomination word is not recognized, or if a
            clause is not in the expected "<quantity> <denomination>"
            form.
    """
    total_cents = 0

    # Sentences join each quantity/denomination pair with the word "and".
    # Extra surrounding whitespace is tolerated.
    clauses = sentence.strip().split(" and ")

    for clause in clauses:
        words = clause.strip().split()

        if len(words) != 2:
            raise ValueError(
                f"Could not parse clause '{clause}'. Expected a "
                f"quantity followed by a denomination, e.g. '4 dimes'."
            )

        quantity_word, denomination_word = words

        try:
            quantity = int(quantity_word)
        except ValueError:
            raise ValueError(
                f"Expected a numeral quantity but got '{quantity_word}' "
                f"in clause '{clause}'."
            )

        # Normalize case so "Penny", "PENNY", and "penny" all match.
        denomination_key = denomination_word.lower()

        if denomination_key not in COIN_VALUES_IN_CENTS:
            raise ValueError(
                f"Unrecognized denomination '{denomination_word}' in "
                f"clause '{clause}'."
            )

        value_in_cents = COIN_VALUES_IN_CENTS[denomination_key]
        total_cents += quantity * value_in_cents

    # Convert whole cents back to a dollar amount only at the very end,
    # so no rounding error can accumulate during summation.
    return total_cents / 100


def format_dollar_amount(amount):
    """Formats a numeric dollar amount as a string with two decimal
    places, e.g. 4.3 -> '4.30'."""
    return f"{amount:.2f}"


def process_sentences(sentences):
    """
    Given a list of sentences, prints the formatted dollar amount for
    each one.
    """
    for sentence in sentences:
        amount = parse_sentence(sentence)
        print(format_dollar_amount(amount))


def main():
    # Keep accepting sentences until the user submits a blank line.
    print("Enter a coin sentence, or press Enter to finish.")
    while True:
        sentence = input("> ").strip()
        if sentence == "":
            break

        try:
            amount = parse_sentence(sentence)
            print(format_dollar_amount(amount))
        except ValueError as error:
            # Display a clear message and allow the user to try again.
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
