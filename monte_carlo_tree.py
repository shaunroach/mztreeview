import random

class MonteCarloTree:
    def __init__(self, state, parent=None, children=None):
        self.state = state
        self.visits = 0
        self.reward = 0
        self.parent = parent
        self.children = children or []

    def add_child(self, child_state):
        child = MonteCarloTree(child_state, parent=self)
        self.children.append(child)
        return child

    def update(self, reward):
        self.visits += 1
        self.reward += reward

    def selection(self):
        """Selection step in the MCTS algorithm"""
        best_child = max(self.children, key=lambda c: c.reward / c.visits +
                         random.random() * 2**(-0.5 * (c.visits)))
        return best_child

    def expansion(self):
        """Expansion step in the MCTS algorithm"""
        raise NotImplementedError("Expansion must be implemented by subclasses")

    def simulation(self):
        """Simulation step in the MCTS algorithm"""
        raise NotImplementedError("Simulation must be implemented by subclasses")

    def backpropagation(self, reward):
        """Backpropagation step in the MCTS algorithm"""
        node = self
        while node:
            node.update(reward)
            node = node.parent

    def run_mcts(self):
        """Run one iteration of the MCTS algorithm"""
        node = self
        while node.children:
            node = node.selection()
        node = node.expansion()
        reward = node.simulation()
        node.backpropagation(-reward)
