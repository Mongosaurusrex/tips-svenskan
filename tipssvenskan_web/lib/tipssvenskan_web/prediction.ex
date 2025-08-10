defmodule TipssvenskanWeb.Prediction do
  use Ecto.Schema
  import Ecto.Changeset

  schema "predictions" do
    field :shared_slug, :string

    belongs_to :user, TipssvenskanWeb.User
    belongs_to :league, TipssvenskanWeb.League

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(prediction, attrs) do
    prediction
    |> cast(attrs, [:shared_slug, :user_id, :league_id])
    |> validate_required([:shared_slug, :user_id, :league_id])
    |> unique_constraint(:shared_slug)
  end
end
