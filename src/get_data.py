## read params
## process
## return dataframe
import os
import yaml
import ruptures as rpt
import argparse

##def read_params(config_path):
    ##with open(config_path) as yaml_file:
        #config = yaml.safe_load(yaml_file)
    #return config

def generate_signal():
    
    # Generating signal
    n_samples,n_dim,sigma = 1000,3,2
    #number of breakpoints
    n_bkps = 4
    signal,bkps = rpt.pw_constant(n_samples,n_dim,n_bkps,noise_std = sigma)
    print(bkps)
    return signal,bkps



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = generate_signal()
    
    