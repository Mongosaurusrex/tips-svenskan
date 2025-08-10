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
    |> cast(attrs, [:user_name, :email, :password])
    |> validate_required([:user_name, :email, :password])
    |> validate_format(:email, ~r/@/)
    |> unique_constraint(:email)
    |> unique_constraint(:user_name)
    |> put_pass_hash()
  end

  defp put_pass_hash(%Ecto.Changeset{valid?: true, changes: %{password: pw}} = changeset) do
    change(changeset, hashed_password: Bcrypt.hash_pwd_salt(pw))
  end

  defp put_pass_hash(changeset), do: changeset
end
