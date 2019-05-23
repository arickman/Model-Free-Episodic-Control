#!/usr/bin/env python3

import os
import random
import time

import gym

from mfec.agent import MFECAgent
from mfec.utils import Utils

ENVIRONMENT = "Qbert-v0"  # More games at: https://gym.openai.com/envs/#atari
#AGENT_PATH = "agents/Qbert-v0_1558646022/agent.pkl"
AGENT_PATH = ""
RENDER = False
RENDER_SPEED = 0.04

EPOCHS = 5
FRAMES_PER_EPOCH = 100000
SEED = 42

ACTION_BUFFER_SIZE = 1000000
K = 11 # Number of nearest neighbors. Can tune.
DISCOUNT = 1
EPSILON = 0.005

FRAMESKIP = 4  # Default gym-setting is (2, 5)
REPEAT_ACTION_PROB = 0.0  # Default gym-setting is .25

SCALE_HEIGHT = 84
SCALE_WIDTH = 84
STATE_DIMENSION = 64

# Tune this between [0, 1]. 0 = Frequency weighting, 1 = No frequency weighting
# AGGRESSION = 1.0
# UPDATE_TYPE = 'simple average'

def main():
    random.seed(SEED)

    # Create agent-directory
    execution_time = str(round(time.time()))
    agent_dir = os.path.join("agents", ENVIRONMENT + "_" + execution_time)
    os.makedirs(agent_dir)

    # Initialize utils, environment and agent
    utils = Utils(agent_dir, FRAMES_PER_EPOCH, EPOCHS * FRAMES_PER_EPOCH)
    env = gym.make(ENVIRONMENT)

    try:
        env.env.frameskip = FRAMESKIP
        env.env.ale.setFloat("repeat_action_probability", REPEAT_ACTION_PROB)
        if AGENT_PATH:
            agent = MFECAgent.load(AGENT_PATH)
        else:
            agent = MFECAgent(
                ACTION_BUFFER_SIZE,
                K,
                DISCOUNT,
                EPSILON,
                SCALE_HEIGHT,
                SCALE_WIDTH,
                STATE_DIMENSION,
                range(env.action_space.n),
                SEED,
            )
        run_algorithm(agent, agent_dir, env, utils)

    finally:
        utils.close()
        env.close()


def run_algorithm(agent, agent_dir, env, utils):
    frames_left = 0
    for _ in range(EPOCHS):
        frames_left += FRAMES_PER_EPOCH
        while frames_left > 0:
            episode_frames, episode_reward = run_episode(agent, env)
            frames_left -= episode_frames
            utils.end_episode(episode_frames, episode_reward)
        utils.end_epoch()
        agent.save(agent_dir)


def run_episode(agent, env):
    episode_frames = 0
    episode_reward = 0

    env.seed(random.randint(0, 1000000))
    observation = env.reset()

    done = False
    while not done:

        if RENDER:
            env.render()
            time.sleep(RENDER_SPEED)

        action = agent.choose_action(observation)
        observation, reward, done, _ = env.step(action)
        agent.receive_reward(reward)

        episode_reward += reward
        episode_frames += FRAMESKIP

    agent.train()
    return episode_frames, episode_reward


if __name__ == "__main__":
    main()
