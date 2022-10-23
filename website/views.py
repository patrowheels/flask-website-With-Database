from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
# this is how you define a blueprint and you choose to call it views.
views = Blueprint('views', __name__)

# this is a root and in this case it needs the function right after it


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note is to short", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    # return "<h1>Home</h1>""<h1>Welcome</h1>"
    return render_template("home.html", user=current_user)
