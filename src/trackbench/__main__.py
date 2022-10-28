"""Entry module of the package.

You can run this script using:
python -m trackbench

"""

import time

import gym
import stable_baselines3

import trackbench


def main() -> None:
    """Entry point of the package"""
    print(f"Hello world from {trackbench.__name__} ({trackbench.__doc__})")

    # DQN on CartPole
    print("DQN on CartPole")
    env = gym.make("CartPole-v1")
    model = stable_baselines3.DQN("MlpPolicy", env, verbose=0)
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
    model = stable_baselines3.PPO("MlpPolicy", env, verbose=0)
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


if __name__ == "__main__":
    main()
