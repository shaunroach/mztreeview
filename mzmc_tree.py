import tree_view
import monte_carlo_tree
import muzero_interface


class MuZeroTree(monte_carlo_tree.MonteCarloTree):
    def __init__(self, state, value, policy, parent=None, children=None):
        monte_carlo_tree.MonteCarloTree.__init__(self, state, parent, children)
        self.value = value
        self.policy = policy

    def expansion(self, mz):
        estates = self.state*len(self.policy)
        actions = mz.valid_actions_from_policy(self.policy)
        self.children = MuZeroTree.create_with_estates_and_actions(estates, actions)
        map(lambda x: x.parent = self, self.children)

    def create_with_game_states(mz, game_states):
        estates = mz.eval_h(game_states)
        values, policies = mz.eval_f(estates)
        nodes = list(map(lambda x,y,z: MuZeroTree(x,y,z), estates, values, policies))
        return nodes

    def create_with_estates_and_actions(mz, estates, actions):
        next_estate = mz.eval_g(estates, actions)
        nodes = MuZeroTree.create_with_game_states(next_estates)
        return nodes


if __name__ == "__main__":
    t = MuZeroTree("astate")
    print(t)
    pass
