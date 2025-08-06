defmodule TipssvenskanWeb.Repo do
  use Ecto.Repo,
    otp_app: :tipssvenskan_web,
    adapter: Ecto.Adapters.Postgres
end
