import csv
import sys

def load_str_counts(csv_file):
    str_counts = {}
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = row.pop('name')
            str_counts[person] = {str_key: int(str_value) for str_key, str_value in row.items()}
    return str_counts

def find_matching_person(str_counts, sequence):
    max_counts = {str_key: 0 for str_key in str_counts[next(iter(str_counts))]}
    for str_key in max_counts:
        max_counts[str_key] = max_consecutive_repeats(sequence, str_key)
    for person, counts in str_counts.items():
        if counts == max_counts:
            return person
    return "No match"

def max_consecutive_repeats(sequence, str_key):
    str_length = len(str_key)
    max_repeats = 0
    current_repeats = 0
    i = 0
    while i < len(sequence):
        if sequence[i:i+str_length] == str_key:
            current_repeats += 1
            i += str_length
        else:
            max_repeats = max(max_repeats, current_repeats)
            current_repeats = 0
            i += 1
    return max(max_repeats, current_repeats)

def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]

    str_counts = load_str_counts(csv_file)

    with open(sequence_file, 'r') as file:
        sequence = file.read().replace('\n', '')

    person = find_matching_person(str_counts, sequence)
    print(person)

if __name__ == "__main__":
    main()
