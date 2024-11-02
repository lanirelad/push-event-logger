from flask import Flask
from routes import bp as appRoutes

app = Flask(__name__)

# Register the routes
app.register_blueprint(appRoutes)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000) #, debug=True
    
    
# "url": "https://github.com/lanirelad/Ansible04/commit/c713ed2971d3b3b29d4df638b42e7d4e0d794d1f",