import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parent_to_html(self):
        child1 = LeafNode("p", "Hello, world!")
        child2 = LeafNode("a", "Click Me !", {"href" : "https://www.boots.dev/"})
        parent = ParentNode("div", [child1, child2], {"class" : "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><p>Hello, world!</p><a href="https://www.boots.dev/">Click Me !</a></div>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    


if __name__ == "__main__":
    unittest.main()