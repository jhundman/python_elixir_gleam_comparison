defmodule CLI do
  def print([]) do
    IO.puts("Hello, World!")
  end

  def print([arg | _tail]) do
    IO.puts("Hello, #{arg}!")
  end
end
