'''
This file contains the function to convert a numerical value to its corresponding word representation.
'''
def convert_to_words(number):
    # Define word representations for numbers up to 19
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    # Define word representations for tens
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    # Define word representations for powers of 10
    powers_of_10 = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion",
                    "septillion", "octillion", "nonillion", "decillion", "undecillion", "duodecillion"]
    # Handle negative numbers
    if number < 0:
        return "negative " + convert_to_words(abs(number))
    # Handle zero
    if number == 0:
        return "zero"
    # Convert the number to words
    words = []
    power_index = 0
    while number > 0:
        # Get the last three digits of the number
        last_three_digits = number % 1000
        number //= 1000
        # Convert the last three digits to words
        last_three_digits_words = []
        hundreds_digit = last_three_digits // 100
        if hundreds_digit > 0:
            last_three_digits_words.append(units[hundreds_digit] + " hundred")
        last_two_digits = last_three_digits % 100
        if last_two_digits < 20:
            last_three_digits_words.append(units[last_two_digits])
        else:
            tens_digit = last_two_digits // 10
            last_three_digits_words.append(tens[tens_digit])
            ones_digit = last_two_digits % 10
            if ones_digit > 0:
                last_three_digits_words.append(units[ones_digit])
        # Add the word representation of the last three digits to the overall words
        if last_three_digits_words:
            words.append(" ".join(last_three_digits_words) + " " + powers_of_10[power_index])
        power_index += 1
    return " ".join(words[::-1])