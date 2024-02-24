import axios from "axios";

export async function login({ userName, password }) {
  const response = await axios.post("http://localhost:8000/auth/login", {
    user_name: userName,
    password,
  });

  return response.data;
}

export async function signUp({ userName, password }) {
  const response = await axios.post("http://localhost:8000/auth/signup", {
    user_name: userName,
    password,
  });

  return response.data;
}
