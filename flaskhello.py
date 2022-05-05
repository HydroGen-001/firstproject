from flask import Flask, render_template, request
import os
folder = os.getcwd()
print("papka:", folder) #убедитесь, что папка templates у вас точно по получившемуся адресу
app = Flask(__name__, template_folder=folder)

@app.route('/')
def index():
    return render_template('templates/vvod.html')
    
@app.route('/login', methods=['POST', 'GET'])
def index2():
    user = request.args.get('user')
    print(user)
    return render_template('templates/vivod.html', user=user)

app.run()

