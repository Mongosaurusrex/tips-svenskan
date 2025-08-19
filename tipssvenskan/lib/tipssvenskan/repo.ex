defmodule Tipssvenskan.Repo do
  use Ecto.Repo,
    otp_app: :tipssvenskan,
    adapter: Ecto.Adapters.Postgres
end
