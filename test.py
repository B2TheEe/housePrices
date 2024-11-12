import pandas as pd

def main():
   cols =  ["price", "bedrooms", "living_in_m2", "renovated"]
   df_minimize = read(cols)
   print(df_minimize)


def read(cols):
    df = pd.read_csv('data/df_test.csv', usecols=cols)
    return df


if __name__ == "__main__":
    main()