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


   
BudgetManagment
├── APP
│   ├── database
│   │   ├── database_connection.py
│   │   └── database_functions.py
│   ├── models
│   │   ├── expense_model.py
│   │   ├── revenue_model.py
│   │   └── user_model.py
│   ├── routes
│   │   ├── expenses_router.py
│   │   ├── revenues_router.py
│   │   └── users_router.py
│   ├── services
│   │   ├── expenses_service.py
│   │   ├── revenues_service.py
│   │   ├── users_service.py
│   │   └── visualization_service.py
│   ├── tests
│   │   ├── expenses_router_tests.py
│   │   ├── revenues_router_tests.py
│   │   └── users_router_tests.py
│   ├── validition
│   │   └── validition_functions.py
│   ├── main.py
│   └── utils.py
├── README.md
└── requirements.txt



### Support and Contributions
  If you encounter any issues or wish to contribute to the development of the project, please open an issue in our repository.

  Thank you for using our Expense and Revenue Management System! We hope it helps you manage your finances effectively. Feel free to reach out for any assistance or feedback.

  Happy budgeting! 📊💰



