"""Outputs experiment results to TensorBoard"""

import gym
from tensorboard import program
from trackbench.experiment import DQNExperiment, PPOExperiment
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv, VecVideoRecorder
import wandb
from wandb.integration.sb3 import WandbCallback

dqn = DQNExperiment(tensorboard_log="logs/dqn_cartpole")
ppo = PPOExperiment(tensorboard_log="logs/ppo_cartpole")


def run_tensorboard(training_steps: int = 15000) -> str:
    """
    Runs CartPole experiment using TensorBoard.
    """
    dqn.train(training_steps)
    ppo.train(training_steps)

    # Launch TensorBoard
    tb = program.TensorBoard()
    tb.configure(argv=[None, "--logdir", "logs"])
    return tb


def create_wandb_env():
    """
    Creates a recorded and monitored CartPole environment for Weights & Biases.
    """
    env = Monitor(DummyVecEnv([lambda: gym.make("CartPole-v1")]))
    # Record videos
    env = VecVideoRecorder(
        env,
        "videos",
        record_video_trigger=lambda x: x % 10000 == 0,
        video_length=1000,
    )
    return env


def run_wandb(training_steps: int = 15000) -> None:
    """
    Runs CartPole experiment using Weights & Biases.
    """
    print("Please input your wandb username:")
    username = input()

    run = wandb.init(project="trackbench", entity=username, name="dqn")
    env = create_wandb_env()
    dqn.set_env(env)
    dqn.train(
        training_steps,
        callbacks=[
            WandbCallback(
                gradient_save_freq=1000,
                model_save_path=f"models/{run.id}",
                verbose=0,
            )
        ],
    )
    run.finish()

    run = wandb.init(project="trackbench", entity=username, name="ppo")
    env = create_wandb_env()
    ppo.set_env(env)
    ppo.train(
        training_steps,
        callbacks=[
            WandbCallback(
                gradient_save_freq=1000,
                model_save_path=f"models/{run.id}",
                verbose=0,
            )
        ],
    )
    run.finish()
