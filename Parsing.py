import cianparser
import pandas as pd
import time

moscow = cianparser.CianParser(location='Москва')

data = []
for i in range(1, 20):
    a = moscow.get_flats(deal_type='sale', rooms=(3), additional_settings={'start_page': i, 'end_page':i} )
    data.extend(a)
    time.sleep(5)
    
exel_export = pd.DataFrame(data)
columns = ['author', 'author_type', 'location', 'deal_type', 'accommodation_type', 'floors_count', 'rooms_count', 'total_meters', 'price', 'district', 'street', 'house_number', 'underground', 'residential_complex']
selected_columns = exel_export[columns]
selected_columns.to_csv('c:/Users/Mrsoning/OneDrive/Документы/GitHub/Intensive_one/result.csv', mode='a', header=False, index=False)