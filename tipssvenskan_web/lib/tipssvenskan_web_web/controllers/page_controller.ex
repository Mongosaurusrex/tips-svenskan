defmodule TipssvenskanWebWeb.PageController do
  use TipssvenskanWebWeb, :controller

  def home(conn, _params) do
    render(conn, :home)
  end
end
