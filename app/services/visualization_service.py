import matplotlib.pyplot as plt
import pandas as pd
from app.database  import database_functions
async def get_dataframes():
    users = await database_functions.get_all("users")
    expenses = await database_functions.get_all("expenses")
    revenues = await database_functions.get_all("revenues")

    users_df = pd.DataFrame(users)
    expenses_df = pd.DataFrame(expenses)
    revenues_df = pd.DataFrame(revenues)

    expenses_sum = expenses_df.groupby('user_id')['total_expense'].sum().reset_index()
    revenues_sum = revenues_df.groupby('user_id')['total_revenue'].sum().reset_index()

    df = pd.merge(users_df, expenses_sum, left_on='id', right_on='user_id', how='left')
    df = pd.merge(df, revenues_sum, left_on='id', right_on='user_id', how='left')

    df['total_expense'].fillna(0, inplace=True)
    df['total_revenue'].fillna(0, inplace=True)
    df['net_income'] = df['total_revenue'] - df['total_expense']

    return df

async def plot_income_expense_per_user():
    try:
        df = await get_dataframes()
        plt.figure(figsize=(12, 6))
        bar_width = 0.35
        index = df.index
        plt.bar(index, df['total_revenue'], bar_width, label='Income', color='b')
        plt.bar(index + bar_width, df['total_expense'], bar_width, label='Expenses', color='r')
        plt.xlabel('User')
        plt.ylabel('Amount')
        plt.title('Income and Expenses per User')
        plt.xticks(index + bar_width / 2, df['name'])
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        raise e

async def plot_revenue_distribution():
    try:
        df = await get_dataframes()
        plt.figure(figsize=(8, 8))
        plt.pie(df['total_revenue'], labels=df['name'], autopct='%1.1f%%', startangle=140)
        plt.title('Total Revenue Distribution')
        plt.show()
    except Exception as e:
        raise e

async def plot_net_income_over_time():
    try:
        df = await get_dataframes()
        expenses_df = pd.DataFrame(await database_functions.get_all("expenses"))
        revenues_df = pd.DataFrame(await database_functions.get_all("revenues"))
        plt.figure(figsize=(12, 6))
        for user_id in df['id']:
            user_expenses = expenses_df[expenses_df['user_id'] == user_id].set_index('date')['total_expense']
            user_revenues = revenues_df[revenues_df['user_id'] == user_id].set_index('date')['total_revenue']
            user_net_income = user_revenues - user_expenses
            user_net_income.fillna(0, inplace=True)
            user_name = df[df['id'] == user_id]['name'].values[0]
            plt.plot(user_net_income.index, user_net_income, label=user_name)
        plt.xlabel('Date')
        plt.ylabel('Net Income')
        plt.title('Net Income Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        raise e

async def plot_combined_income_expense_net_income():
    try:
        df = await get_dataframes()
        plt.figure(figsize=(12, 6))
        index = df.index
        bar_width = 0.25
        plt.bar(index, df['total_revenue'], bar_width, label='Income', color='b')
        plt.bar(index + bar_width, df['total_expense'], bar_width, label='Expenses', color='r')
        plt.plot(index + bar_width / 2, df['net_income'], label='Net Income', color='g', marker='o')
        plt.xlabel('User')
        plt.ylabel('Amount')
        plt.title('Income, Expenses, and Net Income per User')
        plt.xticks(index + bar_width / 2, df['name'])
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        raise e