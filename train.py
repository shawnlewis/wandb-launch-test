#!/usr/bin/env python
import argparse
import os
import random
import time
import sys
import random

import wandb


parser = argparse.ArgumentParser()
parser.description = 'Train an example model'
parser.add_argument('--print_repeat', type=int, default=1)
parser.add_argument('--max_steps', type=int, default=60)
parser.add_argument('--learning_rate', type=float, default=0.01)
parser.add_argument('--momentum', type=float, default=0.9)


def main():
    args = parser.parse_args()
    run = wandb.init(entity='shawn', project='launch-test')
    run.config.update(args)
    print('config', run.config)
    for i in range(args.max_steps):
        wandb.log({'a': i * i * args.learning_rate * random.random(), 'b': i * args.momentum * random.random()})


if __name__ == '__main__':
    main()
    # main()
    # main()
