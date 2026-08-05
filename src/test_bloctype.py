import unittest

from bloctype import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph."
        self.assertEqual(BlockType.PARAGRAPH, BlockType(block_to_block_type(block)))

    def test_block_to_block_type_heading(self):
        block = "# This is a heading."
        self.assertEqual(BlockType.HEADING, BlockType(block_to_block_type(block)))

    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello, World!')\n```"
        self.assertEqual(BlockType.CODE, BlockType(block_to_block_type(block)))

    def test_block_to_block_type_quote(self):
        block = "> This is a quote."
        self.assertEqual(BlockType.QUOTE, BlockType(block_to_block_type(block)))

    def test_block_to_block_type_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(BlockType.ORDERED_LIST, BlockType(block_to_block_type(block)))

    def test_block_to_block_type_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(BlockType.UNORDERED_LIST, BlockType(block_to_block_type(block)))