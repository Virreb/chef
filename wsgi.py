from api import app
from globals import IP, PORT

if __name__ == '__main__':
    app.run(host=IP, port=PORT, debug=False, threaded=True)

# To run this locally:
# gunicorn -c gunicorn.conf.py wsgi:app

