from application import app, server, db, models


if __name__ == '__main__':
    app.run_server(
        debug=True
    )