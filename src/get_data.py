## read params
## process
## return dataframe
import os
import yaml
import ruptures as rpt
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def generate_signal(config_path):
    
    # Generating signal
    config = read_params(config_path)
    n_samples = config["data_source"]['n_samples']
    n_dim = config["data_source"]['n_dim']
    sigma = config["data_source"]['sigma']
    #number of breakpoints
    n_bkps = config["data_source"]["n_bkps"]
    signal,bkps = rpt.pw_constant(n_samples,n_dim,n_bkps,noise_std = sigma)
    #print(f'breakpoints in the signal are {bkps}')
    return signal,bkps



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    generate_signal(config_path = parsed_args.config )
    
    