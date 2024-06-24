#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Deletion-resilient hypermedia pagination'''
        dataset = self.dataset()
        ln = len(dataset)
        assert isinstance(index, int) and 0 <= index < ln or index is None

        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index

        while len(data) < page_size and next_index < ln:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        next_index = None if next_index >= ln else next_index

        dicto = {"index": index,
                 "next_index": next_index,
                 "page_size": page_size,
                 "data": data
                 }
        return dicto

    def delete_item(self, index: int) -> None:
        """Delete an item from the dataset and update the indexed dataset"""
        if self.__dataset is None or self.__indexed_dataset is None:
            self.dataset()
            self.indexed_dataset()

        # Remove item from both dataset and indexed dataset
        if 0 <= index < len(self.__dataset):
            del self.__dataset[index]
            self.__indexed_dataset = {
                i: item for i, item in enumerate(self.__dataset)
            }
