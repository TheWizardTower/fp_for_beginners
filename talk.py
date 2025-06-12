
from enum import Enum
from typing import Callable, Final, NamedTuple

A: Final[int] = 10

# Python won't complain, but mypy will.
A = 11

class Sauce(Enum):
    Marinara = "Marinara"
    Alfredo = "Alfredo"
    GarlicAndOil = "Alfredo"
    
class Pasta(Enum):
    Bowtie = "Bowtie"
    Penne = "Penne"
    Spaghetti = "Spaghetti"
    
class Dish(NamedTuple):
    sauce: Sauce;
    pasta: Pasta;
    
my_favorite: Dish = Dish(sauce=Sauce.GarlicAndOil, pasta=Pasta.Penne)
print(my_favorite)

match my_favorite.sauce:
    case Sauce.Marinara:
        print("Pairs well with a red wine")
    case Sauce.Alfredo:
        print("Goes great with salmon or shrimp!")
    case Sauce.GarlicAndOil:
        print("Weeknight meal of champions!")

# Note that Python/mypy complains that this match is not exhaustive.
match my_favorite:
    case Dish(sauce=Sauce.Marinara, pasta=Pasta.Bowtie):
        print("A classic combination!")
    case Dish(sauce=Sauce.Alfredo, pasta=Pasta.Penne):
        print("A creamy delight!")
    case Dish(sauce=Sauce.GarlicAndOil, pasta=Pasta.Spaghetti):
        print("A simple yet elegant dish!")

myList: list[int] = [1, 2, 3, 4, 5]

myLambda: Callable[[int], int] = lambda x: x * x
myNewList: list[int] = list(map(myLambda, myList))

# prints [1, 4, 9, 16, 25]
print("Mapped List:")
print(myNewList)

myFilterLambda: Callable[[int], bool] = lambda x: x % 2 == 0

myFilteredList: list[int] = list(filter(myFilterLambda, myList))

# prints [2, 4]
print("Filtered List:")
print(myFilteredList)

from functools import reduce

# Reduce functions takes two arguments, the current accumulated value and the
# next element in the list. The result of the function body is assigned to the
# accumulator for the next iteration.
myReduceLambda: Callable[[int, int], int] = lambda acc, elem: acc + elem
myReducedValue: int = reduce(myReduceLambda, myList)

print("Reduced Value:")
print(myReducedValue)

# Use a function that returns an optional instead of an exception.
def safe_divide(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return numerator / denominator

# Example usage of safe_divide
result: float | None = safe_divide(10, 2)
if result is None:
    print("Division by zero is not allowed.")
    exit(code=0)

print(f"Result of division: {result}")

# Python has a notion of "I return this type or that" which we've seen above.
# This is very similar to Either in Haskell, or Result in Rust. We'll use this
# to demonstrate how to return an error that is not an exception, but still
# gives context on what went wrong.

class FileReadError(Enum):
    FILE_NOT_FOUND = "File not found"
    IO_ERROR = "I/O error occurred"

def read_file_with_union(file_path: str) -> str | FileReadError:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return FileReadError.FILE_NOT_FOUND
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return FileReadError.IO_ERROR


