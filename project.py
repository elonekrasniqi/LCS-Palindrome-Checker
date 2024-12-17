import json
import time

class MultiLCS:
    def __init__(self):
        print("Initialization started...")
        try:
            n = int(input("Enter the number of strings (maximum 5): "))
            if n <= 0 or n > 5:
                raise ValueError("Number of strings must be between 1 and 5.")

            self.strings = []
            for i in range(n):
                while True:
                    string = input(f"Enter string {i + 1}: ").strip()
                    if string.isalpha():
                        self.strings.append(string)
                        break
                    else:
                        print("Error: Strings can only contain alphabetic characters. Please try again.")

            if any(s == "" for s in self.strings):
                raise ValueError("Strings cannot be empty.")

        except ValueError as e:
            print(f"Error: {e}")
            exit()

        print(f"Strings entered: {self.strings}")

        start_time = time.time()

        # Calculate LCS for all strings
        lcs_result = self.strings[0]
        for i in range(1, len(self.strings)):
            print(f"Calculating LCS between: {lcs_result} and {self.strings[i]}")
            lcs_result = self.calculate_lcs(lcs_result, self.strings[i])
            if lcs_result == "":
                print("\nError: No common subsequence found among the strings.")
                exit()

        end_time = time.time()

        print(f"\nLCS calculated: {lcs_result}")
        print(f"LCS length: {len(lcs_result)}")
        print(f"Execution time: {end_time - start_time:.2f} seconds")

        # Check if LCS is a palindrome and find the nearest palindrome if not
        if self.is_palindrome(lcs_result):
            print("LCS is a palindrome.")
            nearest_palindrome = lcs_result
        else:
            print("LCS is not a palindrome.")
            nearest_palindrome = self.find_nearest_word_with_common_letters(lcs_result)
            print(f"Recommended nearest palindrome: {nearest_palindrome}")


        self.save_results_to_file(lcs_result, nearest_palindrome)

    def calculate_lcs(self, A, B):
        m, n = len(A), len(B)
        # Initialize DP arrays
        previous = [0] * (n + 1)
        current = [0] * (n + 1)

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    current[j] = previous[j - 1] + 1
                else:
                    current[j] = max(previous[j], current[j - 1])
            previous, current = current, previous  # Swap rows for the next iteration

        # Reconstruction of LCS
        i, j = m, n
        lcs = []
        while i > 0 and j > 0:
            if A[i - 1] == B[j - 1]:
                lcs.append(A[i - 1])
                i -= 1
                j -= 1
            elif previous[j] >= current[j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(reversed(lcs))

    def is_palindrome(self, s):
        print(f"Checking if '{s}' is a palindrome.")
        return s == s[::-1]

    def find_nearest_word_with_common_letters(self, s):
        print(f"Finding the word with the most common letters for LCS: {s}")
        try:
            with open("palindrome.txt", "r") as file:
                words = [line.strip() for line in file if line.strip()]
            if not words:
                print("Warning: No words found in 'palindrome.txt'.")
                return None
        except FileNotFoundError:
            print("Error: 'palindrome.txt' not found.")
            exit()

        def count_common_letters(a, b):
            # Count common letters in order, ensuring the sequence matches
            common = 0
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    common += 1
                    i += 1
                    j += 1
                elif a[i] < b[j]:
                    i += 1
                else:
                    j += 1
            return common

        nearest_word = None
        max_common_letters = -1

        for word in words:
            common_letters = count_common_letters(s, word)
            if common_letters > max_common_letters:
                max_common_letters = common_letters
                nearest_word = word

        return nearest_word

    def save_results_to_file(self, lcs, nearest_palindrome):
        print("Saving results to file...")
        results = {
            "LCS": lcs,
            "Nearest Word": nearest_palindrome
        }
        with open("results.json", "w") as file:
            json.dump(results, file, indent=4)
        print("\nResults saved to 'results.json'.")

if __name__ == "__main__":
    MultiLCS()
