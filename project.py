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
        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Reconstruction of LCS
        i, j = m, n
        lcs = []
        while i > 0 and j > 0:
            if A[i - 1] == B[j - 1]:
                lcs.append(A[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(reversed(lcs))

    def is_palindrome(self, s):
        print(f"Checking if '{s}' is a palindrome.")
        return s == s[::-1]

    def longest_consecutive_subsequence_length(self, a, b):
        """Finds the longest consecutive matching subsequence length between two strings."""
        max_length = 0
        n, m = len(a), len(b)

        for i in range(n):
            current_length = 0
            for j in range(m):
                k = 0
                while i + k < n and j + k < m and a[i + k] == b[j + k]:
                    k += 1
                    current_length += 1
                max_length = max(max_length, current_length)
                current_length = 0  # Reset for next starting point in b

        return max_length

    def find_nearest_word_with_common_letters(self, s):
        print(f"Finding the word with the most consecutive matching letters in order for LCS: {s}")
        try:
            with open("palindrome.txt", "r") as file:
                words = [line.strip() for line in file if line.strip()]
            if not words:
                print("Warning: No words found in 'palindrome.txt'.")
                return None
        except FileNotFoundError:
            print("Error: 'palindrome.txt' not found.")
            exit()

        nearest_word = None
        max_consecutive_length = -1

        for word in words:
            consecutive_length = self.longest_consecutive_subsequence_length(s, word)
            print(f"Comparing with word '{word}': Longest consecutive subsequence length = {consecutive_length}")
            if consecutive_length > max_consecutive_length:
                max_consecutive_length = consecutive_length
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
