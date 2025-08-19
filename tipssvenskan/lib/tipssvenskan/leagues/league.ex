defmodule Tipssvenskan.Leagues.League do
  use Ecto.Schema
  import Ecto.Changeset

  schema "leagues" do
    field :name, :string
    field :season, :date
    field :lock_date, :date

    has_many :teams, Tipssvenskan.Leagues.Team
    has_many :predictions, Tipssvenskan.Predictions.Prediction

    timestamps(type: :utc_datetime)
  end

  def changeset(league, attrs) do
    league
    |> cast(attrs, [:name, :season, :lock_date])
    |> validate_required([:name, :season, :lock_date])
    |> unique_constraint([:name, :season])
  end
end
