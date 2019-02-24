"""Main file"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.debug = True
    app.config['BUNDLE_ERRORS'] = True
    app.run(host='0.0.0.0', port=5000)
