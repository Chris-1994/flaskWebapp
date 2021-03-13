from flask import Blueprint


web_hooks = Blueprint("web_hooks", __name__)

@web_hooks.route("/page", methods=["POST", "GET"])
def post_data():
    return "This is the post page"


