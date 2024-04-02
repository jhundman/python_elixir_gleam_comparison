# In config/config.exs
use Mix.Config

# Configure your database
config :cli_ex, Foggy.Repo,
  adapter: Ecto.Adapters.SQLite3,
  database: "../../foggy.db"
