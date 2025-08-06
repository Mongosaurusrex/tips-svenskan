defmodule TipssvenskanWeb.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      TipssvenskanWebWeb.Telemetry,
      TipssvenskanWeb.Repo,
      {DNSCluster, query: Application.get_env(:tipssvenskan_web, :dns_cluster_query) || :ignore},
      {Phoenix.PubSub, name: TipssvenskanWeb.PubSub},
      # Start a worker by calling: TipssvenskanWeb.Worker.start_link(arg)
      # {TipssvenskanWeb.Worker, arg},
      # Start to serve requests, typically the last entry
      TipssvenskanWebWeb.Endpoint
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: TipssvenskanWeb.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    TipssvenskanWebWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
