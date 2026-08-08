from enum import Enum
from inline_markdown import markdown_to_blocks
from HTMLNode import HTMLNode

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




def to_blockquote(block: str) -> str:
    new_block = block[1:].strip()
    return f"<blockquote>{new_block}</blockquote>"

def to_code(block: str) -> str:
    new_block = block[3:-3].strip()
    return f"<pre><code>{new_block}</code></pre>"

def to_heading(block: str) -> str:
    level = block.count("#")
    new_block = block[level:].strip()
    return f"<h{level}>{new_block}</h{level}>"

def to_paragraph(block: str) -> str:
    return f"<p>{block.strip()}</p>"

def to_ordered_list(block: str) -> str:
    splited_block = block.split("\n")
    list_items = [f"<li>{line.split('.', 1)[1].strip()}</li>" for line in splited_block]
    return f"<ol>{''.join(list_items)}</ol>"

def to_unordered_list(block: str) -> str:
    splited_block = block.split("\n")
    list_items = [f"<li>{line[2:].strip()}</li>" for line in splited_block]
    return f"<ul>{''.join(list_items)}</ul>"