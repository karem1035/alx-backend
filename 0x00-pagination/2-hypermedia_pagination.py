#!/usr/bin/env python3
"""Module to calculate the range of indices for a given page and page size."""


from typing import List
import math
import csv


def index_range(page: int, page_size: int):
    """
    Calculate the range of indices for a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices of the range.

    Example:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 5)
        (5, 10)
    """
    return ((page - 1) * page_size, page * page_size)


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
        """
        retrieves a page from the dataset,
        based on the page number and page size.

        Args:
            page (int): The current page number. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: representing the data on the specified page.
        """

        assert isinstance(page, int) and page > 0, "\
            page must be an integer greater than 0"
        assert isinstance(
            page_size, int) and page_size > 0, "\
                page_size must be an integer greater than 0"
        start, end = index_range(page, page_size)

        if start > len(self.dataset()):
            return []
        return self.dataset()[start:end]


def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
    Retrieves a hypermedia representation of the dataset,
    based on the page number and page size.

    Args:
        page (int): The current page number. Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

    Returns:
        List[List]: representing the hypermedia data on the specified page.
    """

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Page must be and int > 0"
        assert isinstance(
            page_size, int) and page_size > 0, "page_size must be and int > 0"

        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        dict = {}
        dict['page_size'] = len(data)
        dict['page'] = start
        dict['data'] = data
        dict['next_page'] = end if end else None
        dict['prev_page'] = start - 1 if start - 1 else None
        dict['total_page'] = len(self.dataset()) / page_size
        return dict
