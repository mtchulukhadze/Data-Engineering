
def save_csv(df):

    df.to_csv(
        "D:\Data\Data Engineering\weather.csv",
        index=False
    )