from flask import Flask

app= Flask(__name__,template_folder="views")

app.secret_key ='YDdYb'

from application.controllers import *

