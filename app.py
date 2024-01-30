# app.py
import numpy as np

def main():
    a = np.array([1, 2, 3, 4, 5,15,-2,0])
    print("Original array:", a)
    squared_array = np.square(a)
    print("Squared array:", squared_array)

if __name__ == "__main__":
    main()

