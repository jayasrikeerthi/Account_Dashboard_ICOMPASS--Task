from flask import Blueprint, render_template, request, flash, redirect, url_for
from extensions import db  # Import db correctly
from models import User, Billing  # Import models
from forms import RegistrationForm

routes_bp = Blueprint("routes", __name__)  # Define Blueprint

@routes_bp.route("/", methods=["GET", "POST"])

def dashboard():
    if request.method == "POST":
        name = request.form.get("name")
        flash(f"Welcome, {name}!", "success")
    return render_template("dashboard.html")

@routes_bp.route("/billing", methods=["GET", "POST"])
def billing():
    if request.method == "POST":
        flash("Billing details updated!", "success")
    return render_template("billing.html")

@routes_bp.route("/plans", methods=["GET", "POST"])
def plans():
    if request.method == "POST":
        plan_choice = request.form.get("plan")
        flash(f"You selected the {plan_choice} plan!", "success")
    return render_template("plans.html")

@routes_bp.route("/notifications", methods=["GET", "POST"])
def notifications():
    return render_template("notifications.html")

@routes_bp.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        flash("Profile updated successfully!", "success")
    return render_template("profile.html")


