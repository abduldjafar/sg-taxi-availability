from google.cloud import bigquery

class BigQueryTableSchemas(object):
    def __init__(self):
        pass

    def sg_taxi_availability(self):

        return [
            bigquery.SchemaField("latitude", "FLOAT", mode="REQUIRED"),
            bigquery.SchemaField("longitude", "FLOAT", mode="REQUIRED"),
            bigquery.SchemaField("latitude_longitude", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("road_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("inserted_time", "DATETIME", mode="REQUIRED"),
            bigquery.SchemaField("inserted_time_hourly", "DATETIME", mode="REQUIRED")
            
        ]