#!/bin/bash

brew install --cask miniforge

mamba init zsh

eval "$(mamba shell hook --shell zsh)"
source ~/.zshrc

mamba create -n tf-gpu python=3.11

mamba activate tf-gpu

python3 -m pip install tensorflow

python3 -m pip install tensorflow-metal

python3 -m pip install pandas 

# To connect to jupyter
# python3 -m pip install jupyter jupyter_http_over_ws tensorflow tensorflow-hub tensorflow-datasets matplotlib
