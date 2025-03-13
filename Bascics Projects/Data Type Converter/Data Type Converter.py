###  Data Type Converter (DataTypes)

def data_type_converter():
    value = input("Enter a value: ")
    print(f"Integer: {int(float(value))}")
    print(f"Float: {float(value)}")
    print(f"String: {str(value)}")

data_type_converter()