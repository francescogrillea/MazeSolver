from Problem import *

class Labirinto(Problem):

    def __init__(self, initial_state, goal_state, walls, possible_actions=['left', 'up', 'right', 'bottom']):
        super().__init__(initial_state, goal_state)
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.constraints = walls
        self.possible_action = possible_actions

    def actions(self,state):

        possible_action = self.possible_action[:]
        denied_actions = self.constraints[state]
        for a in denied_actions:
            try:
                possible_action.remove(a)
            except ValueError as err:
                pass
        return possible_action

    def result(self, state, action):
        # Restituisce lo stato che si ottiene quando viene eseguita l'azione indicata
        # mentre si e' nella casella indicata da state

        row = int(state[1:2])
        col = int(state[-2:-1])
        if action == 'up':
            row = row - 1
        elif action == 'bottom':
            row = row + 1
        elif action == 'right':
            col = col + 1
        elif action == 'left':
            col = col - 1
        else:
            raise NameError('Invalid move')
        new_state = '('+str(row)+','+str(col)+')'
        return new_state
