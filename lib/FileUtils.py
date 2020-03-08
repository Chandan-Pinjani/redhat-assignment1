#!/usr/bin/env python

"""
Library to deal with file operations
"""

import os
from pathlib import Path

class FileUtils():
    """
    This library is created for file related operations.
    """

    def read_file(self, file_name):
        """
        Function to read file contents from bin directory
        """
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        path = Path(cur_dir)
        cur_dir = path.parent
        file_name = os.path.join(cur_dir, "bin", file_name)
        try:
            with open(file_name, 'r') as fileread:
                data = fileread.read()
                return file_name, data
        except IOError as error:
            print(error)

if __name__ == "__main__":
    pass
