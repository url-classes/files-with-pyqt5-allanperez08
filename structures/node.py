from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, cancion: T):
        self.cancion: T = cancion
        self.cancion: Optional[Node] = None

