# detection of change points 
# save it in results
import os
import argparse
from get_data import generate_signal,read_params
import ruptures as rpt
import json


def detection(config_path):
    config = read_params(config_path)
    signal,bkps = generate_signal(config_path)
    model1 = config['detection']['model']
    algo = rpt.Dynp(model = model1).fit(signal)
    result = algo.predict(n_bkps=4)
    print(f'detected break points are {result}')

    breakpoints_file = config["reports"]["breakpoints"]

    with open(breakpoints_file,'w') as f:
        breakpoints = {
            "breakpoint":result
        }
        json.dump(breakpoints,f,indent= 4)

    return result

    

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    detection(config_path = parsed_args.config)