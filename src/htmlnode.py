class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str]={},
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("This has not been implemented yet")
    
    def props_to_html(self)->str:
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str|None, value:str, props: dict[str, str]={}):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("value cannot be empty for a leaf Node")

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] = {}):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.children:
            raise ValueError("A parent node should have children")
        if not self.tag:
            raise ValueError("A parent node must have a tag")

        children_html: list[str] = []
        # return the html representation of this parent node
        for child in self.children:
            
            if isinstance(child, LeafNode):
                children_html.append(child.to_html())
            elif isinstance(child, ParentNode):
                html: list[str] = child.to_html()
                children_html.extend(html)
        
        return f"<{self.tag}>{''.join(children_html)}</{self.tag}>"
    