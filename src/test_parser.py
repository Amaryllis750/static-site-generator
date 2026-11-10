import unittest
from textnode import TextNode, TextType
from parser import split_text_by_delimeter


class TestParser(unittest.TestCase):
    def test_split_text_by_delimeter(self):
        node = TextNode("This is my `code` here", TextType.TEXT)
        text_nodes = split_text_by_delimeter([node], "`", TextType.CODE)
        self.assertEqual(3, len(text_nodes))

    def test_list_elements(self):
        node = TextNode("This is my `code` here", TextType.TEXT)
        text_nodes = split_text_by_delimeter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is my", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode("here", TextType.TEXT),
            ],
        text_nodes)
    
    def test_bold_element_first(self):
        node = TextNode("**Daniel** is my name", TextType.TEXT)
        text_nodes = split_text_by_delimeter([node], "**", TextType.BOLD)
        self.assertListEqual([
            TextNode("", TextType.TEXT), 
            TextNode("Daniel", TextType.BOLD), 
            TextNode("is my name", TextType.TEXT)
        ], text_nodes)
