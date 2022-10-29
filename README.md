# **Experiment Tracking Benchmark**

This is a package to test the performance of different experiment tracking tools: Tensorboard, Weights and Biases, Neptune and Comet.

## **Usage**

Make sure you have Python installed:

**1. Install the package with pip in your terminal:**

```
pip install git+https://github.com/AlexandreSajus/Experiment-Tracking-Benchmark.git
```

**2. Run the benchmark with the following command:**

```
python -m trackbench NAME_OF_EXPERIMENT
```

Currently the supported experiments are: tensorboard

This will train DQN and PPO on CartPole and output the experiment tracking website in the terminal.

For example, for tensorboard, the output will be:

```
Hello world from trackbench (Trackbench is a tool for evaluating the performance of experiment tracking tools.)
Training DQN on CartPole...
Total reward: 157.0

Training PPO on CartPole...
Total reward: 500.0

Launching TensorBoard
TensorBoard launched at http://localhost:6006/
Press Ctrl+C to stop TensorBoard
```

You will then be able to access the experiment tracking website at http://localhost:6006/ which will show result curves:

<p align="center">
  <img src="assets/tensorboard_rew.png" alt="Tensorboard Curves" width="80%"/>
</p>
