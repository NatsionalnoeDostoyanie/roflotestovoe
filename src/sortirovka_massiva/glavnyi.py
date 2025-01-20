from random import randint as sluchaynoe_chislo
from typing import (
    MutableSequence,
    TypeVar,
)


T = TypeVar("T", bound=MutableSequence[int | float])  # TODO: replace "int | float" with any comparable


class SortirovkaMassiva:
    def __init__(self) -> None:
        self.Istina = True
        self.Lozh = False
        self.dlina = len
        self.ohvat = range

    def uporyadochen(self, spisok: MutableSequence[int | float]) -> bool:
        dlina_spiska = self.dlina(spisok)
        for i in self.ohvat(0, dlina_spiska - 1):
            if spisok[i] > spisok[i + 1]:
                return self.Lozh
        return self.Istina

    def peremeshivanie(self, spisok: MutableSequence[int | float]) -> None:
        dlina_spiska = self.dlina(spisok)
        for i in range(0, dlina_spiska):
            nomer_elementa_zadannyi_na_sharu = sluchaynoe_chislo(0, dlina_spiska - 1)
            vremennyi = spisok[i]
            spisok[i] = spisok[nomer_elementa_zadannyi_na_sharu]
            spisok[nomer_elementa_zadannyi_na_sharu] = vremennyi

    def bogo_sort(self, spisok: T) -> T:
        while not self.uporyadochen(spisok):
            self.peremeshivanie(spisok)
        return spisok


print(SortirovkaMassiva().bogo_sort([3, 2, 1]))  # type: ignore[type-var]
