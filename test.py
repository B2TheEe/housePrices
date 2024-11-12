import pandas as pd

def main():
   location = 'data/df_test.csv'
   cols =  ["price", "bedrooms", "living_in_m2", "renovated"]
   df = read(location,cols)

   #seeing the first and last 5 of datast
   print(df.head())
   print(df.tail())


def read(location,cols):
    df = pd.read_csv(location, usecols=cols)
    return df


if __name__ == "__main__":
    main()