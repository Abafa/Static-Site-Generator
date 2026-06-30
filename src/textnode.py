from enum import Enum
from htmlnode import LeafNode, HTMLNode, ParentNode

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6


class TextNode :
    def __init__(self, text: str, text_type: TextType = TextType.TEXT, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"


def text_node_to_html_node(text_node : TextNode) -> LeafNode : 
    if text_node.text_type not in TextType :
        raise Exception ("Text Type error !")
    if text_node.text_type is TextType.TEXT :
        return LeafNode(None, text_node.text, None)
    if text_node.text_type is TextType.BOLD :
        return LeafNode("b", text_node.text, None)
    if text_node.text_type is TextType.ITALIC :
        return LeafNode("i", text_node.text, None)
    if text_node.text_type is TextType.CODE :
        return LeafNode("code", text_node.text, None)
    if text_node.text_type is TextType.LINK :
        return LeafNode("a", text_node.text, {"href":text_node.text})
    if text_node.text_type is TextType.IMAGE :
        return LeafNode("img", None, {"src":text_node.url, "alt":text_node.text})