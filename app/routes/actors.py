from flask import Blueprint, render_template
from app.database import Database

actors_bp = Blueprint("actors", __name__)


@actors_bp.route("/")
def view_all_actors():
    """Fetch and display all actors."""

    # >>>> TODO 1: Write a query that fetches all actors from `People` <<<<
    #              The query should retrieve `name`, `nationality`, `dob`, and `gender`.

    query = """SElECT DISTINCT p.name, p.nationality, p.dob, p.gender
    	       FROM People p
    	       JOIN Role r ON p.id = r.pid
    	       WHERE r.role_name = 'Actor';
    	    """

    with Database() as db:
        actors = db.execute(query=query)

    return render_template("actors.html", actors=actors)
