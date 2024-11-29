from flask import Flask, render_template
from src.security.decorators import login_required
from src.routeControllers.oauth import oauthPage, initOauthClient
from src.config.appConfig import loadAppConfig

# https://gist.github.com/thomasdarimont/6a3905778520b746ff009cf3a41643e9
# https://stackoverflow.com/a/78419713/2746323
# get application config
appConfig = loadAppConfig()

initOauthClient()

app = Flask(__name__)

app.secret_key = "hkajshfkhkjhkjhgkf"

app.register_blueprint(oauthPage, url_prefix='/oauth')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

@app.route('/admin')
@login_required(roles=["admin"])
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50100, debug=True)
