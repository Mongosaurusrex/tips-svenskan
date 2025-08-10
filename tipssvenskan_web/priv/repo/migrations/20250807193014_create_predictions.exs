defmodule TipssvenskanWeb.Repo.Migrations.CreatePredictions do
  use Ecto.Migration

  def change do
    create table(:predictions) do
      add :shared_slug, :string
      add :user_id, references(:users, on_delete: :nothing)
      add :league_id, references(:leagues, on_delete: :nothing)

      timestamps(type: :utc_datetime)
    end

    create index(:predictions, [:user_id])
    create index(:predictions, [:league_id])
    create unique_index(:predictions, [:shared_slug])
  end
end
