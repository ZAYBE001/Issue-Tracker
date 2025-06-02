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

def main():
    parser = argparse.ArgumentParser(description="IssueTracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    # User commands
    user_parser = subparsers.add_parser('user', help='Manage users')
    user_subparsers = user_parser.add_subparsers(dest='user_command')
    
    create_user_parser = user_subparsers.add_parser('create', help='Create a new user')
    create_user_parser.add_argument('username', help='Username')
    create_user_parser.add_argument('email', help='Email')
    
    delete_user_parser = user_subparsers.add_parser('delete', help='Delete a user')
    delete_user_parser.add_argument('username', help='Username')
    
    list_users_parser = user_subparsers.add_parser('list', help='List all users')

    # Issue commands
    issue_parser = subparsers.add_parser('issue', help='Manage issues')
    issue_subparsers = issue_parser.add_subparsers(dest='issue_command')
    
    create_issue_parser = issue_subparsers.add_parser('create', help='Create a new issue')
    create_issue_parser.add_argument('title', help='Title')
    create_issue_parser.add_argument('description', help='Description')
    create_issue_parser.add_argument('priority', choices=['Low', 'Medium', 'High'], help='Priority')
    create_issue_parser.add_argument('status', choices=['Open', 'In Progress', 'Resolved'], help='Status')
    create_issue_parser.add_argument('username', help='Username of the creator')
    
    delete_issue_parser = issue_subparsers.add_parser('delete', help='Delete an issue')
    delete_issue_parser.add_argument('issue_id', type=int, help='Issue ID')
    
    list_issues_parser = issue_subparsers.add_parser('list', help='List all issues')

    args = parser.parse_args()

    if args.command == 'user':
        if args.user_command == 'create':
            create_user(args.username, args.email)
        elif args.user_command == 'delete':
            delete_user(args.username)
        elif args.user_command == 'list':
            list_users()
    elif args.command == 'issue':
        if args.issue_command == 'create':
            create_issue(args.title, args.description, args.priority, args.status, args.username)
        elif args.issue_command == 'delete':
            delete_issue(args.issue_id)
        elif args.issue_command == 'list':
            list_issues()

if __name__ == '__main__':
    create_tables()
    main()