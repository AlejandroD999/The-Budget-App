from flask import render_template, request, session, Blueprint, redirect, url_for
from .utils import get_year_range, string_to_date 
from .expenses_db import * 
import os

# TODO Make expense table date the same format as input

CURR_DIR_PATH = os.path.dirname(__file__)

features_bp = Blueprint("features", __name__, 
                        template_folder="templates", static_folder="static",
                        static_url_path="/src/features/static")


@features_bp.route("/expenses", methods=["GET", "POST"])
def expenses():
    # TODO Add filter reset button

    username = session.get("user")
    user_id = session.get("user_id")
    
    if not username or not user_id:
        return redirect(url_for("auth.sign_in"))

    expenses = pull_expenses(user_id) 
    
    # Filter Expenses
    if request.method == "POST":
        start_date= request.form.get("start_date")
        end_date= request.form.get("end_date") 
        
        if not start_date or not end_date:
            # TODO Prompt error (maybe optional due to other actions) 
            return
        
        expenses = pull_expenses(user_id, start_date=string_to_date(start_date), end_date=string_to_date(end_date))
        
    headers = get_headers() 
    years = get_year_range()
    table_headers = [] 

    if not headers:
        # TODO Handle error 
        pass
    
    for header in headers:
        if "id" not in header.lower():
            table_headers.append(header)

    return render_template("expenses.html",
                           table_headers=table_headers,
                           expenses=expenses,
                           years=years)

@features_bp.route("/expenses/create-expense", methods=["POST"])
def create():
    username = session.get("user")
    user_id = session.get("user_id")

    if not username or not user_id:
        return redirect(url_for("auth.sign_in"))
    
    description = request.form.get("description")
    amount = request.form.get("amount")
    date = request.form.get("date")
    
    if not description or not amount or not date:
        # TODO Error pop up
        return redirect(url_for('features.expenses'))

    insert_expense(user_id, description, amount, date) 
     
    return redirect(url_for('features.expenses'))

@features_bp.route('/expenses/delete-expense', methods=["POST"])

def delete():
    user_id = session.get("user_id")

    expense_id = request.form.get("expense_id")
    
    if not expense_id or not user_id:
        # TODO Error pop-up
        return redirect(url_for('features.expenses'))
     
    delete_expense(expense_id, user_id)

    return redirect(url_for('features.expenses'))

@features_bp.route("/expenses/edit-expense", methods=["POST"])
def edit():
    return redirect(url_for("features.expenses")) 

