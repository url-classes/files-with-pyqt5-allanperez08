from typing import Optional, TypeVar, Generic
from structures.node import Node

T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def _search_by_position(self, position: int) -> Node:
        current = self._head
        current_position = 0
        while current_position < self._size:
            if current_position == position:
                return current
            else:
                current = current.next
        raise "Position doesn't exist inside the list"

    def _search_by_data(self, song: T) -> Node:
        current = self._head
        while current is not self._tail:
            if current.song == song:
                return current
            else:
                current = current.next
        if current.song == self._tail.song:
            return self._tail
        else:
            raise Exception("The node doesn't exist inside the list")

    def is_empty(self) -> bool:
        return self._head is None and self._tail is None and self._size == 0

    def append(self, song: T) -> None:
        new_node = Node(song)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._tail.next = self._head
        self._size += 1

    def prepend(self, song: T) -> None:
        if self.is_empty():
            new_node = Node(song)
            self._head = new_node
            self._tail = new_node
            self._tail.next = self._head
            self._size += 1
        else:
            new_node = Node(song)
            new_node.next = self._head
            self._head = new_node
            self._tail.next = self._head
            self._size += 1

    def traversal(self) -> str:
        result: str = ''
        aux: Node = self._head
        while aux is not self._tail:
            result += str(aux.song) + '->'
            aux = aux.song
        result += str(self._tail.song)
        return result

    def remove_first(self) -> T:
        if self.is_empty() is True:
            raise Exception('Subdesbordamiento de listas')
        elif self._head == self._tail:
            current = self._head
            self._head = None
            self._tail = None
            self._size -= 1
            return current
        else:
            current = self._head
            self._head = current.next
            current.next = None
            self._size -= 1
            return current

    def remove_last(self) -> T:
        current = self._tail
        prev = self._search_by_position(self._size - 2)
        self._tail = prev
        self._tail.next = self._head
        current.next = None
        return current.song

    def remove(self, song: T) -> T:
        current = self._search_by_data(song)
        if current is self._head:
            return self.remove_first()
        elif current is self._tail:
            return self.remove_last()
        else:
            position = self.search_position_node(song)
            anterior = self.searh_nodo_position(position - 1)
            posterior = self.searh_nodo_position(position + 1)
            anterior.next = posterior
            current.next = None
            self._size -= 1
            return current

    def search_position_node(self, song: T) -> int:
        current = self._head
        index = 0
        while current is not self._tail:
            if current.song == song:
                return index
            else:
                current = current.next
                index += 1
        if current.song == self._tail.song:
            return index
        else:
            raise Exception("The node doesn't exist inside the list")

    def searh_nodo_position(self, posicion) -> Node:
        index = 0
        current = self._head
        while current is not None:
            # ¿Es {posicion} igual a {iteraciones}?
            if posicion == index:
                return current
            else:
                index += 1
                current = current.song
        raise Exception('La posicion no existe')

    def searh_nodo_value(self, value) -> Node:
        current = self._head
        while current is not None:
            if value == current.song:
                return current
            else:
                current = current.next
        raise Exception("El elemento no existe")

    def anterior(self):
        return self._tail

    def actual(self):
        return self._head

    @property
    def tail(self):
        return self._tail
