# Cafe Application
Cafe Management is a desktop Python application that helps manage a cafe.
The app includes face recognition for customer authentication using OpenCV.
It consists of three layers:<br>
- Graphics User Interface (GUI): a presentation layer that uses Tkinter for the user interface.
- Business Logic Layer (BLL): a business layer that handles the application logic.
- Data Access Layer (DAL): a data access layer that connects to a MySQL database.

___

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [External Dependencies](#external-dependencies)
- [License](#license)

___

## Features
The Cafe Management application includes the following features:
- Customer authentication using face recognition.
- Manage items which a real cafe has (e.g. products, staffs, customers, ingredients...).
- Create, manage and export bills (selling products) and receipt (importing ingredients) to Excel.
- Generate reports on sales, inventory and other metrics.

___

## Installation
To install the Cafe Management application, follow these steps:
- Clone the repository to your local machine (VSCode is recommended).
- Open a terminal at the project folder and type this: `python ./setup.py` to create a virtual environment (venv)
- Activate the venv: `./venv/Scripts/activate`
- Install the required dependencies: `pip install -r requirements.txt`
- Create a MySQL database named `cafe_management` and run this [`SQL`](cafe_application/database/cafe_db.sql) file.
- Configure this [`MySQL`](cafe_application/src/DAL/MySQL.py) class to connect to your MySQL database.
- Build the project and run this [`CafeManagement`](cafe_application/src/main/CafeApplication.py) class.

___

## Usage
- Log in with the default account: `username = 'admin'`, `password = 'admin'`
- Use the GUI to manage items, bills, and receipts.
- Click the "DETECTION" button to use face recognition for customer authentication.

___

## Contributors
The following contributors have contributed to the Cafe Management:

| **ID**       | **Name**                                              |
|--------------|-------------------------------------------------------|
| `3121410116` | [`Đinh Quang Duy   `](https://github.com/quangduy201) |
| `3121410296` | [`Nguyễn Hoàng Long`](https://github.com/LongBOTT)    |
| `3121410138` | [`Nguyễn Zi Đan    `](https://github.com/zidan63)     |

___

## External Dependencies
Look up this file [`requirement.txt`](requirements.txt) to see the dependencies

___

## License
This project is licensed under the [`MIT License`](https://opensource.org/licenses/MIT).
See the [`LICENSE`](LICENSE) file for more information.

___

_This file was created on April 20, 2023, v1.0_
