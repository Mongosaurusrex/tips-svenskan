defmodule Tipssvenskan.Repo.Migrations.CreateLeagues do
  use Ecto.Migration

  def change do
    create table(:leagues) do
      add :name, :string
      add :season, :date
      add :lock_date, :date

      timestamps(type: :utc_datetime)
    end

    create index(:leagues, [:season])
    create unique_index(:leagues, [:name, :season])
  end
end
