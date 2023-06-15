from data_sources.api import sg_taxi_availability
from data_warehouse import bigquery_api
from data_warehouse import bigquery_schemas
from transformation.transformation import Transformation
from transformation import time_utils
from os import environ

if __name__ == "__main__":

    data_sources = sg_taxi_availability.ApiCall()
    data_warehouse = bigquery_api.BigqueryApi()
    bq_schemas = bigquery_schemas.BigQueryTableSchemas()
    time_utility = time_utils.TimeUtils()
    transformation = Transformation()

    time_now_minutes_version = time_utility.get_minutes()
    time_now_hours_version = time_utility.get_hourly()

    cordinates = data_sources.get_cordinates_dataset()

    # bigquery properties
    bq_project_id = environ["bq_project_id"]
    bq_dataset_id = environ["bq_dataset_id"]
    bq_table_id = environ["bq_table_id"]

    full_table_name = "{0}.{1}.{2}".format(bq_project_id, bq_dataset_id, bq_table_id)

    data_warehouse.create_table(
        bq_project_id, bq_dataset_id, bq_table_id, bq_schemas.sg_taxi_availability()
    )

    datas = [
        {
            "longitude": data[0],
            "latitude": data[1],
            "latitude_longitude": "{},{}".format(str(data[1]), str(data[0])),
            "road_name": transformation.get_road_from_api(
                data_sources.geocode(data[0], data[1])
            ),
            "inserted_time": time_now_minutes_version,
            "inserted_time_hourly": time_now_hours_version,
        }
        for data in cordinates
    ]
    
    print("data amount that will be insert : {}".format(len(datas)))
    
    data_warehouse.insert_rows_json(
        full_table_name, datas, bq_schemas.sg_taxi_availability()
    )
