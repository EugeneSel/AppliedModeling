import requests
import pandas as pd


URL_TOTAL = 'http://api.coronatracker.com/v3/analytics/trend/country'
URL_DAILY_CASES = 'http://api.coronatracker.com/v3/analytics/newcases/country'

PARAMS = {
    'countryCode': 'UA',
    'startDate': '2020-05-01',
    'endDate': '2020-11-01'
}


def load_data():
    r_total = requests.get(url=URL_TOTAL, params=PARAMS) 
    if r_total.ok:
        data_total = r_total.json()

        df_total = pd.DataFrame(data_total)
        df_total.to_csv("data/total_cases.csv")
    else:
        print(r_total.reason)
        df_total = None

    r_daily_cases = requests.get(url=URL_DAILY_CASES, params=PARAMS) 
    if r_daily_cases.ok:
        data_daily_cases = r_daily_cases.json()

        df_daily_cases = pd.DataFrame(data_daily_cases)
        df_daily_cases.to_csv("data/daily_cases.csv")
    else:
        print(r_daily_cases.reason)
        df_daily_cases = None

    return df_total, df_daily_cases


if __name__ == '__main__':
    from IPython.display import display


    df_total, df_daily_cases = load_data()
    
    if df_total is not None:
        display(df_total.head())
    if df_daily_cases is not None:
        display(df_daily_cases.head())
