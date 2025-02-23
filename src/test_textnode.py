import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_uneq(self):
        node = TextNode("Test", TextType.NORMAL)
        node2 = TextNode("Test", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == ""
        assert html_node.value == "Hello, world!"
        assert html_node.props == {}
    
    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Click me!", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "a"
        assert html_node.value == "Click me!"
        assert html_node.props == {"href": "https://boot.dev"}

if __name__ == "__main__":
    unittest.main()