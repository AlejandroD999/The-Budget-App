from ..extensions import db
from ..models.expenses_mod import Expenses
from datetime import date

def insert_expense(user_id, description, amount, date):
    statement = Expenses(user_id=user_id, description=description, amount=amount, date=date)
    
    try:
        db.session.add(statement)
        db.session.commit()

    except Exception:
        print("Error creating expense")
        db.session.rollback()

def update_expense(user_id, expense_id, new_description, new_amount, new_date):
    
    expense = pull_expense(expense_id, user_id)
    
    if new_description != expense.description:
        expense.description = new_description

    if new_amount != expense.amount:
        expense.amount = new_amount

    if new_date != expense.date:
        expense.date = new_date
    
    try:
        db.session.commit()

    except Exception:
        print("Error updating expense")
        db.session.rollback()

def get_headers():
    return [column.name.capitalize() for column in Expenses.__table__.columns]

def pull_expense(expense_id, user_id):
    if not expense_id or not user_id:
        # TODO Handle Error
        return
    
    expense = db.session.execute(db.select(Expenses).filter_by(
        id=expense_id, 
        user_id=user_id
        )).scalar_one_or_none()

    return expense
    

def pull_expenses(user_id, start_date=None, end_date=None):
    # Fetch and return expenses in rows [Expenses>1, Expenses>2, ...]
    # Optional: filter date -> uses start_date and end_date
    
    # TODO Clean and strengthen
    # Handle types && narrow method 

    if not start_date or not end_date: 
        return db.session.scalars(db.select(Expenses).filter_by(user_id=user_id)).all()
     
    expense = db.session.scalars(db.select(Expenses).where(
        Expenses.user_id==user_id,
        Expenses.date >= start_date, 
        Expenses.date < end_date)).all()

    return expense
    

def delete_expense(expense_id, user_id):
    expense = pull_expense(expense_id, user_id)
    
    if not expense:
        # TODO Error pop up
        print("Error deleting expense")
        return 

    try:
        db.session.delete(expense)
        db.session.commit()

    except Exception:
        print("Error deleting expense")
        db.session.rollback()

