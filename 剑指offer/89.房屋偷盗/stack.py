

def sum(value):
    if value > 30:
        return value
    else:
        value1 = value + 2
        return sum(value1)

if __name__ == "__main__":
    value = 10
    
    print(sum(value))
