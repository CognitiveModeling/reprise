from gym.envs.registration import register

register(
    id='rocketball-v0',
    entry_point='gym_rocketball.envs:RocketballEnv',
)
