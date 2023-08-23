import pandas as pd
crm = pd.read_csv('crm.csv')
events = pd.read_csv('events.csv')
crm.info()
events.info()
df = events.merge(crm, left_on=['agent_id', 'date_utc'], right_on=['agent_id', 'date_utc'], how='inner')
df = df[['agent_id', 'date_utc', 'punch_in', 'punch_out', 'user_shift_assign', 'timezone_string', 'time_zone']]
df.to_csv('agent_schedule.csv')
