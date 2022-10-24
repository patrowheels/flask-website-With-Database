from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
# this is how you define a blueprint and you choose to call it views.
views = Blueprint('views', __name__)

# this is a root and in this case it needs the function right after it


# adding in the methods attribute allows this route to recieve "GET" or "POST" requests
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        # request.for.get('note') is getting the text area element from our home.html by its atrribute "note"
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


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    # when you use get it accesses the primary key
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

# @views.route('/edit-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     # when you use get it accesses the primary key
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.add(note)
#             db.session.commit()

#     return jsonify({})
