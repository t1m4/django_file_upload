import pickle

import numpy as np
import pandas as pd


def pred_attack(path_csv, path_weight="templates/XGBoost_NSLKDD.pkl"):
    model = pickle.load(open(path_weight, "rb"))
    data = pd.read_csv(path_csv)
    pred = model.predict(data).astype(str)
    return np.where(pred == '1', 'attack', 'norm').tolist()


def save_uploaded_file(user_file, filename: str = "test_data.csv"):
    with open('static/' + filename, 'wb+') as f:
        for chunk in user_file.chunks():
            f.write(chunk)
