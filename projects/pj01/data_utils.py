"""Utility functions."""

__author__ = "730348936"

from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.    
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented tables."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produce new table from old table with only the first N rows."""
    # Step 1
    result: dict[str, list[str]] = {}

    # Step 2
    for column in table:
        list_result: list[str] = []
        i: int = 0
        while i < number_of_rows and i < len(table[column]):
            list_result.append(table[column][i])
            i += 1
        result[column] = list_result

    # Step 3
    return result


# def select
def select(table: dict[str, list[str]], names_of_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only some of the original columns."""
    # Step 1
    result: dict[str, list[str]] = {}

    # Step 2
    for column in names_of_columns:
        result[column] = table[column]
    
    # Step 3
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table from two original tables."""
    # Step 1
    result: dict[str, list[str]] = {}

    # Step 2
    for column in table1:
        result[column] = table1[column]

    # Step 3
    for column in table2:
        if column in result:
            i = 0
            while i < len(table2[column]):
                result[column].append(table2[column][i])
                i += 1
        else:
            result[column] = table2[column]

    # Step 4
    return result


def count(list_of_values: list[str]) -> dict[str, int]:
    """Counts how many times a value appears in a list."""
    # Step 1
    result: dict[str, int] = {}

    # Step 2
    for item in list_of_values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    
    # Step 3
    return result


def find_intersection(table: list[dict[str, str]], first_column: str, first_value: str, second_column: str, second_value: str) -> int:
    """Counts how many times a piece of data has two values we're searching for at once. Requires row-oriented table."""
    # Step 1
    result: int = 0
    i = 0

    # Step 2
    while i < len(table):
        row = table[i]
        if row[first_column] == first_value and row[second_column] == second_value:
            result += 1
        i += 1
    
    # Step 3
    return result


def group_values(table: list[dict[str, str]], column: str, values_to_group: list[str], wanted_value: str) -> None:
    """Goes through row-oriented table and destructively changes values in a column from a list to one specified value."""
    for row in table:
        if row[column] in values_to_group:
            row[column] = wanted_value
    
    return None
    
