from textnode import TextNode, TextType


def split_text_by_delimeter(
    nodes: list[TextNode], delimeter: str, text_type: TextType
) -> list[TextNode]:
    node_units = []
    for node in nodes:
        if node.text_type is not TextType.TEXT:
            raise Exception("Non TEXT TextNode cannot be split")

        elements = node.value.split(delimeter)
        sub_nodes = [
            TextNode(x.strip(), TextType.TEXT) if i % 2 == 0 else TextNode(x.strip(), text_type)
            for i, x in enumerate(elements)
        ]   
        node_units.extend(sub_nodes)

    return node_units
