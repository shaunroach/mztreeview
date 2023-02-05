import numpy as np

class MuZeroInterface():
    def __init__(self):
        pass

    def eval_h(self, states):
        return states

    def eval_f(self, estates):
        return values, policies

    def eval_g(self, estates, actions):
        return states

    def valid_actions_from_policy(self, policy):
        return actions


class DummyMuzero(MuZeroInterface):
    def __init__(self):
        pass

    def eval_h(self, states):
        def append_neg_one(arr):
            return np.append(arr, [-1])
        estates = np.apply_along_axis(append_neg_one, 1, states)
        return estates

    def eval_f(self, estates):
        num_dummy_actions = 4
        dummy_values = [1]*len(estates)
        dummy_policy = [float(1)/num_dummy_actions]*num_dummy_actions
        dummy_policies = np.tile(dummy_policy, (len(estates), 1))
        #estates = np.tile(self.state, (len(self.policy), 1))
        return dummy_values, dummy_policies

    def eval_g(self, estates, actions):
        new_estates = np.concatenate((estates, actions), axis=1)
        return new_estates

    def valid_actions_from_policy(self, policy):
        nonzero_indices = np.nonzero(policy)
        nonzero_indices_arrs = list(map(lambda x: [x], nonzero_indices[0]))
        return nonzero_indices_arrs
