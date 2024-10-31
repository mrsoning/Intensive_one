import pandas as pd

base = "c:/Users/Mrsoning/OneDrive/Документы/GitHub/Intensive_one/result.csv"

data = pd.read_csv(base)
data = data.drop_duplicates()
data.to_csv(base, index=False)

zxc = pd.read_csv(base)
zxc = zxc.dropna(subset=['author_type', 'location', 'floors_count', 'rooms_count', 'total_meters', 'price', 'district'])
zxc.to_csv(base, index=False)

zxc = pd.read_csv(base)
zxc = zxc.loc[zxc['author_type'] != 'unknown']

zxc.to_csv(base, index=False)

zxc = pd.read_csv(base)
zxc['underground'].fillna('not available', inplace=True)
zxc.to_csv(base, index=False)

data = pd.read_csv(base)

def metro(row):
    if row['underground'] == 'not available': return False
    return True

def meters(row):
    return round(row['price']/row['total_meters'])

data['availability_underground'] = data.apply(metro, axis=1)
data['price_per_meter'] = data.apply(meters, axis=1)
data.to_csv(base, index=False)


res = "c:/Users/Mrsoning/OneDrive/Документы/GitHub/Intensive_one/result.csv"

zxc = pd.read_csv(base)
total = zxc.drop(['street', 'house_number','residential_complex'], axis=1)
total.info()

total.to_csv( res, index=False, encoding='utf-8-sig')