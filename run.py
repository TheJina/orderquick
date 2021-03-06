import os
from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv('PROD_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
    app.run()
