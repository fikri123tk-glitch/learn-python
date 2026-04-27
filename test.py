#unpaking

product = [
    "Laptop",
    "HP",
    "electronics",
    "black",
    "included accessories",
     1200,
    "instock"
]    

produck_name, brand,*_, price, stock_status = product

print(f"{produck_name} {brand} costs ${price} and is currently {stock_status}.")