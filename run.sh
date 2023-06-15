export GOOGLE_APPLICATION_CREDENTIALS=/opt/credentils/google/keys.json
export bq_project_id=quipper-school-analytics-dev
export bq_dataset_id=tmp
export bq_table_id=sg_taxi_availability
while true;
do
    python main.py
    sleep 2m
done