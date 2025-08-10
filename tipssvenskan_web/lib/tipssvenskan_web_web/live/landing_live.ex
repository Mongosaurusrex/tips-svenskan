defmodule TipssvenskanWebWeb.LandingLive do
  use TipssvenskanWebWeb, :live_view

  def mount(_params, _session, socket) do
    {:ok,
     socket
     |> assign(:page_title, "Tipssvenskan – Tippa slutställningen")
     |> assign(:cta_loading, false)}
  end

  def handle_event("start", _params, socket) do
    {:noreply, push_navigate(socket, to: ~p"/register")}
  end

  def handle_event("learn_more", _params, socket) do
    {:noreply, push_navigate(socket, to: ~p"/about")}
  end
end
