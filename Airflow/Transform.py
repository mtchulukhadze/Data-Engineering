
def transform_product(products):
    df  = products.copy()

    df = df.rename(columns={
        "id" : "product_id",
        "title": "title",
        "price": "price",
        "description": "desc",
        "category": "category"
    })

    df = df[[
         "title",
         "price",
         "desc",
         "category"
    ]]

    df["price"] = df["price"].astype(float)

    return df

def transform_users(user):
    df = user.copy()

    df = df.rename(columns={
        "address": "address",
        "city": "city",
        "street":"street",
        "number": "number",
        "zipcode": "zipcode"
    })

    df = df[[
          "address",
          "city",
         "street",
         "number",
         "zipcode"
    ]]

    return df