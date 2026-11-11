"""Print the Collatz sequence starting at 27 and its total step count."""


def collatz(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    # 27 is step 0, so the step count is the number of transitions.
    print(f"total_steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
