from library import library as app, session_manager
import os

app.config['app_root'] = os.path.abspath(os.path.dirname(__file__))
app.config['app_static'] = app.config['app_root'] + "library/static/master/"
app.secret_key = 'library_management_system'

session_manager.init_app(app)


session_manager.login_view = "login"
session_manager.refresh_view = "login"
session_manager.session_protection = "strong"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)