from api import create_app

if __name__ == "__main__":
    create_app().run(debug=True, port=5000)

# https://stackoverflow.com/questions/70400863/common-file-structure-with-flask-and-flask-sqlalchemy