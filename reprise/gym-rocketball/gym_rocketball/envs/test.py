import time

import gym
import numpy as np

from agent import Agent, RB3Mode
from obstacle import Obstacle

env = gym.make("gym_rocketball:rocketball-v0")
env.reset()

agent0 = Agent(id="foo", mode=RB3Mode.Rocket.value, init_pos=np.array([-.5, 1]))
agent1 = Agent(id="bar", mode=RB3Mode.Stepper.value, init_pos=np.array([.5, 1]))
obstacle = Obstacle(id="obs", position=np.array([-.45, 1.5]), color="grey")

env.add_agent(agent0)
env.add_agent(agent1)
env.add_obstacle(obstacle)

actions = [np.array([0.8, 0.8, 0, 0]),
           np.array([0.8, 1, 0, 0])]

for step in range(50):
    print("Step {}".format(step))
    observation, reward, done, info = env.step(actions)
    env.render()
    print(observation)
    print()
    time.sleep(0.1)
