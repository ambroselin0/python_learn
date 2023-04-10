import pandas as pd


def data_split_generator(data):
    train_start_date = pd.to_datetime('1749-01-31')
    train_end_date = pd.to_datetime('1963-12-31')
    vali_end_date = pd.to_datetime('1973-12-31')
    test_end_date = pd.to_datetime('1983-12-31')
    for i in range(5):
        # print(train_start_date, train_end_date, vali_end_date, test_end_date)
        train_data = data[(data.target_dates >= train_start_date) & (data.target_dates <= train_end_date)]
        vali_data = data[(data.target_dates > train_end_date) & (data.target_dates <= vali_end_date)]
        test_data = data[(data.target_dates > vali_end_date) & (data.target_dates <= test_end_date)]
        yield train_data, vali_data, test_data
        # print(train_data.shape, vali_data.shape, test_data.shape)
        train_end_date = train_end_date + pd.DateOffset(years=-10) + pd.offsets.MonthEnd(0)
        vali_end_date = vali_end_date + pd.DateOffset(years=-10) + pd.offsets.MonthEnd(0)
        test_end_date = test_end_date + pd.DateOffset(years=-10) + pd.offsets.MonthEnd(0)
