class HTMLNode:
    def __init__ (self, tag : str = None, value : str = None, children : list = None, props : dict = None) :
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) :
        raise NotImplementedError("this method must be implemented by a subclass")
    
    def props_to_html(self) : 
        props_string = ""
        if self.props == None or not self.props : 
            return props_string

        for k, v in self.props.items() :
            props_string += f' {k}="{v}"'
        return props_string

    def __repr__(self):
        return f"HTMLNode(value={self.value}, tag={self.tag}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    

    def to_html(self):
        if not self.value : 
            raise ValueError("This node should have a value !")
        if self.tag == None : 
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode(value={self.value}, tag={self.tag}, props={self.props})"


class ParentNode(HTMLNode) :
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag : 
            raise ValueError("This node should have a tag !")
        if not self.children : 
            raise ValueError("This node should have a child !")

        output_string = ""
        for child in self.children :
            output_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>" + output_string + f"</{self.tag}>"



#message alakon juste pour pas cramer de frozen flame
#+1