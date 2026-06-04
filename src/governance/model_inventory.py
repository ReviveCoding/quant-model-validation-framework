import pandas as pd


def inventory_from_config(cfg):
    return pd.DataFrame(cfg['models'])
