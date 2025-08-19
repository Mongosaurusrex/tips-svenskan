defmodule Tipssvenskan.Predictions.PredictionEntry do
  use Ecto.Schema
  import Ecto.Changeset

  schema "prediction_entries" do
    field :predicted_position, :integer

    belongs_to :prediction, Tipssvenskan.Predictions.Prediction
    belongs_to :team, Tipssvenskan.Leagues.Team

    timestamps(type: :utc_datetime)
  end

  def changeset(entry, attrs) do
    entry
    |> cast(attrs, [:predicted_position, :prediction_id, :team_id])
    |> validate_required([:predicted_position, :prediction_id, :team_id])
    |> validate_number(:predicted_position, greater_than: 0)
    |> unique_constraint([:prediction_id, :team_id])
    |> unique_constraint([:prediction_id, :predicted_position])
    |> foreign_key_constraint(:team_id)
    |> foreign_key_constraint(:prediction_id)
  end
end
