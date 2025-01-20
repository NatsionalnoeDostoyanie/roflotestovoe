from typing import Any


# TODO: make it more "built-in list" like to add some abilities, for example - slices
class InfiniteArray:
    def __init__(self, *elements: Any) -> None:
        self.elements = list(elements)
        self.length = len(elements)

    def __getitem__(self, index: int) -> Any:
        return self.elements[index % self.length]


infinite_array = InfiniteArray(1, 2)

print(infinite_array[-3])
