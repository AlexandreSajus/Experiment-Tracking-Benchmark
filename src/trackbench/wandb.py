"""Wandb experiment"""

import gym
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv, VecVideoRecorder
import wandb
from wandb.integration.sb3 import WandbCallback

import trackbench


def run_wandb():
    """
    Runs CartPole experiment using Wandb.
    """

    print(
        "WARNING: make sure you are logged in to Wandb before running this example (wandb login)"
    )
    print("WARNING: if on Windows, make sure you have admin rights to run this example")
    # DQN on CartPole
    config = {
        "policy_type": "MlpPolicy",
        "total_timesteps": 15000,
        "env_name": "CartPole-v1",
    }

    run = wandb.init(
        project="sb3",
        config=config,
        sync_tensorboard=True,
        monitor_gym=True,
        save_code=True,
        name="dqn",
    )

    def make_env():
        env = gym.make(config["env_name"])
        env = Monitor(env)  # record stats such as returns
        return env

    print("Training DQN on CartPole...")

    env = DummyVecEnv([make_env])
    env = VecVideoRecorder(
        env,
        f"videos/{run.id}",
        record_video_trigger=lambda x: x % 10000 == 0,
        video_length=200,
    )
    model = DQN(config["policy_type"], env, verbose=0, tensorboard_log=f"runs/{run.id}")
    model.learn(
        total_timesteps=config["total_timesteps"],
        callback=WandbCallback(
            gradient_save_freq=1000,
            model_save_path=f"models/{run.id}",
            verbose=0,
        ),
    )
    run.finish()

    # PPO on CartPole
    run = wandb.init(
        project="sb3",
        config=config,
        sync_tensorboard=True,
        monitor_gym=True,
        save_code=True,
        name="ppo",
    )

    print("Training PPO on CartPole...")
    model = PPO(config["policy_type"], env, verbose=0, tensorboard_log=f"runs/{run.id}")
    model.learn(
        total_timesteps=config["total_timesteps"],
        callback=WandbCallback(
            gradient_save_freq=1000,
            model_save_path=f"models/{run.id}",
            verbose=0,
        ),
    )
    run.finish()
    env.close()
