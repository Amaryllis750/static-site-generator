from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    LINK = "LINK"
    CODE="CODE"
    IMAGE = "IMAGE"


class TextNode:
    def __init__(self, value: str, text_type: TextType, url: str | None = None):
        self.value = value
        self.text_type = text_type
        self.url = url

    def __repr__(self) -> str:
        return f"TextNode({self.value}, {self.text_type}, {self.url})"

    def __eq__(self, textnode: "TextNode") -> bool:
        if (
            self.value == textnode.value
            and self.text_type == textnode.text_type
            and self.url == textnode.url
        ):
            return True
        return False


def textnode_to_htmlnode(textNode: TextNode)-> LeafNode:
    if textNode.text_type not in list(TextType):
        raise Exception("This textnode does not have a valid type")

    tag, value = None, None
    props = {}
    
    value = textNode.value
    
    if textNode.text_type == TextType.BOLD:
        tag = "b"
    elif textNode.text_type == TextType.ITALIC:
        tag = "i"
    elif textNode.text_type == TextType.IMAGE:
        tag = "img"
        value=None
        props = {"src": textNode.url, "alt": textNode.value}
    elif textNode.text_type == TextType.LINK:
        tag = "a"
        props = {"href": textNode.url}
    
    
    return LeafNode(tag, value, props)

print(textnode_to_htmlnode(TextNode("Hello", TextType.LINK, "https://google.com")).to_html())