import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
    
    def test_uneq(self):
        node = HTMLNode(tag="test", value="None", children="test321")
        node2 = HTMLNode(tag="test", value="None", children="test123")
        self.assertNotEqual(node, node2)
    
    def test_leaf(self):
        test_props = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode(tag="a", value="Click me!", props=test_props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')

if __name__ == "__main__":
    unittest.main()