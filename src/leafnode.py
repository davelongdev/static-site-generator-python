from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag=None, props=None)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node must have a value")
        if self.tag is None:
            return self.value
        else:
            props = self.props_to_html()
            string = f'<{self.tag} {props}>{self.value}<{self.tag}>'
            return string

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
