class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        self._author = new_author


class PaperBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, new_duration: int) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительноcть книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительноcть книги должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Аудиокнига {self.__name}. Автор {self.__author}"
