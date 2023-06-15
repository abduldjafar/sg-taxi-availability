from time import sleep
from google.cloud import bigquery
from requests import HTTPError
from google.api_core.exceptions import AlreadyExists, Conflict
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
logger = logging.getLogger('spam')


class BigqueryApi(object):
    def __init__(self):
        self.client = bigquery.Client()
        
    
    def insert_rows_json(self,table_id,datas,schema):

        job_config = bigquery.LoadJobConfig()
        job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
        job_config.schema = schema
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        job = self.client.load_table_from_json(datas, table_id, job_config = job_config)

        logger.info("job with id {0} is {1}".format(job.job_id,job.state))


    def create_table(self,project_id, dataset_id, table_id, schema):
        full_table_name =  "{0}.{1}.{2}".format(project_id, dataset_id,table_id)

        table = bigquery.Table(
            full_table_name,
            schema=schema,
           
        )

        table.time_partitioning=bigquery.TimePartitioning(
                type_=bigquery.TimePartitioningType.HOUR,
                field="inserted_time_hourly",
                expiration_ms=None
        )

        try:
            self.client.create_table(table)
            logger.info("Table {}.{}.{} created.".format(project_id, dataset_id, table_id))
            sleep(10)
        except AlreadyExists:
            logger.error("Caught google.api_core.exceptions.AlreadyExists")
        except Conflict:
            logger.error("Caught google.api_core.exceptions.Conflict")
        