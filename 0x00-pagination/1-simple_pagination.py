#!/usr/bin/env python3
'''Server class to paginate a database of popular baby names.
and get a particular page
'''
import csv
import math
from typing import Tuple, Union, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''gets specified page'''
        assert isinstance(page, int) and page > 0, "page must be an integer\
                                                    greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size must\
                                            be an integer greater than 0"
        if page > len(self.dataset()) or page_size > len(self.dataset()):
            return []
        start, end = self.index_range(page, page_size)
        page = self.dataset()[start: end]
        return page

    def index_range(self, page, page_size):
        '''return a tuple of size two containing a start and an end index'''
        starting_point = (page * page_size) - page_size
        end_point = page * page_size

        return (starting_point, end_point)
