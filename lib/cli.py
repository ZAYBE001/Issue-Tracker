import argparse
from datetime import datetime
from database import Session, create_tables
from models import User, Issue

def create_user(username, email):
    session = Session()
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    session.close()
    print(f"User '{username}' created successfully.")

def delete_user(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User '{username}' deleted successfully.")
    else:
        print(f"User '{username}' not found.")
    session.close()

def list_users():
    session = Session()
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    session.close()

def create_issue(title, description, priority, status, username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        issue = Issue(title=title, description=description, priority=priority, status=status, user=user)
        session.add(issue)
        session.commit()
        print(f"Issue '{title}' created successfully.")
    else:
        print(f"User '{username}' not found.")
    session.close()

def delete_issue(issue_id):
    session = Session()
    issue = session.query(Issue).filter_by(id=issue_id).first()
    if issue:
        session.delete(issue)
        session.commit()
        print(f"Issue ID {issue_id} deleted successfully.")
    else:
        print(f"Issue ID {issue_id} not found.")
    session.close()

def list_issues():
    session = Session()
    issues = session.query(Issue).all()
    for issue in issues:
        print(f"ID: {issue.id}, Title: {issue.title}, Priority: {issue.priority}, Status: {issue.status}, Created by: {issue.user.username}")
    session.close()

def manage_users():
    while True:
        print("\nManage Users:")
        print("1. Create User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            create_user(username, email)
        elif choice == '2':
            username = input("Enter username to delete: ")
            delete_user(username)
        elif choice == '3':
            list_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_issues():
    while True:
        print("\nManage Issues:")
        print("1. Create Issue")
        print("2. Delete Issue")
        print("3. List Issues")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter issue title: ")
            description = input("Enter issue description: ")
            priority = input("Enter issue priority (Low, Medium, High): ")
            status = input("Enter issue status (Open, In Progress, Resolved): ")
            username = input("Enter username of the creator: ")
            create_issue(title, description, priority, status, username)
        elif choice == '2':
            issue_id = int(input("Enter issue ID to delete: "))
            delete_issue(issue_id)
        elif choice == '3':
            list_issues()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\n🔎Welcome to IssueTracker CLI!📍")
        print("1. Manage Users")
        print("2. Manage Issues")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_issues()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    create_tables()
    main_menu()