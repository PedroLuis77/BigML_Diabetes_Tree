# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.cluster import Cluster
from bigml.api import BigML
# Downloads and generates a local version of the cluster, if it
# hasn't been downloaded previously.
cluster = Cluster('cluster/6176960599dfe7074e0066ea',
                  api=BigML("pedroanillo77",
                            "62a194c19474d1cee6e5a12eb23d908662a90020",
                            domain="bigml.io"))
# To predict centroids fill the desired input_data
# in next line. Numeric fields are compulsory.
input_data = {
    "Diabetes pedigree": 1,
    "Age": 1,
    "Insulin": 1,
    "BMI": 1,
    "Blood pressure": 1,
    "Skinfold": 1,
    "Pregnancies": 1,
    "Glucose": 1}
cluster.centroid(input_data)
# The result is a dict with three keys: distance, centroid_name and
# centroid_id
            
