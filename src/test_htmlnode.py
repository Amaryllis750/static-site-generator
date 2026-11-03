import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", None, {"style": "color:red;"})
        self.assertEqual(f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})", str(node))
    
    def test_props_to_html(self):
        node= HTMLNode("p", "This is a paragraph", None, {"style": "color:red;"})
        self.assertEqual('style="color:red;"', node.props_to_html().strip())
    
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode("p", "This is a paragraph", None, {"style": "color:red;"})
            node.to_html()
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("p", "Hello, world!", {"id": "para"})
        self.assertEqual("<p id=\"para\">Hello, world!</p>", node.to_html())