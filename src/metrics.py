from ruptures.metrics import hausdorff
from ruptures.metrics import precision_recall
from ruptures.metrics import randindex
from get_data import generate_signal,read_params
from detection import detection
import argparse
import json



def evaluation_metrices(config_path):
    config = read_params(config_path)
    signal,bkps1 = generate_signal(config_path)
    bkps2 = detection(config_path)
    eval_metrics = hausdorff(bkps1,bkps2)
    rand_index = randindex(bkps1,bkps2)
    print(f'housdorff is {eval_metrics}')
    print(f'rand_index is{rand_index}')
    p,r = precision_recall(bkps1, bkps2)
    print(f'precision is {p} and recall is {r}')

    metrics_file = config["reports"]["metrics"]

    with open(metrics_file,'w') as f:
        metrics = {
            "precision":p,
            "recall" : r,
            "housdorff": eval_metrics,
            "randinex": rand_index
         }
        json.dump(metrics,f,indent= 4)

    return eval_metrics

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    evaluation_metrices(config_path = parsed_args.config)
