from db import db, app
from routes import configure_routes

configure_routes(app, db)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)