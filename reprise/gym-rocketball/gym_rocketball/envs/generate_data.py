import pickle

import gym
import numpy as np

from agent import Agent
from terrain import Terrain

noise = True
num_trajectories = 1000
len_trajectories = 100

env = gym.make("gym_rocketball:rocketball-v0")

for m in [0, 1, 2, 10, 11, 12]:

    data = []

    for i in range(num_trajectories):
        print("{}/{}".format(i, num_trajectories))
        env.reset()
        agent = Agent(id="foo", mode=m, init_pos=np.array([0, 1]))
        env.add_agent(agent)
        if noise:
            terrain_b = Terrain(np.array([-1, 0.5]), np.array([1, 0.8]), 'yellow', gravity=np.array([0, 0]), noise=0.02)
            terrain_l = Terrain(np.array([-1, 0.8]), np.array([-0.5, 1.2]), 'yellow', gravity=np.array([0, 0]), noise=0.02)
            terrain_r = Terrain(np.array([0.5, 0.8]), np.array([1, 1.2]), 'yellow', gravity=np.array([0, 0]), noise=0.02)
            terrain_t = Terrain(np.array([-1, 1.2]), np.array([1, 1.5]), 'yellow', gravity=np.array([0, 0]), noise=0.02)
            env.add_terrain(terrain_b)
            env.add_terrain(terrain_l)
            env.add_terrain(terrain_r)
            env.add_terrain(terrain_t)
        trajectory = []
        for step in range(len_trajectories):
            command = env.get_random_motor_commands()
            output = env.step(command)[0]
            trajectory.append((command, output))
        data.append(trajectory)

    if noise:
        pickle.dump(data, open("noise_mode_{}.data".format(m), "wb"))
    else:
        pickle.dump(data, open("mode_{}.data".format(m), "wb"))
