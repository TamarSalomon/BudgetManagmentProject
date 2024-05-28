import matplotlib.pyplot as plt
import pandas as pd
from app.database import database_functions
import datetime

async def filter_by_current_month(data_df):
    """
    Filters the given dataframe to include only the rows from the current month.

    Args:
        data_df (pd.DataFrame): The dataframe to be filtered.

    Returns:
        pd.DataFrame: A dataframe containing only the rows from the current month.
    """
    current_month = datetime.datetime.now().month
    return data_df[data_df['date'].dt.month == current_month]

async def get_dataframes():
    """
    Retrieves all users, expenses, and revenues data from the database and returns them as dataframes.

    Returns:
        tuple: A tuple containing three dataframes: users, expenses, and revenues.
    """
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

async def plot_revenue_expense_per_user(user_id):
    """
    Plots a bar chart showing the total revenue and total expense for a specific user in the current month.

    Args:
        user_id (int): The ID of the user.

    Raises:
        ValueError: If the user with the specified ID is not found.

    Returns:
            None: Displays a bar chart showing total revenue and expense for the specified user.

    """
    try:
        users_df, expenses_df, revenues_df = await get_dataframes()

        expenses_sum = expenses_df.groupby('user_id')['total_expense'].sum().reset_index()
        revenues_sum = revenues_df.groupby('user_id')['total_revenue'].sum().reset_index()

        df = pd.merge(users_df, expenses_sum, left_on='id', right_on='user_id', how='left')
        df = pd.merge(df, revenues_sum, left_on='id', right_on='user_id', how='left')

        df['total_expense'] = df['total_expense'].fillna(0)
        df['total_revenue'] = df['total_revenue'].fillna(0)

        user_df = df[df['id'] == user_id]

        if user_df.empty:
            raise ValueError(f"User with id {user_id} not found")

        plt.figure(figsize=(12, 6))

        bar_width = 0.35
        index = user_df.index

        plt.bar(index, user_df['total_revenue'], bar_width, label='Total Revenue', color='green')
        plt.bar(index + bar_width, user_df['total_expense'], bar_width, label='Total Expense', color='yellow')

        plt.xlabel('User')
        plt.ylabel('Amount')
        plt.title(f'Revenue and Expenses for User {user_id}')
        plt.xticks(index + bar_width / 2, user_df['name'])

        plt.legend()
        plt.grid(True)

        plt.show()
    except Exception as e:
        print(f"Error in plot_revenue_expense_per_user: {e}")
        raise e

async def plot_pie_chart(user_id):
    """
    Plots a pie chart showing the distribution of expenses and revenues for a specific user in the current month.

    Args:
        user_id (int): The ID of the user.

    Returns:
            None: Displays a pie chart showing the distribution of expenses and revenues for the specified user in the current month.

    """
    try:
        users_df, expenses_df, revenues_df = await get_dataframes()

        expenses_df = await filter_by_current_month(expenses_df)
        revenues_df = await filter_by_current_month(revenues_df)

        user_expenses = expenses_df[expenses_df['user_id'] == user_id]
        user_revenues = revenues_df[revenues_df['user_id'] == user_id]

        total_expenses = user_expenses['total_expense'].sum()
        total_revenues = user_revenues['total_revenue'].sum()

        labels = ['Expenses', 'Revenues']
        sizes = [total_expenses, total_revenues]
        colors = ['red', 'green']
        explode = (0.1, 0)  # explode Expenses slice

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.title(f'Expense and Revenue Distribution for User {user_id}')

        plt.show()
    except Exception as e:
        print(f"Error in plot_pie_chart: {e}")
        raise e

async def plot_revenue_expense_over_time(user_id):
    """
    Plots a line chart showing the total revenue and total expense over time for a specific user.

    Args:
        user_id (int): The ID of the user.

    Returns:
            None: Displays a line chart showing total revenue and expense over time for the specified user.

    """
    try:
        users_df, expenses_df, revenues_df = await get_dataframes()

        user_expenses = expenses_df[expenses_df['user_id'] == user_id]
        user_revenues = revenues_df[revenues_df['user_id'] == user_id]

        plt.figure(figsize=(14, 7))

        plt.plot(user_expenses['date'], user_expenses['total_expense'], label='Total Expense', color='red')
        plt.plot(user_revenues['date'], user_revenues['total_revenue'], label='Total Revenue', color='blue')

        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title(f'Revenue and Expense Over Time for User {user_id}')

        plt.legend()
        plt.grid(True)

        plt.show()
    except Exception as e:
        print(f"Error in plot_revenue_expense_over_time: {e}")
        raise e
