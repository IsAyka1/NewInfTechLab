import pandas as pd


def save(data: dict, file: str):
    df = pd.DataFrame(data)
    df.to_excel(file, index=False)