import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.preprocessing import OneHotEncoder
import numpy as np

def data_split_generator(data):
    train_start_date = pd.to_datetime('1749-01-31')
    train_end_date = pd.to_datetime('1963-12-31')
    vali_end_date = pd.to_datetime('1973-12-31')
    # test_end_date = pd.to_datetime('1983-12-31')
    for i in range(5):
        # print(train_start_date, train_end_date, vali_end_date, test_end_date)
        train_start_date = train_end_date + pd.DateOffset(years=-30) + pd.offsets.MonthEnd(0)
        train_data = data[(data.target_dates >= train_start_date) & (data.target_dates <= train_end_date)]
        vali_data = data[(data.target_dates > train_end_date) & (data.target_dates <= vali_end_date)]
        yield train_data, vali_data
        train_end_date = train_end_date + pd.DateOffset(years=-10) + pd.offsets.MonthEnd(0)
        vali_end_date = vali_end_date + pd.DateOffset(years=-10) + pd.offsets.MonthEnd(0)

def get_metric(y_true, y_predict):
    RMSE = np.sqrt(mean_squared_error(y_true, y_predict))
    # MAE = mean_absolute_error(y_true, y_predict)
    # MAPE = mean_absolute_percentage_error(y_true, y_predict)
    return RMSE

def make_x_y(data: pd.DataFrame, month_encoder:OneHotEncoder = None):
    data = data.copy(deep=True)
    data.reset_index(drop=True, inplace=True)
    data.drop(columns=['dates', 'target_dates'], inplace=True)
    if month_encoder is None:
        month_encoder = OneHotEncoder()
        month_encoder.fit(data[['month']])
    month = month_encoder.transform(data[['month']]).toarray()
    month = pd.DataFrame(month, columns=[str(x) for x in month_encoder.categories_[0].tolist()])
    data:pd.DataFrame = pd.concat([data, month], axis = 1)
    Y = data.pop('target_sunspots')
    return data , Y, month_encoder
