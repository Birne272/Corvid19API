'''
Created on 21.03.2020

@author: Jan-Erik Matthies
'''
from flask import render_template
from flask_cors import CORS
import connexion

HOST_ADDRESS =  "bene.gridpiloten.de"
#HOST_ADDRESS = "localhost"

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# add CORS support
CORS(app.app)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/apiUI/')
def apiUI():
    return render_template('apiUi/index.html')
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(port=8000, debug=True)
