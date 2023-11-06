def solution(letters):
    different_letters = set()  # To store different letters that meet the conditions
    seen_letters = set()  # To keep track of seen letters

    for char in letters:
        if char.isalpha():
            if char.lower() in seen_letters and char.isupper():
                different_letters.add(char.lower())
            seen_letters.add(char.lower())

    return len(different_letters)
