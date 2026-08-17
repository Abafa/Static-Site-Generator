import unittest

from bloctype import block_to_block_type, BlockType, markdown_to_html_node
from htmlnode import HTMLNode

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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
     )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

#OOF ! Don't know why the .to_html does not work... but i'll know soon
