"""Examples of imports."""

from lessons import helpers

# import using an alias
from lessons import helpers as hp

# import names directly from globals of a module
from lessons.helpers import THE_ANSWER, powerful


def main() -> None:
    # access the first import
    print(helpers.powerful(2, 4))

    # access the aliased import
    print(hp.THE_ANSWER)

    # call the imported function directly
    print(powerful(2, 10))
    print(THE_ANSWER)

    print(f"imports.py: {__name__}")


if __name__ == "__main__":
    main()