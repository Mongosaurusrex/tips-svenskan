defmodule TipssvenskanWeb.Team do
  use Ecto.Schema
  import Ecto.Changeset

  schema "teams" do
    field :name, :string
    field :short_name, :string
    field :logo_url, :string
    field :league_id, :id

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(team, attrs) do
    team
    |> cast(attrs, [:name, :short_name, :logo_url])
    |> validate_required([:name, :short_name, :logo_url])
  end
end
