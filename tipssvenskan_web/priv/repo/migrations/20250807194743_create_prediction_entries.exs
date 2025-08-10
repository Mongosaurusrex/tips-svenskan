defmodule TipssvenskanWeb.Repo.Migrations.CreatePredictionEntries do
  use Ecto.Migration

  def change do
    create table(:prediction_entries) do
      add :predicted_position, :integer
      add :prediction_id, references(:predictions, on_delete: :nothing)
      add :team_id, references(:teams, on_delete: :nothing)

      timestamps(type: :utc_datetime)
    end

    create index(:prediction_entries, [:prediction_id])
    create index(:prediction_entries, [:team_id])
  end
end
