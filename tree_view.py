

class TreeView():
    def __init__(self):
        self.root = None


    def print_html(self):
        if( self.root == None ):
            return ""


class HtmlNode():
    def __init__(self):
        self.tag = ""
        self.inner_text = ""
        self.attribute_pairs = {}
        self.nodes = []

    def set_tag(self, tag):
        self.tag = tag

    def set_inner_text(self, inner_text):
        self.inner_text = inner_text

    def set_attribute(self, key, value):
        self.attribute_pairs[key] = value

    def add_node(self, new_node):
        self.nodes.append(new_node)

    def get_attribute_pairs_string(self):
        sorted_keys = sorted(self.attribute_pairs)
        attribute_strings = " ".join(map(lambda x: f"{x}='{self.attribute_pairs[x]}'", sorted_keys))
        return attribute_strings

    def print_html(self):
        attribute_string = self.get_attribute_pairs_string()
        attribute_buffer = " " if len(attribute_string) > 0 else ""
        start_tag = f"<{self.tag}{attribute_buffer}{attribute_string}>"
        end_tag = f"</{self.tag}>"

        node_strings = list(map(lambda x: x.print_html(), self.nodes))
        node_text = "".join(node_strings)

        return f"{start_tag}{self.inner_text}{node_text}{end_tag}"
