from textnode import TextNode, TextType

def main():
    node = TextNode("This is a paragraph", TextType.PLAIN, None)
    print(node)

if __name__ == "__main__":
    main()