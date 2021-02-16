import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

# class for data_generation


def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20, 260)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()
    max_speed = 260
    min_speed = 0

    return [surr_id, speed, date, time, max_speed, min_speed]


if __name__ == '__main__':
    REST_API_URL = 'https://api.powerbi.com/beta/dc83dd11-0b98-4487-922c-ed8f0379c336/datasets/25893a22-cf77-4072-a94a-9d0a82b197d8/rows?key=zERrCDh%2F92ehQSkEJ1KEX0I4yausgc6Iq%2FgGfmc5nNd6eZDh5zwJrT1klbGqjeLoKPnGkaiZtwku%2Bq%2F4wrY0VA%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            # print(row[2])
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["surr_id", "speed", "date", "time", 'max_speed', 'min_speed']

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        r = requests.post(REST_API_URL, data_json)
        pastebin_url = r.status_code
        print("response status:", pastebin_url)

        print("Data posted in Power BI API")
        time.sleep(2)
