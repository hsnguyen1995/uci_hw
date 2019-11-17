import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


#Create engine to SQLite database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect existing database 
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session 
session = Session(engine)


# Initiate Flask
app = Flask(__name__)


# Flask Routes

@app.route("/")
def welcome():
    """Welcome to the Hawaii Climate Analyis Page! Navigate to any of the following routes."""
    return (
        f"Available Routes:<br/>"
        f"===========================<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        f"===========================<br/>"
        f"Note: Dates are YYYY-MM-DD format."
    )

@app.route("/api/v1.0/precipitation")
def prcp():

@app.route("/api/v1.0/stations")
def stations():

@app.route("/api/v1.0/tobs")
def tobs():

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def info():


if __name__ == '__main__':
    app.run()