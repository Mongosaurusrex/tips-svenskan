defmodule TipssvenskanWeb.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :user_name, :string
    field :email, :string
    field :hashed_password, :string
    field :password, :string, virtual: true

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(user, attrs) do
    user
    |> cast(attrs, [:user_name, :email, :hashed_password])
    |> validate_required([:user_name, :email, :hashed_password])
    |> unique_constraint(:email)
    |> unique_constraint(:user_name)
  end
end
