from datetime import datetime, timedelta


def days_to_go_back(days):
    delta_date = (datetime.now() - timedelta(days=days)).isoformat()
    return delta_date
