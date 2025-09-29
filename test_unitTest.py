import pytest
import book_functions as bf


def test_add_book(monkeypatch):
    # Mock user inputs for adding a book
    #A list of fake inputs that simulate what a user would type if they were adding a book
    inputs = iter(["Clean Code", "Robert Martin", "2008", "Programming", "3", "Shelf B1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    bf.add_book()

    # Check if book was added
    new_book = bf.books[-1]
    assert new_book["title"] == "Clean Code"
    assert new_book["author"] == "Robert Martin"
    assert new_book["year"] == "2008"
    assert new_book["total_copies"] == 3
    assert new_book["available_copies"] == 3
    assert new_book["location"] == "Shelf B1"


def test_edit_book(monkeypatch):
    book_id = bf.books[0]["id"]  # Edit first book
    inputs = iter([str(book_id), "Refactored Title", "", "", "", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    bf.edit_book()

    assert bf.books[0]["title"] == "Refactored Title"

