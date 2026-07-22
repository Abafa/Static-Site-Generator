import unittest

from textnode import TextNode, TextType, text_node_to_html_node, text_to_textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is a text node"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "This is a text node")
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
    
    def test_text_to_textnode_with_bold(self):
        text = "**This is a bold text node**"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "This is a bold text node")
        self.assertEqual(text_nodes[0].text_type, TextType.BOLD)
    
    def test_text_to_textnode_with_italic(self):
        text = "*This is an italic text node*"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "This is an italic text node")
        self.assertEqual(text_nodes[0].text_type, TextType.ITALIC)

    def test_text_to_textnode_with_code(self):
        text = "`This is a code text node`"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "This is a code text node")
        self.assertEqual(text_nodes[0].text_type, TextType.CODE)

    def test_text_to_textnode_with_link(self):
        text = "[This is a link](https://www.boot.dev)"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "This is a link")
        self.assertEqual(text_nodes[0].text_type, TextType.LINK)
        self.assertEqual(text_nodes[0].url, "https://www.boot.dev")
    
    def test_text_to_textnode_with_image(self):
        text = "![This is an image](https://www.boot.dev/image.png)"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "This is an image")
        self.assertEqual(text_nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(text_nodes[0].url, "https://www.boot.dev/image.png")

    def test_text_to_textnode_with_multiple_nodes(self):
        text = "This is a **bold** and *italic* text node with a [link](https://www.boot.dev) and an ![image](https://www.boot.dev/image.png)"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 5)
        self.assertEqual(text_nodes[0].text, "This is a ")
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[1].text, "bold")
        self.assertEqual(text_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(text_nodes[2].text, " and ")
        self.assertEqual(text_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[3].text, "italic")
        self.assertEqual(text_nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(text_nodes[4].text, " text node with a ")
        self.assertEqual(text_nodes[4].text_type, TextType.TEXT)
    
    def test_text_to_textnode_imported(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnode(text)
        self.assertEqual(len(text_nodes), 9)
        self.assertEqual(text_nodes.text, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
    
    


if __name__ == "__main__":
    unittest.main()
