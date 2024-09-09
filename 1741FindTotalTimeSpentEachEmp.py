import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    # print(employees.index)
    # employees.rename({'event_day':'day'}, axis = 1, inplace = True)
    employees.rename(columns={'event_day': 'day'})
    return employees
