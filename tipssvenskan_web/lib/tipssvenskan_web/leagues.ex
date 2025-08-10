defmodule TipssvenskanWeb.League do
  use Ecto.Schema
  import Ecto.Changeset

  schema "leagues" do
    field :name, :string
    field :season, :date
    field :lock_date, :date

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(league, attrs) do
    league
    |> cast(attrs, [:name, :season, :lock_date])
    |> validate_required([:name, :season, :lock_date])
  end
end
