defmodule Foggy do
  def foggy_weather(location, lat, long) do
    get_data(location, lat, long)
  end

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

    IO.puts("#{location} RESPONSE BODY" <> Integer.to_string(foggy_hours))
  end
end
