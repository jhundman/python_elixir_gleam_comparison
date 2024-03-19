defmodule CLI do
  def main([]) do
    IO.puts("Please do something, I don't got all day")
  end

  def main(["--help"]) do
    # Using ANSI excape instead of more granular controls by table_rex
    rows_o = [["\e[1m\e[34m--help\e[0m", "Show commands, options, and args"]]

    TableRex.quick_render!(rows_o, ["Option", "Description"], "Options")
    |> IO.puts()

    rows_cmd = [
      ["\e[1m\e[34mfoggy\e[0m", "Retrieve foggy data from open-meteo"],
      ["\e[1m\e[34mlist\e[0m", "List current records in database"]
    ]

    TableRex.quick_render!(rows_cmd, ["Command", "Description"], "Commands")
    |> IO.puts()
  end

  def main(["foggy" | rest_args]) do
    case rest_args do
      ["--help"] -> foggy_help()
      [city, lat, long] -> Foggy.foggy_weather(city, lat, long)
      _ -> IO.puts("Wrong args provided, ☹️")
    end
  end

  defp foggy_help do
    rows = [
      ["\e[1m\e[34m#{"location"}\e[0m", "The name of the location"],
      ["\e[1m\e[34mlat\e[0m", "Latitude of the location"],
      ["\e[1m\e[34mlat\e[0m", "Longitude of the location"]
    ]

    TableRex.quick_render!(rows, ["Command", "Description"], "Commands")
    |> IO.puts()
  end
end
