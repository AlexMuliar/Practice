from flask import Flask, make_response, url_for, Blueprint

from routes.user import api_user
from config import app, db


api_root = Blueprint('root-route', __name__)



def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)



@api_root.route("/")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return make_response(dict(links=links))


app.register_blueprint(api_user)
app.register_blueprint(api_root)


if __name__ == '__main__':
    db.create_all()
    app.run('0.0.0.0', 5000, debug=True)
