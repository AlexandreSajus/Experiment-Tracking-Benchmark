# **Experiment Tracking Benchmark**

This is a package to test the performance of different experiment tracking tools: `Tensorboard`, `Weights and Biases`, `Neptune`, `Comet` and `ClearML`.

<p align="center">
  <img src="assets/tools.png" alt="Tools" width="40%"/>
</p>

**Table of Contents**
- [**Experiment Tracking Benchmark**](#experiment-tracking-benchmark)
  - [**Usage**](#usage)
  - [**Comparison**](#comparison)
    - [**Tensorboard**](#tensorboard)
    - [**Weights and Biases**](#weights-and-biases)

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

Currently the supported experiments are: `tensorboard`, `wandb`

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

## **Comparison**

### **Tensorboard**

<p align="left">
  <img src="assets/tensorboard_logo.png" alt="Tensorboard Logo" width="3%"/>
</p>

Tensorboard creates a local webpage with curves of the training process. It is supported on many platforms and is really easy to start with but it is not very customizable.

<p align="center">
  <img src="assets/tensorboard_rew.png" alt="Tensorboard Curves" width="40%"/>
</p>

:white_check_mark: Advantages:
- Easy to start
- Supported on many platforms

:x: Disadvantages:
- Difficult to customize
- Limited
- Basic interface

### **Weights and Biases**

<p align="left">
  <img src="assets/wandb_logo.png" alt="Wandb Logo" width="3%"/>
</p>


Weights and Biases records a lot of data about the training process and creates a webpage to visualize it

This allows the creation of customizable dashboards to visualize and analyze the training process.

<p align="center">
  <img src="assets/wandb_dash.png" alt="Wandb Dashboard" width="60%"/>
</p>

But also hosted webpages with reports that you can share with colleagues

<p align="center">
  <img src="assets/wandb_report.gif" alt="Wandb Report" width="60%"/>
</p>

:white_check_mark: Advantages:
- Many features (dashboards, reports, video, audio, ...)
- Very customizable
- Very ergonomic interface
- Supported everywhere with detailed documentation

:x: Disadvantages:
- Requires an account and an internet connection
- Paid when working as a team
- Setup is more complicated, takes time to learn