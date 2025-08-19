defmodule Tipssvenskan.Predictions.Prediction do
  use Ecto.Schema
  import Ecto.Changeset

  schema "predictions" do
    field :shared_slug, :string

    belongs_to :user, Tipssvenskan.Accounts.User
    belongs_to :league, Tipssvenskan.Leagues.League
    has_many :entries, Tipssvenskan.Predictions.PredictionEntry

    timestamps(type: :utc_datetime)
  end

  def changeset(prediction, attrs) do
    prediction
    |> cast(attrs, [:shared_slug, :user_id, :league_id])
    |> validate_required([:shared_slug, :user_id, :league_id])
    |> unique_constraint(:shared_slug)
    |> unique_constraint([:user_id, :league_id])
  end
end
