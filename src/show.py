import matplotlib.pyplot as plt
import ruptures as rpt 
import argparse
from detection import   detection
from get_data import generate_signal,read_params

def show(config_path):
    config =read_params(config_path)
    result = detection(config_path)
    signal,bkps = generate_signal(config_path)
    print(f'break points in signal {bkps}')
    rpt.display(signal,bkps,result)
    plt.show()


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    show(config_path = parsed_args.config)  