import pandas as pd

def transform_weather(data):

    current = data["current"]

    df = pd.DataFrame([{
        "timestamp": current["time"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"]
    }])

    return df