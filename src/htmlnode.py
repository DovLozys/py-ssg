class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        attributes_string = ""
        for prop in self.props:
            attributes_string += f' {prop}="{self.props[prop]}"'
        return attributes_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
