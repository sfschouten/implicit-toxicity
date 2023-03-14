import os
import uuid

import duckdb
import pandas as pd
from dotenv import load_dotenv

from toxic_impl.data import load_toxic_span_datasets

load_dotenv()

PROJECT_HOME = os.getenv('TOXIC_IMPL_HOME')
RESULTS_FILE = 'results.duckdb'

def open_db(file_name=RESULTS_FILE):
    file_path = os.path.join(PROJECT_HOME, file_name)
    return duckdb.connect(database=file_path, read_only=False)


def initialize_db(file_name=RESULTS_FILE):
    con = open_db(file_name)

    with open(os.path.join(PROJECT_HOME, 'src/toxic_impl/schema.sql'), 'r') as schema_file:
        query = schema_file.read()
        con.execute(query)

    datasets = load_toxic_span_datasets()

    columns = ','.join(SPAN_DATA_COLUMNS)
    for key, dataset in datasets.items():
        dataset['sample_id'] = dataset['id']
        dataset['dataset_key'] = key
        con.execute(f'INSERT INTO span_data({columns}) SELECT {columns} FROM dataset')

    con.close()


if __name__ == "__main__":
    initialize_db()
