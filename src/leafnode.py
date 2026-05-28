from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if not self.value:
            raise Exception("Value is missing")
        
        if not self.tag:
            return self.value
        
        html_props = self.props_to_html()
        closing_tag = " />" if self.tag == "img" else f"</{self.tag}>"
        return f'<{self.tag}{html_props}>{self.value}{closing_tag}'
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.props})'