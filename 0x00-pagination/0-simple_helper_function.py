#!/usr/bin/env python3
'''
return a tuple of size two containing a start index and an end index
'''
from typing import Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''return a tuple of size two containing a start index and an end index'''
    starting_point = (page * page_size) - page_size
    end_point = page * page_size

    return (starting_point, end_point)
