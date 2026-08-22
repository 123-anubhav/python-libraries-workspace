import pandas as pd
import os


house_data = {
    "area": [
        1000, 1200, 1500, 1800, 2000,
        2200, 2500, 2800, 3000, 3500
    ],

    "bedrooms": [
        2, 2, 3, 3, 4,
        4, 4, 5, 5, 5
    ],

    "bathrooms": [
        2, 2, 2, 3, 3,
        3, 4, 4, 4, 5
    ],

    "age": [
        10, 8, 7, 5, 6,
        4, 3, 2, 1, 1
    ],

    "price": [
        5000000, 6000000, 7500000, 9000000, 10000000,
        11000000, 13000000, 15000000, 17000000, 20000000
    ]
}


df = pd.DataFrame(house_data)


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CSV_FILE = os.path.join(
    BASE_DIR,
    "houses.csv"
)


df.to_csv(
    CSV_FILE,
    index=False
)


def csv_data():

    df = pd.read_csv(CSV_FILE)

    return df