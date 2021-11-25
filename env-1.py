import random

class Thing:

    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def is_alive(self):
        return hasattr(self, 'alive') and self.alive


class Room:

    def __init__(self, per) -> None:
        self.per = per


class RandomAgent(Thing):

    def __init__(self, position) -> None:
        self.position = position
        self.alive = True
        self.actions = ['right', 'left', 'suck', 'noop']

    def get_action(self, actions: list):
        return random.choice(actions)

    def program(self, percept, env):
        action = random.choice(self.actions)
        if action == 'suck':
            print('Agent sucking')
            env.per = 0
        elif action == 'noop':
            return
        elif action == 'left':
            if room_count > 1:
                if self.position >= 1:
                    self.position -= 1
                else:
                    self.position += 1
        elif action == 'right':
            if room_count > 1:
                if self.position <= room_count - 2:
                    self.position += 1
                else:
                    self.position -= 1
        return action


class Environment:

    def __init__(self, room_count) -> None:
        self.agent = RandomAgent(random.randint(0, room_count - 1))
        self.envs = []
        self.add_obj()

        print('Initial position ' + str(self.agent.position))

    def execute_action(self, action):
        if action == 'suck':
            print('After :' + str(self.envs[self.agent.position].per))

    def step(self):
        if not self.is_done():
            action = self.agent.program(self.percept(agent=self.agent), self.envs[self.agent.position])
            self.execute_action(action)
            self.exogeneous_change()

    def exogeneous_change(self):
        for i in range(len(self.envs) - 1):
            if random.randint(0, 9) == 9:
                self.envs[i].per = 1

    def is_done(self):
        self.agent.alive = False
        for env in self.envs:
            if env.per == 1:
                self.agent.alive = True
        return not self.agent.alive

    def percept(self, agent: RandomAgent):
        return self.envs[agent.position].per

    def run(self, steps=1000):
        for _ in range(steps):
            if self.is_done():
                return
            self.step()

    def add_obj(self):
        for _ in range(room_count):
            self.envs.append(Room(random.randint(0, 1)))


room_count = int(input('Enter room count: '))
env = Environment(room_count)
[print(item.per) for item in env.envs]
env.run()
[print(item.per) for item in env.envs]
print('Done cleaning')
