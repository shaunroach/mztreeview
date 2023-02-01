

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
        self.indent_level = 0

    def set_tag(self, tag):
        self.tag = tag

    def set_inner_text(self, inner_text):
        self.inner_text = inner_text

    def set_attribute(self, key, value):
        self.attribute_pairs[key] = value

    def add_node(self, new_node):
        new_node.recalculate_indent_level(self.indent_level + 1)
        self.nodes.append(new_node)

    '''
    This method sets the indentation method of all nodes inside.
    The children node's indentation is adjusted to the parent identation + 1
    And this is done recursively
    '''
    def recalculate_indent_level(self, new_level):
        self.indent_level = new_level
        map(lambda x: x.recalculate_indent_level(new_level+1), self.nodes)

    def get_attribute_pairs_string(self):
        sorted_keys = sorted(self.attribute_pairs)
        attribute_strings = " ".join(map(lambda x: f"{x}='{self.attribute_pairs[x]}'", sorted_keys))
        return attribute_strings

    def print_html(self, linebreak_characters = '\n', indent_characters="  "):
        attribute_string = self.get_attribute_pairs_string()
        attribute_buffer = " " if len(attribute_string) > 0 else ""
        indent_string = indent_characters*self.indent_level
        start_tag = f"{indent_string}<{self.tag}{attribute_buffer}{attribute_string}>"
        end_tag = f"{indent_string}</{self.tag}>"

        node_strings = list(map(lambda x: x.print_html(), self.nodes))
        node_text = linebreak_characters.join(node_strings)
        if( len(node_text) > 0 ):
            node_text = f"{node_text}{linebreak_characters}"

        inner_text_string = linebreak_characters
        text_indent_string = indent_string + indent_characters
        if( len(self.inner_text) > 0 ):
            inner_text_string = f"{linebreak_characters}{text_indent_string}{self.inner_text}{linebreak_characters}"

        return f"{start_tag}{inner_text_string}{node_text}{end_tag}"
