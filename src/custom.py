# this file imports custom routes into the experiment server
from flask import Blueprint, render_template, request, jsonify, Response, abort, current_app, make_response
from jinja2 import TemplateNotFound
from functools import wraps
from sqlalchemy import or_

from psiturk.psiturk_config import PsiturkConfig
from psiturk.experiment_errors import ExperimentError, InvalidUsage
from psiturk.user_utils import PsiTurkAuthorization, nocache

# # Database setup
from psiturk.db import db_session, init_db
from psiturk.models import Participant
from json import dumps, loads

# Helper import
from helpers import *

# load the configuration options
config = PsiturkConfig()
config.load_config()
# if you want to add a password protect route use this
myauth = PsiTurkAuthorization(config)

# explore the Blueprint
custom_code = Blueprint('custom_code', __name__,
                        template_folder='templates', static_folder='static')

# ----------------------------------------------
# Accessing data
# ----------------------------------------------
@custom_code.route('/view_data')
@myauth.requires_auth
def list_my_data():
    users = Participant.query.all()
    try:
        return render_template('list.html', participants=users)
    except TemplateNotFound:
        abort(404)


# ----------------------------------------------
# Downloading data
# ----------------------------------------------
@custom_code.route('/get_data')
@myauth.requires_auth
def get_data():
    workerId = request.args.get('id')
    data_type = request.args.get('dataType')
    participant = Participant.query.filter(Participant.workerid == workerId).one()
    output = make_response(get_datafile(participant, data_type))
    output.headers["Content-Disposition"] = "attachment; filename={}-{}.csv".format(workerId,data_type)
    output.headers["Content-Type"] = "text/csv"
    return output