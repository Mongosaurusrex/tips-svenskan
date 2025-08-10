defmodule TipssvenskanWebWeb.ContactLive do
  use TipssvenskanWebWeb, :live_view

  @impl true
  def mount(_params, _session, socket) do
    {:ok, assign(socket, page_title: "Kontakt")}
  end
end
