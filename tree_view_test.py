import tree_view


def test_tree_view():
    tv = tree_view.TreeView()
    out_string = tv.print_html()
    assert(out_string == "")

    anode = tree_view.HtmlNode()
    anode.set_tag("html")
    test_1_out = anode.print_html()
    assert(test_1_out == "<html></html>")

    anode.set_attribute("version", 1)
    test_2_out = anode.print_html()
    assert(test_2_out == "<html version='1'></html>")

    anode.set_inner_text("green")
    test_3_out = anode.print_html()
    assert(test_3_out == "<html version='1'>green</html>")

    bnode = tree_view.HtmlNode()
    bnode.set_tag("p")

    test_4_out = bnode.print_html()
    assert(test_4_out == "<p></p>")

    anode.add_node(bnode)
    test_5_out = anode.print_html()
    assert(test_5_out == "<html version='1'>green<p></p></html>")

    assert(anode.indent_level == 0)
    assert(bnode.indent_level == 1)
