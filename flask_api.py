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
# Use a try block with the pd read and if not working then return a 44 with message of country not available or user input error

# aggregate_country_path = "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/{country}/aggregate_job_postings_{country}.csv"

#inherit the Resource object?
class AggregateCountryJobs(Resource):
    
    def get(self, selected_country):
            data = pd.read_csv(f"https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/{selected_country}/aggregate_job_postings_{selected_country}.csv")
            data = data.to_dict()
            return {"data": data}, 200

class SectorCountryJobs(Resource):
    
    def get(self, selected_country):
            data = pd.read_csv(f"https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/{selected_country}/job_postings_by_sector_{selected_country}.csv")
            data = data.to_dict()
            return {"data": data}, 200


# use the converter from here: https://uniwebsidad.com/libros/explore-flask/chapter-6/url-converters
api.add_resource(AggregateCountryJobs, "/<string:selected_country>/aggregate") 
api.add_resource(SectorCountryJobs, "/<string:selected_country>/sector")

if __name__ == "__main__":
    app.run(debug = True)