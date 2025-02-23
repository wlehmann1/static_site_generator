from enum import Enum
from htmlnode import LeafNode

TextType = Enum("TextType", ['NORMAL','BOLD','ITALIC','CODE','LINK','IMAGE'])

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    props = {}
    if text_node.text_type == TextType.NORMAL:
        return LeafNode("", text_node.text, props)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, props)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, props)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, props)
    elif text_node.text_type == TextType.LINK:
        props["href"] = text_node.url
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == TextType.IMAGE:
        props["src"] = text_node.url
        props["alt"] = text_node.text
        return LeafNode("img", "", props)
    else:
        raise Exception("Not a valid TextType")