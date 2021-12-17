from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

# Initialise Flask for it to know where to find resources
# https://stackoverflow.com/questions/39393926/flaskapplication-versus-flask-name
app = Flask(__name__) 

# Initialise the Api
api = Api(app)

# Variables needed
# Country, aggregate or sector, 
# if aggregate new postings, total_postings or all_postings 
# if sector specific sector or all sector

aggregate_country_path = "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/AU/aggregate_job_postings_AU.csv"

#inherit the Resource object?
class Country(Resource):
    def get(self):
        data = pd.read_csv(aggregate_country_path)
        data = data.to_dict()
        return {"data": data}, 200


api.add_resource(Country, "/country")


if __name__ == "__main__":
    app.run(debug = True)

