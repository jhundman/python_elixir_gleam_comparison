defmodule Foggy.Db do
  use Ecto.Schema

  schema "weather_data" do
    field(:date, :date)
    field(:location, :string)
    field(:lat, :float)
    field(:long, :float)
    field(:foggy_hours, :integer)
    # You might want to calculate this value
    field(:first_date, :date)
  end
end
