defmodule TipssvenskanWebWeb.RegisterLive do
  use TipssvenskanWebWeb, :live_view

  def render(assigns) do
    ~H"""
    <section class="max-w-4xl mx-auto px-6 py-12">
      <h2 class="text-3xl font-bold mb-4">Registrera användare</h2>
      <p class="text-base-content/80"></p>
    </section>
    """
  end
end
