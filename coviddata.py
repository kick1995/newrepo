import pandas as pd
import json
import requests

state_req = requests.get('https://api.covid19india.org/data.json')
state = json.loads(state_req.content)
district_req = requests.get('https://api.covid19india.org/state_district_wise.json')
district = json.loads(district_req.content)

df1 = pd.DataFrame(state['statewise'])
df1 = df1.set_index('state')
df2 = pd.DataFrame(district)
df2 = df2.T


# df2.loc['Andhra Pradesh']['districtData']
def state(msg):
    st = df1.index
    msg = msg.casefold()
    if ' ' not in msg:
        msg = msg.capitalize()
    elif ' ' in msg:
        d = msg.split(' ')
        d[0] = d[0].capitalize()
        d[1] = d[1].capitalize()
        msg = d[0] + ' ' + d[1]

    if msg in st:
        dp1 = (int(df1.loc[msg]['deaths']) / int(df1.loc[msg]['confirmed'])) * 100
        dp1 = round(dp1, 2)
        rp1 = (int(df1.loc[msg]['recovered']) / int(df1.loc[msg]['confirmed'])) * 100
        rp1 = round(rp1, 2)
        # calling api data
        state_daily_deaths2 = requests.get('https://api.covid19india.org/states_daily.json')
        states_daily_deaths1 = json.loads(state_daily_deaths2.content)
        # cconverting it into dataframe using pandas
        states_daily_deaths = pd.DataFrame(states_daily_deaths1)
        # to fetch last 3 values of the data frame
        ct = states_daily_deaths.index[-3]
        rt = states_daily_deaths.index[-2]
        dt = states_daily_deaths.index[-1]

        tip_confirm = pd.DataFrame(states_daily_deaths.loc[ct]['states_daily'], index=[1])
        tip_confirm = tip_confirm.T
        tip_recover = pd.DataFrame(states_daily_deaths.loc[rt]['states_daily'], index=[1])
        tip_recover = tip_recover.T
        tip_dead = pd.DataFrame(states_daily_deaths.loc[dt]['states_daily'], index=[1])
        tip_dead = tip_dead.T

        sc = df1.loc[msg]['statecode'].lower()
        confirm_today = tip_confirm.loc[sc][1]
        recover_today = tip_recover.loc[sc][1]
        dead_today = tip_dead.loc[sc][1]
        a = 'Active: ' + df1.loc[msg]['active']
        c = 'Confirmed: ' + df1.loc[msg]['confirmed']
        d = 'Deaths: ' + df1.loc[msg]['deaths']
        r = 'Recovered: ' + df1.loc[msg]['recovered']
        dp = 'Death Percentage: ' + str(dp1) + '%'
        rp = 'Recovery Percentage: ' + str(rp1) + '%'
        l1 = 'Stats in the last and latest update are as follows:'
        l2 = 'Confirmed: ' + confirm_today
        l3 = 'Recovered: ' + recover_today
        l4 = 'Deaths: ' + dead_today


    else:
        for i in range(1, len(st)):
            df3 = pd.DataFrame(df2.loc[st[i]]['districtData'])
            df3 = df3.T
            if msg in df3.index:
                dp1 = ((df3.loc[msg]['deceased']) / (df3.loc[msg]['confirmed'])) * 100
                dp1 = round(dp1, 2)
                rp1 = ((df3.loc[msg]['recovered']) / (df3.loc[msg]['confirmed'])) * 100
                rp1 = round(rp1, 2)
                a = 'Active: ' + str(df3.loc[msg]['active'])
                c = 'Confirmed: ' + str(df3.loc[msg]['confirmed'])
                d = 'Deaths: ' + str(df3.loc[msg]['deceased'])
                r = 'Recovered: ' + str(df3.loc[msg]['recovered'])
                dp = 'Death Percentage: ' + str(dp1) + '%'
                rp = 'Recovery Percentage: ' + str(rp1) + '%'
                l1 = 'no data found'
                l2 = 'no data found'
                l3 = 'no data found'
                l4 = 'no data found'
                break
            else:
                a = 'not found'
                c = 'not found'
                d = 'not found'
                r = 'not found'
                dp = 'not found'
                rp = 'not found'
                l1 = 'no data found'
                l2 = 'no data found'
                l3 = 'no data found'
                l4 = 'no data found'
    return a, c, d, r, dp, rp,l1,l2,l3,l4