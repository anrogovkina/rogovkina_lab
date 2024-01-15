from pydantic import BaseModel
from typing import List


class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id={self.id!r},name={self.name!r},pages={self.pages!r})'


class Library(BaseModel):
    books: List[Book] = []
    first_book_id = 1
    book_id = 0

    @classmethod
    def get_next_book_id(cls):
        cls.first_book_id += 1

    def get_index_by_book_id(self, book_id: int) -> int:
        if self.id == book_id:
            return self.id
        if book_id == 0:
            raise ValueError("Книги с запрашиваемым id не существует")
