from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

# Initialise Flask for it to know where to find resources
# https://stackoverflow.com/questions/39393926/flaskapplication-versus-flask-name
app = Flask(__name__) 

# Initialise the Api
api = Api(app)

# If needed add a filter point to filter the endpoints for new postings
# And offer a country list possibility
# if aggregate new postings, total_postings or all_postings 
# if sector specific sector or all sector

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