defmodule TipssvenskanWeb.PredictionEntry do
  use Ecto.Schema
  import Ecto.Changeset

  schema "prediction_entries" do
    field :predicted_position, :integer
    field :prediction_id, :id
    field :team_id, :id

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(prediction_entry, attrs) do
    prediction_entry
    |> cast(attrs, [:predicted_position])
    |> validate_required([:predicted_position])
  end
end
