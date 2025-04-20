from flask import Blueprint, render_template, redirect, url_for, flash
from forms import BugForm
from models import Bug
from extensions import db

bug_routes = Blueprint('bug_routes', __name__)

@bug_routes.route('/')
def index():
    return redirect(url_for('bug_routes.report_bug'))

@bug_routes.route('/report', methods=['GET', 'POST'])
def report_bug():
    form = BugForm()
    if form.validate_on_submit():
        bug = Bug(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data
        )
        db.session.add(bug)
        db.session.commit()
        flash('Bug submitted successfully!', 'success')
        return redirect(url_for('bug_routes.bug_history'))
    return render_template('report_bug.html', form=form)

@bug_routes.route('/history')
def bug_history():
    bugs = Bug.query.all()
    return render_template('bug_history.html', bugs=bugs)
