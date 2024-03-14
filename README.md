# Comparison of Python, Elixir, and Gleam

# Work in Progress

## Description

Recently saw the release of Gleam and I wanted to compare that with Python, a language I am familiar with, and Elixir as I am interested in learning. Elixir and Gleam seem similar in many regards so I figured why not compare all three. This will be a very simple CLI app which tells you how many hours over the next 7 days will be foggy, and when the first time it will be. It will also save some data to sqlite.

This simple exploration will be as follows:

- Create a CLI app in all three languages
- The goal of the app is to have the two following commands
  - `foggy` which calls the open meteo api for a given location lat long for the next week. It logs the location name, lat long, date, and number of hours in a sql lite db.
  - `list` which prints out all the data from the sqlite db.

## Links

[Open Meteo API](https://open-meteo.com/en/docs#hourly=weather_code&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=auto)

https://api.open-meteo.com/v1/forecast?latitude=33.7&longitude=-84.38&hourly=weather_code&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=auto
