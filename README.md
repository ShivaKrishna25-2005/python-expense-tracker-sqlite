# python-expense-tracker-sqlite
A Python-based command-line Personal Expense Tracker using SQLite with full CRUD functionality.


🧾 Personal Expense Tracker (Python + SQLite)
📌 Project Overview

The Personal Expense Tracker is a command-line application developed using Python and SQLite.
It allows users to manage daily expenses efficiently by storing, retrieving, filtering, and deleting financial records from a local database.

This project demonstrates practical implementation of:
Object-Oriented Programming (OOP)
SQLite Database Integration
CRUD Operations
Exception Handling
Menu-Driven CLI Application

🚀 Features
➕ Add a new expense
📋 View all expenses
💰 View total amount spent
🔎 Filter expenses by category
❌ Delete an expense by ID
🔐 Secure parameterized SQL queries

🛠️ Technologies Used
Python 3.x
SQLite3 (Built-in Python module)
SQL (Structured Query Language)

🗄️ Database Schema
Column	Type	Description
id	INTEGER	Primary Key (Auto Increment)
amount	REAL	Expense amount
category	TEXT	Expense category
date	TEXT	Date (YYYY-MM-DD)
