import os
import random
import argparse
import numpy as np
import pandas as pd

from utils import make_dirs, load_data, standardization, SequenceDataset
import torch
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader



def main(args):

    # Fix Seed #
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed(args.seed)

    # Weights and Plots Path #
    paths = [args.weights_path, args.plots_path, args.numpy_path]
    for path in paths:
        make_dirs(path)

    # Prepare Data #
    data = load_data(args.which_data)[args.feature]
    
    

    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--which_data', type=str, default='./data/data.xlsx', help='which data to use')
    parser.add_argument('--seed', type=int, default=7777, help='seed for reproducibility')
    parser.add_argument('--feature', type=str, default=['value', 'lag24', 'lag48'], help='extract which feature')
    parser.add_argument('--weights_path', type=str, default='./results/weights/', help='weights path')
    parser.add_argument('--plots_path', type=str, default='./results/plots/', help='plots path')
    parser.add_argument('--numpy_path', type=str, default='./results/numpy/', help='numpy path')
    parser.add_argument('--plot_full', type=bool, default=False, help='plot full graph or not')
    parser.add_argument('--output_size', type=int, default=1, help='output_size')
    
    parser.add_argument('--seq_length', type=int, default=5, help='window size')
    parser.add_argument('--batch_size', type=int, default=64, help='mini-batch size')
    
    config = parser.parse_args()

    torch.cuda.empty_cache()
    main(config)
