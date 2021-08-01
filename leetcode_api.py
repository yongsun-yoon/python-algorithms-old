import os
import requests
import pandas as pd
from datetime import datetime

def fetch():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'leetcode.csv')
    if not os.path.isfile(filepath) or datetime.weekday == 0:
        req = requests.get('https://leetcode.com/api/problems/algorithms/')
        data = req.json()
        data = data['stat_status_pairs']
        data = pd.json_normalize(data, sep='_')
        data.to_csv(filepath, index=False, encoding='utf-8')
        print('finish downloading data')
    else:
        data = pd.read_csv(filepath)
        print('loading')
    return data

def sample_data(data):
    sample = data.query("difficulty_level == 1").sample(1).iloc[0]
    return sample

def main():
    data = fetch()
    sample = sample_data(data)
    print(f"""Today's Code
name: {sample['stat_question__title']}
url: https://leetcode.com/problems/{sample['stat_question__title_slug']}/
    """)
    

if __name__ == '__main__':
    main()