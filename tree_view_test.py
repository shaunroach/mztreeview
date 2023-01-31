import tree_view


def test_tree_view():
    tv = tree_view.TreeView()
    out_string = tv.print_html()
    assert(out_string == "")
