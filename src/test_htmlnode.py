import unittest
from HTMLNode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None, "This is a text node")
        node2 = HTMLNode(None, "This is a text node")
        self.assertEqual(node, node2)

    def test_different_types(self):
        node = TextNode(None, "hello")
        node2 = TextNode(None, "BOOYA")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode(None, None, None, {"href" : "https://www.google.com"})
        node2 = TextNode(None, None, None, {"href" : "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_not_url(self):
        node = TextNode(None, None, None, {"href" : "http://www.boot.dev/")
        node2 = TextNode(None, "hello")
        self.assertNotEqual(node, node2)  

    

if __name__ == "__main__":
    unittest.main()