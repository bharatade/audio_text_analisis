from monitoring.monitor import start_monitoring
from database.db_schema import ensure_table_exists

if __name__ == "__main__":
    ensure_table_exists()
    start_monitoring()
