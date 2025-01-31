import os
from flask import Flask, url_for, flash, redirect, abort, render_template, request

app = Flask(__name__)


from players.views import players_bp

app.register_blueprint(players_bp)
