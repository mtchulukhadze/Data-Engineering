
import pandas as pd
import requests

url = "https://fakestoreapi.com"

def extract_products():
    url2 = f"{url}/products"
    response = requests.get(url2)
    response.raise_for_status()

    data = response.json()

    products = pd.DataFrame(data)
    return products


def extract_user():
    url3 = f"{url}/users"
    response = requests.get(url3)
    response.raise_for_status()

    data = response.json()

    user = pd.DataFrame(data)
    return user