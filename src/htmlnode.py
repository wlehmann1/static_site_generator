class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        final_string = ''
        if self.props:
            for key, value in self.props.items():
                final_string += ' ' + key + '="' + value + '"'
        return final_string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def props_to_html(self):
        return super().props_to_html()

    def to_html(self):
        properties = ''
        properties += self.props_to_html()
        if not self.value:
            raise ValueError("no value")
        if not self.tag:
            return self.value
        return f'<{self.tag}{properties}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("no tag")
        if not self.children:
            raise ValueError("no children")
        result = ""
        for child in self.children:
            result += child.to_html()
        props = f' {self.props}' if self.props else ''
        return f'<{self.tag}{props}>{result}</{self.tag}>'