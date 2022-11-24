# detection of change points 
# save it in results
import os
import argparse
from get_data import generate_signal
import ruptures as rpt


def detection():
    signal,bkps = generate_signal()
    algo = rpt.Dynp(model = 'l2').fit(signal)
    result = algo.predict(n_bkps=4)
    ##print(result)
    return result

    

   

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    detection()