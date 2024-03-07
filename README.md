## Lottery Number Frequency Analyzer

### Overview:
This Python script analyzes the frequency of winning lottery numbers from a JSON dataset. It reads the dataset from a file (`lottery.json`), processes the data to count the occurrences of each winning number, and outputs the five most frequent numbers along with their occurrence counts.

### Dependencies:
- Python 3.x
- `json` module (built-in)

### Usage:
1. Ensure that the `lottery.json` file is located in the `dataset` directory.
2. Run the script `lottery.py`.
3. The script will display the five most frequent lottery numbers along with their occurrence counts.

### Script Overview:
1. The script reads the JSON dataset from `lottery.json` using the `json.load()` function.
2. It extracts the winning lottery tickets from the dataset.
3. For each winning ticket, it splits the numbers and counts their occurrences using a dictionary.
4. It sorts the dictionary by the frequency of occurrences.
5. Finally, it prints the five most frequent numbers.

### Example Output:
```cpp
Five Most frequent numbers that have won the lottery

23 has won 45 times
11 has won 42 times
56 has won 39 times
34 has won 37 times
09 has won 36 times
```

### Author 
Dariel Martinez