import pandas as pd

def main():


    df = pd.read_csv('data/df_test.csv')
    df_minimize = pd.read_csv('data/df_test.csv', usecols=[ "price", "bedrooms", "living_in_m2", "renovated"])
    print(df_minimize)

if __name__ == "__main__":
    main()