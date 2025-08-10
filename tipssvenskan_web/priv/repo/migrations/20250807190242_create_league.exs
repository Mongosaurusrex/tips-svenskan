defmodule TipssvenskanWeb.Repo.Migrations.CreateLeague do
  use Ecto.Migration

  def change do
    create table(:leagues) do
      add :name, :string
      add :season, :date
      add :lock_date, :date

      timestamps(type: :utc_datetime)
    end
  end
end
