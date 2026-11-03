from enum import Enum


class TextType(Enum):
    PLAIN = "PLAIN"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    LINK = "LINK"
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
