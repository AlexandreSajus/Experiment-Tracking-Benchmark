"""Example of a module."""

import time

import gym
from stable_baselines3 import DQN, PPO
from tensorboard import program

import trackbench


def run():
    """
    Runs CartPole experiment using TensorBoard.
    """
    print(f"Hello world from {trackbench.__name__} ({trackbench.__doc__})")

    # DQN on CartPole
    print("DQN on CartPole")
    env = gym.make("CartPole-v1")
    model = DQN("MlpPolicy", env, verbose=0, tensorboard_log="logs/dqn_cartpole")
    model.learn(total_timesteps=10000)
    model.save("./models/dqn_cartpole")

    obs = env.reset()
    total_reward = 0
    for _ in range(1000):
        action, _ = model.predict(obs)
        obs, rewards, dones, _ = env.step(action)
        total_reward += rewards
        env.render()
        time.sleep(0.01)
        if dones:
            break

    print(f"Total reward: {total_reward}")
    print("")

    # PPO on CartPole
    print("PPO on CartPole")
    model = PPO("MlpPolicy", env, verbose=0, tensorboard_log="logs/ppo_cartpole")
    model.learn(total_timesteps=10000)
    model.save("./models/ppo_cartpole")

    obs = env.reset()
    total_reward = 0
    for _ in range(1000):
        action, _ = model.predict(obs)
        obs, rewards, dones, _ = env.step(action)
        total_reward += rewards
        env.render()
        time.sleep(0.01)
        if dones:
            break

    print(f"Total reward: {total_reward}")
    print("")
    env.close()

    # Launch TensorBoard
    print("Launching TensorBoard")
    tb = program.TensorBoard()
    tb.configure(argv=[None, "--logdir", "logs"])
    url = tb.launch()
    print(f"TensorBoard launched at {url}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
