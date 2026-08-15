from enum import Enum
from inline_markdown import markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"


def block_to_block_type(block: str) -> BlockType:
    prefix = ("#", "##", "###", "####", "#####", "######")
    if block.startswith(prefix):
        return BlockType.HEADING
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("```"):
        return BlockType.CODE
    splited_block = block.split("\n")
    if all(line.startswith("- ") for line in splited_block):
        return BlockType.UNORDERED_LIST
    if all(line.split(".")[0].isdigit() for line in splited_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH



def markdown_to_html_node(markdown) :
    splited_markdown = markdown_to_blocks(markdown)
    block_types = [block_to_block_type(block) for block in splited_markdown]
    for block, block_type in zip(splited_markdown, block_types):
        if block_type == BlockType.PARAGRAPH:
            yield to_paragraph(block)
        elif block_type == BlockType.HEADING:
            yield to_heading(block)
        elif block_type == BlockType.CODE:
            yield to_code(block)
        elif block_type == BlockType.QUOTE:
            yield to_blockquote(block)
        elif block_type == BlockType.ORDERED_LIST:
            yield to_ordered_list(block)
        elif block_type == BlockType.UNORDERED_LIST:
            yield to_unordered_list(block)

    return HTMLNode("div", None, list(markdown_to_html_node(markdown)), False)




def to_blockquote(block: str) -> str:
    new_block = block[1:].strip()
    return LeafNode("blockquote", new_block)

def to_code(block: str) -> str:
    new_block = block[3:-3].strip()
    return ParentNode("pre", None, [LeafNode("code", new_block)])

def to_heading(block: str) -> str:
    level = block.count("#")
    new_block = block[level:].strip()
    return LeafNode(f"h{level}", new_block)

def to_paragraph(block: str) -> str:
    return LeafNode("p", block.strip())

def to_ordered_list(block: str) -> str:
    splited_block = block.split("\n")
    list_items = [LeafNode("li", line.split('.', 1)[1].strip()) for line in splited_block]
    return ParentNode("ol", None, list_items)

def to_unordered_list(block: str) -> str:
    splited_block = block.split("\n")
    list_items = [LeafNode("li", line[2:].strip()) for line in splited_block]
    return ParentNode("ul", None, list_items)