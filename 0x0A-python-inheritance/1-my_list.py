#!/usr/bin/python3

class MyList(list):
    """A class that inherits from list with an additional method."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        sorted_list = sorted(self)
        print(sorted_list)
