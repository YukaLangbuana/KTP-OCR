from flask import Blueprint
from .forms import ResponseForm
from modules import ping

api_routes = Blueprint('api', __name__)

#PING Routes
@api_routes.route('/api/ping')
def PingController():
    res = ResponseForm()
    res.result = ping.get_response()
    return res.__dict__