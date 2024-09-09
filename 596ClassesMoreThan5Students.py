import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    sub = (courses.groupby('class')['student'].count()).reset_index()
    df = sub[sub['student'] >= 5]
    return df[['class']]