import unittest
from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False


# Prefix Tree
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Test(unittest.TestCase):
    def test1(self):
        t = Trie()
        t.insert("apple")
        self.assertTrue(t.search("apple"))
        self.assertFalse(t.search("app"))
        self.assertTrue(t.startsWith("app"))
        t.insert("app")
        self.assertTrue(t.search("app"))


if __name__ == "__main__":
    unittest.main()
