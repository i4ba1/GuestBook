from flask import Blueprint

guest = Blueprint('guest', __name__)

@guest.route("/getAllGuest")
def get_all_guest():
    return