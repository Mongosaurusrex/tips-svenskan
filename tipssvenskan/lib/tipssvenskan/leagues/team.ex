defmodule Tipssvenskan.Leagues.Team do
  use Ecto.Schema
  import Ecto.Changeset

  schema "teams" do
    field :name, :string
    field :short_name, :string
    field :logo_url, :string

    belongs_to :league, Tipssvenskan.Leagues.League

    has_many :prediction_entries, Tipssvenskan.Predictions.PredictionEntry

    timestamps(type: :utc_datetime)
  end

  def changeset(team, attrs) do
    team
    |> cast(attrs, [:name, :short_name, :logo_url, :league_id])
    |> validate_required([:name, :league_id])
    |> unique_constraint([:league_id, :name])
    |> unique_constraint([:league_id, :short_name])
  end
end
