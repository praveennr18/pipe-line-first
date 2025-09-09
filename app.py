# def add(a, b):
#     return a + b

def add(a, b):
    return a + b + 1  # ❌ intentionally wrong

if __name__ == "__main__":   # 👈 fixed typo (_name_ → __name__)
    print(add(1, 2))
