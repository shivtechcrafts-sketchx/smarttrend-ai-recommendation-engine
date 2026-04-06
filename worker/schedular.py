import time
from app.routes.trends import get_trends

while True:
    print("Refreshing data...")
    get_trends()
    time.sleep(3600)