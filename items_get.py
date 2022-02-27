from bottle import get, view
import g
items = [
    {"id": "1", "name": "a"},
    {"id": "2", "name": "b"},
    {"id": "3", "name": "c"}
]
# my original get item code


@get("/items")
@view("items")
def _():
    return dict(items=g.ITEMS)
