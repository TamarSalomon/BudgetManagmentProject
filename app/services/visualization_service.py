import matplotlib.pyplot as plt
import pandas as pd
from app.database  import database_functions
async def get_dataframes():
    try:
        users = await database_functions.get_all("users")
        expenses = await database_functions.get_all("expenses")
        revenues = await database_functions.get_all("revenues")

        if not all(isinstance(item, dict) for item in users):
            raise ValueError("Invalid data format for users")
        if not all(isinstance(item, dict) for item in expenses):
            raise ValueError("Invalid data format for expenses")
        if not all(isinstance(item, dict) for item in revenues):
            raise ValueError("Invalid data format for revenues")

        users_df = pd.DataFrame(users)
        expenses_df = pd.DataFrame(expenses)
        revenues_df = pd.DataFrame(revenues)

        expenses_df['total_expense'] = expenses_df['total_expense'].fillna(0)
        revenues_df['total_revenue'] = revenues_df['total_revenue'].fillna(0)

        return users_df, expenses_df, revenues_df
    except Exception as e:
        print(f"Error in get_dataframes: {e}")
        raise e


async def plot_revenue_expense_per_user():
    try:
        users_df, expenses_df, revenues_df = await get_dataframes()

        expenses_sum = expenses_df.groupby('user_id')['total_expense'].sum().reset_index()
        revenues_sum = revenues_df.groupby('user_id')['total_revenue'].sum().reset_index()

        df = pd.merge(users_df, expenses_sum, left_on='id', right_on='user_id', how='left')
        df = pd.merge(df, revenues_sum, left_on='id', right_on='user_id', how='left')

        df['total_expense'] = df['total_expense'].fillna(0)
        df['total_revenue'] = df['total_revenue'].fillna(0)

        plt.figure(figsize=(12, 6))

        bar_width = 0.35
        index = df.index

        plt.bar(index, df['total_revenue'], bar_width, label='Total Revenue', color='b')
        plt.bar(index + bar_width, df['total_expense'], bar_width, label='Total Expense', color='r')

        plt.xlabel('User')
        plt.ylabel('Amount')
        plt.title('Revenue and Expenses per User')
        plt.xticks(index + bar_width / 2, df['name'])

        plt.legend()
        plt.grid(True)

        plt.show()
    except Exception as e:
        print(f"Error in plot_revenue_expense_per_user: {e}")
        raise e



async def plot_revenue_expense_over_time():
    try:
        users_df, expenses_df, revenues_df = await get_dataframes()

        df = pd.merge(expenses_df, revenues_df, on='date', how='outer')

        plt.figure(figsize=(14, 7))

        plt.plot(df['date'], df['total_expense'], label='Total Expense', color='r')
        plt.plot(df['date'], df['total_revenue'], label='Total Revenue', color='b')

        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Revenue and Expense Over Time')

        plt.legend()
        plt.grid(True)

        plt.show()
    except Exception as e:
        print(f"Error in plot_revenue_expense_over_time: {e}")
        raise e








async def plot_financial_management_per_user():
    try:
        users_df, expenses_df, revenues_df = await get_dataframes()

        expenses_sum = expenses_df.groupby('user_id')['total_expense'].sum().reset_index()
        revenues_sum = revenues_df.groupby('user_id')['total_revenue'].sum().reset_index()

        df = pd.merge(users_df, expenses_sum, left_on='id', right_on='user_id', how='left')
        df = pd.merge(df, revenues_sum, left_on='id', right_on='user_id', how='left')

        df['total_expense'] = df['total_expense'].fillna(0)
        df['total_revenue'] = df['total_revenue'].fillna(0)
        df['financial_management'] = df['total_revenue'] - df['total_expense']

        plt.figure(figsize=(14, 7))

        bar_width = 0.3
        index = df.index

        plt.bar(index, df['total_revenue'], bar_width, label='Total Revenue', color='b')
        plt.bar(index + bar_width, df['total_expense'], bar_width, label='Total Expense', color='r')
        plt.bar(index + 2 * bar_width, df['financial_management'], bar_width, label='Financial Management', color='g')

        plt.xlabel('User')
        plt.ylabel('Amount')
        plt.title('Financial Management per User')
        plt.xticks(index + bar_width, df['name'], rotation=45)

        plt.legend()
        plt.grid(True)

        plt.show()
    except Exception as e:
        print(f"Error in plot_financial_management_per_user")
