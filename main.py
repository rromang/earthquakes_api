# python version 3.8.12
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData, inspect, Table

from flask import Flask, jsonify, render_template
from flask import url_for
import json


# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__, static_url_path='/static/')

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Database/db/earthquake_db")

metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)
# Earthquakes = metadata_obj.tables['earthquake_raw']
earthquakes = Table('earthquake_raw', metadata_obj, autoload_with=engine)
columns = [c.name for c in earthquakes.columns]
# print(columns)

Base = automap_base(metadata=metadata_obj)
Base.prepare()
# print(Base.classes.keys())
Earthquakes = Base.classes.earthquake_raw
# print(Earthquakes)

# #################################################
# # Flask Routes
# #################################################
with open('Database/json/earthquake.json', 'r') as myfile:
    data = myfile.read()

@app.route("/")
def welcome():
    # """List all available api routes."""
    return render_template('index.html')
        
@app.route("/earthquakes")
def earthquakes():
    session = Session(engine)

    """Return a list of all earthquake information"""
        # Query all measurements
    results = session.query(Earthquakes.time, Earthquakes.mag, Earthquakes.latitude, Earthquakes.longitude, \
            Earthquakes.depth, Earthquakes.magType, Earthquakes.nst, Earthquakes.gap, Earthquakes.dmin, \
                Earthquakes.rms, Earthquakes.net, Earthquakes.id, Earthquakes.updated).all()

    session.close()

        # Convert list of tuples into normal list
    all_earthquakes = []
    for time, mag, lat, lon, depth, magType, nst, gap, dmin, rms, net, id_equake, updated in results:
        equake_dict = {}
            
        equake_dict['mag'] = mag
        equake_dict['latitude'] = lat
        equake_dict['longitude'] = lon
        equake_dict['depth'] = depth
        equake_dict['time'] = time
        equake_dict['magType'] = magType
        equake_dict['nst'] = nst
        equake_dict['gap'] = gap
        equake_dict['dmin'] = dmin
        equake_dict['rms'] = rms
        equake_dict['net'] = net
        equake_dict['id'] = id_equake
        equake_dict['updated'] = updated
        all_earthquakes.append(equake_dict)
        
    return jsonify(all_earthquakes)


if __name__ == '__main__':
    app.run(debug=True)