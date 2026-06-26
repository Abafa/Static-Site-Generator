import unittest
from htmlnode import HTMLNode

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



if __name__ == "__main__":
    unittest.main()