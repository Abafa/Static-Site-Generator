from enum import Enum

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



#dont wanna waste a frozen flame ! 