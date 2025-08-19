defmodule TipssvenskanWeb.PageController do
  use TipssvenskanWeb, :controller

  def home(conn, _params) do
    render(conn, :home)
  end
end
