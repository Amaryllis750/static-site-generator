import unittest
from textnode import TextNode, TextType, textnode_to_htmlnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_type_neq(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_url_neq(self):
        node = TextNode("This is a node", TextType.TEXT)
        node1 = TextNode("This is a node", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node1)

    def test_to_html(self):
        node = TextNode("This is some link", TextType.LINK , "https://www.google.com")
        self.assertEqual("<a href=\"https://www.google.com\">This is some link</a>", textnode_to_htmlnode(node).to_html())


if __name__ == "__main__":
    unittest.main()