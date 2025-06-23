import re

def add(numbers: str) -> int:
    """String-calculator kata: sum comma/ newline-separated numbers,
    optional custom delimiter (“//<delim>\n…”), and reject negatives."""
    if not numbers:
        return 0

    # Check for custom delimiter
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        pattern = re.escape(delimiter)
    else:
        pattern = ",|\n"
    
    nums = [int(n) for n in re.split(pattern, numbers) if n]
    negatives = [str(n) for n in nums if n < 0]

    if negatives:
        raise Exception(f"negative numbers not allowed: {', '.join(negatives)}")

    return sum(nums)