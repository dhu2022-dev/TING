import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from opendatasets import download

def get_dataset():
    download('https://www.kaggle.com/datasets/viveksharmar/flight-price-data')
    df = pd.read_csv('flight-price-data/flight_price_data.csv')
    return df

