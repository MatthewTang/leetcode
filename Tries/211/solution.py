import unittest
from typing import Dict, List, Optional


class Node:
    def __init__(self) -> None:
        self.children: Dict[str:Node] = {}
        self.word = False

    def __repr__(self) -> str:
        return f"{self.children}, {self.word}"


class WordDictionary:
    def __init__(self) -> None:
        self.root = Node()

    # O(n), n no. of characters in word
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True

    # O(26^n), n no. of wildcards in word, O(n), n no. of non-wildards in word
    def search(self, word: str) -> bool:
        def dfs(curr: Node, i: int) -> bool:
            c = word[i]
            if c == ".":
                if i == len(word) - 1:
                    res = [
                        curr.children[c].word for c in curr.children.keys()
                    ]  # list max len 26
                    return True in res
                else:
                    res = [
                        dfs(curr.children[c], i + 1) for c in curr.children.keys()
                    ]  # list max len 26
                    return True in res
            else:
                if c not in curr.children:
                    return False
                if i == len(word) - 1:
                    return curr.children[c].word

                return dfs(curr.children[c], i + 1)

        return dfs(self.root, 0)


class Test(unittest.TestCase):
    def test1(self):
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        self.assertFalse(wd.search("pad"))
        self.assertTrue(wd.search("bad"))
        self.assertTrue(wd.search(".ad"))
        self.assertTrue(wd.search("b.."))
        self.assertFalse(wd.search("."))
        self.assertFalse(wd.search(".."))
        self.assertTrue(wd.search("..."))


if __name__ == "__main__":
    unittest.main()
