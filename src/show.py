import matplotlib.pyplot as plt
import ruptures as rpt 
import argparse
from detection import   detection
from get_data import generate_signal

def show():
    result = detection()
    signal,bkps = generate_signal()
    rpt.display(signal,bkps,result)
    plt.show()


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    show()  