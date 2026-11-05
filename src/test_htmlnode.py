import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestLeafNode(unittest.TestCase):
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
        

class TestHTMLNode(unittest.TestCase):
    def test_parent_to_html(self):
        childnode  = LeafNode("p", "Hello, world!")
        parent = ParentNode("div", [childnode])

        self.assertEqual("<div><p>Hello, world!</p></div>", parent.to_html())

    def test_nested_level_two(self):
        childnode = LeafNode("p", "Hello, world!")
        parentnode1 = ParentNode("span", [childnode])
        parentnode2 = ParentNode("div", [parentnode1])
        
        self.assertEqual("<div><span><p>Hello, world!</p></span></div>", parentnode2.to_html())
    
    def test_multiple_children(self):
        childnode = LeafNode("p", "daniel")
        childnode2 = LeafNode("p", "esther", {"style": "color:red;"})
        parentnode = ParentNode("div", [childnode, childnode2])
        
        self.assertEqual("<div><p>daniel</p><p style=\"color:red;\">esther</p></div>", parentnode.to_html())
    
    def test_multiple_nested_children(self):
        childnode = LeafNode("p", "daniel")
        parentnode = ParentNode("span", [childnode], {"style": "padding: 8px;"})
        childnode2 = LeafNode("p", "esther")
        parentnode2 = ParentNode("div", [parentnode, childnode2])

        self.assertEqual("<div><span><p>daniel</p></span><p>esther</p></div>", parentnode2.to_html())
    
    def test_throw_error_on_no_children(self):
        parentnode = ParentNode("div", None)
     
        with self.assertRaises(ValueError):
            parentnode.to_html()
    
    def test_throw_error_on_no_tag(self):
        childnode = LeafNode("p", "daniel")
        parentnode = ParentNode(None, [childnode])
        
        with self.assertRaises(ValueError):
            parentnode.to_html()