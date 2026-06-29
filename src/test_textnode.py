import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_types(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_same_type(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("http://www.boot.dev/", TextType.LINKS)
        node2 = TextNode("http://www.boot.dev/", TextType.LINKS)
        self.assertEqual(node, node2)

    def test_not_url(self):
        node = TextNode("http://www.boot.dev/", TextType.LINKS)
        node2 = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node, node2)  

    

if __name__ == "__main__":
    unittest.main()


