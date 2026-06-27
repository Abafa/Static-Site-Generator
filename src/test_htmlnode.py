import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None, None, None, {
                                        "href": "https://www.google.com",
                                        "target": "_blank",
                                          })
        expected = ' href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertEqual(result, expected)


    def test_not_eq(self):
        node = HTMLNode(None, None, None, {
                                        "href": "https://www.google.com",
                                          })
        expected = ' href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertNotEqual(result, expected)

    def test_eq_two(self):
        node = HTMLNode(None, None, None, {
                                        "href": "https://www.google.com",
                                        "target": "_blank",
                                        "bully" : "_it_s_not_fine_bro"
                                          })
        expected = ' href="https://www.google.com" target="_blank" bully="_it_s_not_fine_bro"'
        result = node.props_to_html()
        self.assertEqual(result, expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_url(self):
        node = LeafNode("a", "Click Me !", {"href" : "https://www.boots.dev/"})
        self.assertEqual(node.to_html(), '<a href="https://www.boots.dev/">Click Me !</a>')

    def test_leaf_to_html_but_bold(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")


if __name__ == "__main__":
    unittest.main()