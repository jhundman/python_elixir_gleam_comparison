import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
import requests
import time
from collections import Counter
import sqlite3
from datetime import datetime


console = Console(width=80)
app = typer.Typer()


def get_foggy_data(lat: float, long: float):
    payload = {
        "latitude": lat,
        "longitude": long,
        "hourly": "weather_code",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "auto",
    }

    response = requests.get("https://api.open-meteo.com/v1/forecast", params=payload)
    data = response.json()

    codes = data["hourly"]["weather_code"]
    counts = Counter(codes)

    foggy_hours = counts[45] + counts[48]
    first_date = None

    if foggy_hours > 0:
        i_45 = codes.index(45) if 45 in codes else float("inf")
        i_48 = codes.index(48) if 48 in codes else float("inf")
        first_date = data["hourly"]["time"][min(i_45, i_48)]

    return foggy_hours, first_date


def insert_record(
    location: str, lat: float, long: float, foggy_hours: int, first_date: str
):
    insert_sql = """
        INSERT INTO weather_data (date, location, lat, long, foggy_hours, first_date)
        VALUES (?, ?, ?, ?, ?, ?);
    """

    insert_data = (
        datetime.now().date().strftime("%Y-%m-%d"),
        location,
        lat,
        long,
        foggy_hours,
        first_date,
    )

    with sqlite3.connect("../foggy.db") as con:
        cur = con.cursor()
        cur.execute(insert_sql, insert_data)
        con.commit()

    print("1 Record Inserted")
    return


@app.command()
def foggy(location: str, lat: float, long: float):
    console.print(
        """I will consult with the loremasters of the sky """
        """to ascertain if the spirits are to cast their foggy spell upon """
        f"""[bold #fcbb92]{location}[/bold #fcbb92] in the next seven dawns.""",
        style="#cce4fc",
    )

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
    )

    with progress:
        get_api = progress.add_task(description="[#fcbb92]Consulting...")
        time.sleep(0.5)
        foggy_hours, first_index = get_foggy_data(lat, long)
        print(foggy_hours, first_index)
        progress.update(get_api, description="[green]Consulted", completed=100)

        log_data = progress.add_task(description="[#fcbb92]Recording...")
        time.sleep(0.5)
        insert_record(location, lat, long, foggy_hours, first_index)
        progress.update(log_data, description="[green]Recorded", completed=100)


@app.command()
def list():
    # Create Table
    table = Table()

    with sqlite3.connect("../foggy.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM weather_data;")
        records = cur.fetchall()

        for column in cur.description:
            table.add_column(column[0])

        for row in records:
            table.add_row(*[str(item) for item in row])

    # Print the table
    console.print(table, style="#fcbb92")


if __name__ == "__main__":
    app()


# create_table = """
#     --DROP TABLE IF EXISTS weather_data;
#     CREATE TABLE weather_data (
#         date TEXT,
#         location TEXT,
#         lat REAL,
#         long REAL,
#         foggy_hours INTEGER,
#         first_date TEXT
#     );
# """
#    cur.execute(create_table)
