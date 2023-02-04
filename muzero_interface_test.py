import muzero_interface
import numpy as np
import pdb

def test_dummy_interface():
    di = muzero_interface.DummyMuzero()

    game_state = np.array([[0,0,0]])
    estates = di.eval_h(game_state)
    estate = estates[0]
    assert( np.all(estate == np.array([0,0,0,-1])))

    values, policies = di.eval_f(estates)
    assert( np.all(values == [1]))
    assert( np.all(policies == [0.25, 0.25, 0.25, 0.25]))

    valid_actions = di.valid_actions_from_policy(policies)
    assert( np.all(valid_actions == [[0], [1], [2], [3]]))

    current_estates = np.tile(estate, (len(valid_actions), 1))
    next_estates = di.eval_g(current_estates, valid_actions)
    dummy_result = [[0, 0, 0, -1, 0],[0, 0, 0, -1, 1],[0, 0, 0, -1, 2],[0, 0, 0, -1, 3]]
    assert( np.all(next_estates == dummy_result))



if __name__ == "__main__":
    test_dummy_interface()
