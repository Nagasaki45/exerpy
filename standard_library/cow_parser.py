'''
Reads http://opengeocode.org/download/cow.php and print an easier
to use version.
'''

import pandas as pd

url = 'http://opengeocode.org/cude/download.php?file=' + \
      '/home/fashions/public_html/opengeocode.org/download/cow.txt'
filename = 'cow.csv'


def main():
    data = pd.read_csv(url, sep=';', skiprows=28, comment='#',
                       na_values=['0', '-1'], skipinitialspace=True)
    relevant_columns = [('ISO3166A2', 'short_name'),
                        ('ISOen_name', 'name'),
                        ('UNGEGNen_longname', 'long_name'),
                        ('BGN_capital', 'capital'),
                        ('latitude', 'lat'),
                        ('longitude', 'lon'),
                        ('continent', 'continent'),
                        ('population', 'population'),
                        ('land_total', 'land')]
    data = data[[item[0] for item in relevant_columns]]
    data.columns = [item[1] for item in relevant_columns]
    data.to_csv(filename, index=False)

if __name__ == '__main__':
    main()
