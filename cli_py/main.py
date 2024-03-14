import typer
from rich.console import Console
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn
import time
from collections import Counter


console = Console(width=80)
app = typer.Typer()


def get_foggy_data(lat: float, long: float):
    payload = {
        "latitude": 33.7,
        "longitude": -84.38,
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
    foggy_hours = counts[45] + counts[48] + 0
    first_date = None
    if foggy_hours > 0:
        i_45 = codes.index(45) if 45 in codes else float("inf")
        i_48 = codes.index(48) if 48 in codes else float("inf")
        first_date = data["hourly"]["time"][min(i_45, i_48)]

    return foggy_hours, first_date


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
        progress.update(log_data, description="[green]Recorded", completed=100)


@app.command()
def list(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
