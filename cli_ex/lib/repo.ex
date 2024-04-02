defmodule Foggy.Repo do
  use Ecto.Repo,
    otp_app: :cli_ex,
    adapter: Ecto.Adapters.SQLite3
end
