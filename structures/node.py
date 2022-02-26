from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, song: T):
        self.song: T = song
        self.next: Optional[Node] = None

