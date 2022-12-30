# Standard imports
import os
from datetime import datetime
from dotenv import load_dotenv
from toolkit4life.requests import BaseRequests
from toolkit4life.clients.postgres import PostgresClient
from apscheduler.schedulers.blocking import BlockingScheduler

# Load .env
load_dotenv()

postgres_client = PostgresClient(
    host = os.getenv("POSTGRES_HOST"),
    port = os.getenv("POSTGRES_PORT"),
    username = os.getenv("POSTGRES_USERNAME"),
    password = os.getenv("POSTGRES_PASSWORD"),
    schema = "public",
    database = "http-monitor"
)
request = BaseRequests(timeout = 10, retries = 1)

def get_address_status(interval):
    # Get alld the addresses with the given interval
    df = postgres_client._select(f"SELECT * FROM tracker_address WHERE interval = {interval}")
    for _, row in df.iterrows():
        # Get response from URL
        response = request.get(row["url"])
        # Insert request record into database
        postgres_client._execute(f"INSERT INTO tracker_request (status_code, created_at, track_id) VALUES ({response.status_code}, '{datetime.now()}', {row['id']})")


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(func = get_address_status, trigger = "interval", minutes = 1, args = (1))     # every 1 minute
    scheduler.add_job(func = get_address_status, trigger = "interval", minutes = 5, args = (5))     # every 5 minute
    scheduler.add_job(func = get_address_status, trigger = "interval", minutes = 10, args = (10))   # every 10 minutes
    scheduler.add_job(func = get_address_status, trigger = "interval", minutes = 30, args = (30))   # every 30 minutes
    scheduler.add_job(func = get_address_status, trigger = "interval", minutes = 60, args = (60))   # every 60 minutes
    scheduler.start()   # Start to scheduler