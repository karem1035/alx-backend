#!/usr/bin/env python3
"""Module to calculate the range of indices for a given page and page size."""


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
