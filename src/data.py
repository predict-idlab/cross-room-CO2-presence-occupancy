from pathlib import Path

import pandas as pd

def load_rooms():
    rooms = {}

    if Path('../data/office/200.009.parquet').is_file():
        rooms['Office L1'] = pd.read_parquet('../data/office/200.009.parquet')

    if Path('../data/office/200.010.parquet').is_file():
        rooms['Office L2'] = pd.read_parquet('../data/office/200.010.parquet')

    if Path('../data/office/200.024.parquet').is_file():
        rooms['Office S3'] = pd.read_parquet('../data/office/200.024.parquet')

    if Path('../data/home/r16716412444.parquet').is_file():
        rooms['Home 1'] = pd.read_parquet('../data/home/r16716412444.parquet')

    return rooms


