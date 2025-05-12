import atheris
import sys
import re


"""
Completati functiile de mai si observati cum atheris despisteaza exceptii
"""

def extract_numbers(s: str) -> list:
    """
    Returnează o listă de numere întregi găsite în string.
    Ex: "abc123def45" -> [123, 45]
    TODO
    """
    pass


def safe_divide_list(numbers: list) -> float:
    """
    Împarte primul număr la al doilea.
    TODO
    """
    pass


def list_sum(numbers: list) -> int:
    """
    Calculează suma tuturor numerelor din listă.
    TODO
    """
    pass


def process_input(data: bytes):
    """
    Funcția de fuzzing: transformă datele în string și apelează funcțiile de mai sus.
    """
    fdp = atheris.FuzzedDataProvider(data)
    
    input_str = fdp.ConsumeUnicodeNoSurrogates(50)
    
    numbers = extract_numbers(input_str)
    
    try:
        result_divide = safe_divide_list(numbers)
    except ValueError:
        pass
    
    try:
        result_sum = list_sum(numbers)
    except ValueError:
        pass


def main():
    atheris.Setup(sys.argv, process_input)
    atheris.Fuzz()


if __name__ == "__main__":
    main()