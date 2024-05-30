# Expense and Revenue Management System

Welcome to our Expense and Revenue Management System! This project is designed to help users efficiently manage their expenses and revenues in an organized manner. Users can register, log in, update their details, and perform various operations related to their financial activities.

## Key Components and Technologies

- **Database:** MongoDB is used for data management.
- **Server-side:** Developed using Python.
- **Visualizations:** Data is visualized using Matplotlib.

## Features

1. **User Management:**
   - **Registration:** New users can sign up for an account.
   - **Login:** Registered users can log in.
   - **Update User:** Users can update their profile information.
   - **Deletion:** Users can delete their account if desired.

2. **Expense and Revenue Management:**
   - **Addition:** Users can add new expenses or revenues.
   - **Retrieval:** View existing expenses and revenues.
   - **Deletion:** Remove unwanted expenses or revenues.
   - **Update:** Modify details of existing expenses or revenues.

3. **Visualization:**
   - Visualize expense and revenue data for better analysis and insights.

## Routing

### For Users:
  - **Login:** `/login`
  - **Register:** `/register`
  - **Update User:** `/update_user`
  - **Delete User:** `/delete_user`
  - **Retrieve:** `/user/retrieve`

### For Expenses:
  - **Add:** `/expenses/add`
  - **Retrieve:** `/expenses/retrieve`
  - **Delete:** `/expenses/delete`
  - **Update:** `/expenses/update`

### For Revenues:
  - **Add:** `/revenues/add`
  - **Retrieve:** `/revenues/retrieve`
  - **Delete:** `/revenues/delete`
  - **Update:** `/revenues/update`

## Testing and Quality Assurance

- Thorough testing of input data validation.
- Quality checks on system functionalities.

## Documentation

Comprehensive documentation is provided for all system functionalities.

## Logging Decorator
decorator that performs logging operations within the system. The decorator captures logs of function executions and saves them to a specified file.

## Installation and Usage

To get started with BudgetManagment:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/TamarSalomon/BudgetManagmentProject.git

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt


3. **Run the application:**
   ```sh
   python main.py

## The project file tree:
![image](https://github.com/TamarSalomon/BudgetManagmentProject/assets/152272661/bade5f23-c0c4-40ef-957e-72ae2a9841b4)





### Support and Contributions
  If you encounter any issues or wish to contribute to the development of the project, please open an issue in our repository.

  Thank you for using our Expense and Revenue Management System! We hope it helps you manage your finances effectively. Feel free to reach out for any assistance or feedback.

  Happy budgeting!


