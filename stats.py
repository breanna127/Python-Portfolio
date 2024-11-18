def mean(lyst):
    """Returns the average of the numbers in lyst.
    Returns 0 if lyst is empty."""
    if len(lyst) == 0:
        return 0
    else:
        total = sum(lyst)
        return total / len(lyst)

def mode(lyst: list[int]) -> int:
    """Returns the mode of the numbers in lyst.
    Returns 0 if lyst is empty."""
    if len(lyst) == 0:
        return 0
    else:
        frequency: dict[int, int] = {}
        for number in lyst:
            frequency[number] = frequency.get(number, 0) + 1
        max_frequency = max(frequency.values())
        modes = [key for key, value in frequency.items() if value == max_frequency]
        # Return the smallest mode if there are multiple modes
        return min(modes) if len(modes) > 1 else modes[0]

def median(lyst):
    """Returns the median of the numbers in lyst.
    Returns 0 if lyst is empty."""
    if len(lyst) == 0:
        return 0
    else:
        lyst.sort()
        midpoint = len(lyst) // 2
        if len(lyst) % 2 == 0:
            # Even number of elements, average the middle two
            return (lyst[midpoint - 1] + lyst[midpoint]) / 2
        else:
            # Odd number of elements, return the middle one
            return lyst[midpoint]

def main():
    """Tests the mean, mode, and median functions."""
    lyst = [1, 2, 2, 5]  # Corrected example list
    print("List:", lyst)
    print("Mean:", mean(lyst))
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))

# The entry point for program execution
if __name__ == "__main__":
    main()
