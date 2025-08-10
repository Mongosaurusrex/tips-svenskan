defmodule TipssvenskanWeb.Repo.Migrations.CreateTeams do
  use Ecto.Migration

  def change do
    create table(:teams) do
      add :name, :string
      add :short_name, :string
      add :logo_url, :string
      add :league_id, references(:leagues, on_delete: :nothing)

      timestamps(type: :utc_datetime)
    end

    create index(:teams, [:league_id])
  end
end
