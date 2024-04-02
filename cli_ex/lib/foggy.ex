defmodule Foggy do
  alias Foggy.Repo
  alias Foggy.Db

  def foggy_weather(location, lat, long) do
    IO.puts(
      IO.ANSI.blue() <>
        "Wind’s howling. Don’t mistake the stars reflected in a pond at " <>
        "night for those in the sky. Consulting the weather..." <>
        IO.ANSI.reset()
    )

    IO.write("Searching...")
    :timer.sleep(100)

    IO.write("\rSearched     \n")
    IO.write("Gathering...")
    :timer.sleep(100)

    hours = get_data(location, lat, long)
    IO.puts("\nThere will be #{hours} hours of fog in the next 7 days.")

    IO.write("\rGathered     \n")
    IO.write("Recording...")

    # hours
    # |> (&record_data(&1, location, lat, long)).()

    :timer.sleep(100)
    IO.write("\rDone")
  end

  # defp save_data()

  defp get_data(location, lat, long) do
    payload = %{
      "latitude" => lat,
      "longitude" => long,
      "hourly" => "weather_code",
      "temperature_unit" => "fahrenheit",
      "wind_speed_unit" => "mph",
      "precipitation_unit" => "inch",
      "timezone" => "auto"
    }

    response = Req.get!("https://api.open-meteo.com/v1/forecast", params: payload)

    foggy_hours = Enum.count(response.body["hourly"]["weather_code"], &(&1 == 45 || &1 == 48))
    foggy_hours
  end

  # defp record_data(foggy_hours, location, lat, long) do
  #   current_date = Date.utc_today()

  #   new_record = %Foggy.Db{
  #     date: current_date,
  #     location: location,
  #     lat: lat,
  #     long: long,
  #     foggy_hours: foggy_hours,
  #     first_date: nil
  #   }

  #   case Foggy.Repo.insert(new_record) do
  #     {:ok, _record} ->
  #       IO.puts("Data recorded successfully.")

  #     {:error, changeset} ->
  #       IO.inspect(changeset)
  #   end
  # end
end
