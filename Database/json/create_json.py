import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData, inspect, Table


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
# # Json file creation
# #################################################
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

    # data_equakes = json.dumps(all_earthquakes)
    out_file = open("Database/json/earthquake.json", "w")
    json.dump(all_earthquakes, out_file, indent = 6) 
    out_file.close()  