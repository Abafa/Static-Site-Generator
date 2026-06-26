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
    
