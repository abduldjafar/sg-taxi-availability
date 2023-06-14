from data_sources.api import sg_taxi_availability
from data_warehouse import bigquery_api
from data_warehouse import bigquery_schemas
from utils import time_utils
from os import environ

if __name__ == '__main__':

    data_sources = sg_taxi_availability.ApiCall()
    data_warehouse = bigquery_api.BigqueryApi()
    bq_schemas = bigquery_schemas.BigQueryTableSchemas()
    time_utility = time_utils.TimeUtils()

    time_now_minutes_version = time_utility.get_minutes()
    cordinates = data_sources.get_cordinates_dataset()

    # bigquery properties
    bq_project_id = environ["bq_project_id"]
    bq_dataset_id = environ["bq_dataset_id"]
    bq_table_id = environ["bq_table_id"]
    
    full_table_name = "{0}.{1}.{2}".format(
        bq_project_id, bq_dataset_id, bq_table_id)

    data_warehouse.create_table(
        bq_project_id, bq_dataset_id, bq_table_id, bq_schemas.sg_taxi_availability())

    datas = [{
        "longitude": data[0],
        "latitude":data[1],
        "latitude_longitude":"{},{}".format(str(data[1]), str(data[0])),
        "inserted_date":time_now_minutes_version
    } for data in cordinates]

    data_warehouse.insert_rows_json(
        full_table_name, datas, bq_schemas.sg_taxi_availability())
