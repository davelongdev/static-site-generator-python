class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node must have a value")
        if self.tag is None:
            return self.value
        else:
            props = self.props_to_html()
            string = f'<{self.tag}{props}>{self.value}</{self.tag}>'
            return string

    def __repr__(self):
        return f'LeafNode({self.value}, {self.tag}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have a tag")
        if not self.children:
            raise ValueError("parent node must have children")
        else:
            props = self.props_to_html()
            children = ''
            for child in self.children:
                children += child.to_html()
            string = f'<{self.tag}{props}>{children}</{self.tag}>'
            return string

    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'

