from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

# https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-portal%2Cvscode-deploy%2Cterminal-bash%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli
# https://portal.azure.com/#@jmichaelrollins89gmailcom.onmicrosoft.com/resource/subscriptions/062bd048-67c7-4556-8c26-ce4bdb2133a7/resourcegroups/MTG_Testing_Resource_Group/providers/Microsoft.Web/sites/Mtg-Search-For-Deck/appServices
@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()