from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode

def main():
    test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test)

main()