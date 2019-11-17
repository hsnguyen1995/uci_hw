# Dependencies
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
        f"Note: Dates are YYYY-MM-DD format. Example:/api/v1.0/2017-11-29/2017-12-14"
    )

# Get date that was a year prior to last data point. Query to obtain filtered data, using the date and prcp filters. Leave out days that don't have prcp data.
@app.route("/api/v1.0/precipitation")
def precipitation():
    dateYearAgo = dt.date(2017,8,23) - dt.timedelta(days=365)
    prcp_data_query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= dateYearAgo, Measurement.prcp != None).all()
    prcp_values = []
    for p in prcp_data_query:
        precipitation_dic = {p.date: p.prcp}
        prcp_values.append(precipitation_dic)

    return jsonify(prcp_values)

# Query to obtain all station data. use np.ravel to return the data into full list
@app.route("/api/v1.0/stations")
def stations():
    station_query = session.query(Measurement.station).all()
    all_stations = list(np.ravel(station_query))
    return jsonify(all_stations)

# Get date that was a year prior to last data point. Query to obtain tobs data. use np.ravel to return the data into full list
@app.route("/api/v1.0/tobs")
def tobs():
    dateYearAgo = dt.date(2017,8,23) - dt.timedelta(days=365)
    station_with_highest_tobs = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281', Measurement.date >= dateYearAgo).order_by(Measurement.tobs).all()
    all_tobs = list(np.ravel(station_with_highest_tobs))
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def tobs_start(start):
    tobs_start_query = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    tobs_start_results = list(np.ravel(tobs_start_query))
    return jsonify(tobs_start_results)

@app.route("/api/v1.0/<start>/<end>")
def tobs_startend(start, end):
    tobs_startend_query = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    tobs_startend_results = list(np.ravel(tobs_startend_query))
    return jsonify(tobs_startend_results)


if __name__ == '__main__':
    app.run()