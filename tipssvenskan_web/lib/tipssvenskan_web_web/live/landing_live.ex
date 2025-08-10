defmodule TipssvenskanWebWeb.LandingLive do
  use TipssvenskanWebWeb, :live_view

  def mount(_params, _session, socket) do
    {:ok, assign(socket, :page_title, "Tipssvenskan")}
  end
end
