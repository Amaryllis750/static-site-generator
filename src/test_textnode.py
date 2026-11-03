import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_type_neq(self):
        node1 = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_url_neq(self):
        node = TextNode("This is a node", TextType.PLAIN)
        node1 = TextNode("This is a node", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node1)


if __name__ == "__main__":
    unittest.main()