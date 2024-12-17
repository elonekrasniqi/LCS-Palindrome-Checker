# LCS-Palindrome-Checker
University of Prishtina
Faculty of Electrical and Computer Engineering

This project is for the Design and Analysis of Algorithms course in Computer and Software Engineering.

## Overview
**MultiLCS** is a Python program designed to calculate the **Longest Common Subsequence (LCS)** among multiple strings (up to 5 strings). Additionally, it checks whether the LCS is a palindrome and recommends the nearest palindrome word based on a provided file.

---

## Features
- Calculates the **LCS** for up to 5 user-provided strings.
- Checks if the resulting LCS is a **palindrome**.
- Recommends the **nearest palindrome** word if the LCS is not a palindrome.
- Saves results to a `results.json` file.
- Provides performance metrics such as execution time.

---
## Setup Instructions
1. Clone this repository or download the `project.py` file.
   ```bash
   git clone https://github.com/elonekrasniqi/LCS-Palindrome-Checker

## DEMO

### Running the Program

To see the project in action, follow these steps:

1. Open your terminal or command prompt.
2. Run the `project.py` file:
   ```bash
   python project.py
3. Follow the interactive prompts.


### Example Input and Output

### Input
```text
Enter the number of strings (maximum 5): 3
Enter string 1: abcdefg
Enter string 2: acdgk
Enter string 3: adg
```

## Processing

The program calculates the **Longest Common Subsequence (LCS)** step by step:

- **Step 1**: LCS between `abcdefg` and `acdgk` → `adg`
- **Step 2**: LCS between `adg` and `adg` → `adg`

After calculating the LCS, the program checks if the LCS is a **palindrome**:

- The LCS `adg` is **not a palindrome**.
- It searches for the nearest palindrome by comparing the LCS with words from the provided `palindrome.txt` file.

---

## Output

```text
Strings entered: ['abcdefg', 'acdgk', 'adg']
Calculating LCS between: abcdefg and acdgk
Calculating LCS between: adg and adg

LCS calculated: adg
LCS length: 3
Execution time: 0.02 seconds
LCS is not a palindrome.
Recommended nearest palindrome: madam

Results saved to 'results.json'.
```

## Contributions

- [Elonë Krasniqi](https://github.com/elonekrasniqi)
- [Dea Llapatinca](https://github.com/ll-dea)
- [Aulona Ramosaj](https://github.com/aulonaramosaj)
- [Arlinda Beqiraj](https://github.com/arlindabeqiraj)
