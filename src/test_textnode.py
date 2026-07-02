import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_splitter import split_nodes_delimiter

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
        node = TextNode("http://www.boot.dev/", TextType.LINK)
        node2 = TextNode("http://www.boot.dev/", TextType.LINK)
        self.assertEqual(node, node2)

    def test_not_url(self):
        node = TextNode("http://www.boot.dev/", TextType.LINK)
        node2 = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node, node2)  

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("http://www.boot.dev/", TextType.LINK, "http://www.boot.dev/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "http://www.boot.dev/")
        self.assertEqual(html_node.props, {"href":"http://www.boot.dev/"})

    def test_italic(self):
        node = TextNode("YOLO", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "YOLO")

    

if __name__ == "__main__":
    unittest.main()


