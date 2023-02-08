import tree_view
import monte_carlo_tree
import muzero_interface
import pdb
import random
import numpy as np


def make_mz_html(mznode):
    root = tree_view.HtmlNode()
    root.set_tag("ul")
    root.set_inner_text(f"{mznode.state} - {mznode.value}")
    def make_list_item_for_action(action, action_prob, child_mznode):
        li_node = tree_view.HtmlNode()
        li_node.set_tag("li")
        li_node.set_inner_text(f"{action} ({action_prob*100}%)")
        li_node.nodes.append(make_mz_html(child_mznode))
        return li_node
    root.nodes = list(map(lambda x,y,z: make_list_item_for_action(x,y,z), mznode.actions, mznode.policy, mznode.children))
    return root




class MuZeroTree(monte_carlo_tree.MonteCarloTree):
    def __init__(self, state, value, policy, parent=None, children=None):
        monte_carlo_tree.MonteCarloTree.__init__(self, state, parent, children)
        self.expanded = False
        self.value = value
        self.policy = policy
        self.actions = []

    def expansion(self, mz):
        if( self.expanded ):
            random_child = random.choices(self.children, weights=self.policy, k=1)[0]
            random_child.expansion(mz)
            return
        estates = np.tile(self.state, (len(self.policy), 1))
        self.actions = mz.valid_actions_from_policy(self.policy)
        self.children = MuZeroTree.create_with_estates_and_actions(mz, estates, self.actions)
        map(lambda x: set_attr(x, "parent", self), self.children)
        self.expanded = True

    def create_with_game_states(mz, game_states):
        estates = mz.eval_h(game_states)
        values, policies = mz.eval_f(estates)
        nodes = list(map(lambda x,y,z: MuZeroTree(x,y,z), estates, values, policies))
        return nodes

    def create_with_estates_and_actions(mz, estates, actions):
        next_estates = mz.eval_g(estates, actions)
        values, policies = mz.eval_f(next_estates)
        nodes = list(map(lambda x,y,z: MuZeroTree(x,y,z), next_estates, values, policies))
        return nodes





if __name__ == "__main__":
    mz = muzero_interface.DummyMuzero()
    t = MuZeroTree(np.array([0,0,0]), 0.5, [0.15, 0.15, 0.25, 0.45])
    for i in range(50):
        t.expansion(mz)
    html = make_mz_html(t)
    html.html_to_file("./test.html")
    pass
