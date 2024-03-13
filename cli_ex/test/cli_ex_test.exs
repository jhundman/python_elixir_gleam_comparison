defmodule CliExTest do
  use ExUnit.Case
  doctest CliEx

  test "greets the world" do
    assert CliEx.hello() == :world
  end
end
