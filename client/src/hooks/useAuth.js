import { createContext, useContext, useMemo, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useLocalStorage } from "@uidotdev/usehooks";
import {
  login as apiLogin,
  signUp as apiSignup,
  keepAlive as apiKeepAlive,
} from "../api/auth";

import axios from "axios";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useLocalStorage("token", null);
  const navigate = useNavigate();

  axios.interceptors.request.use((config) => {
    config.headers = { Authorization: `Bearer ${token}` };
    return config;
  });

  axios.interceptors.response.use(
    (config) => {
      return config;
    },
    (error) => {
      if (error.status === 403) {
        setToken(null);
      }
    }
  );

  const login = async ({ userName, password }) => {
    const { token: tokenFromResponse } = await apiLogin({ userName, password });
    await setToken(tokenFromResponse);
    navigate("/");
  };

  const signUp = async ({ userName, password }) => {
    const { token: tokenFromResponse } = await apiSignup({
      userName,
      password,
    });
    await setToken(tokenFromResponse);
    navigate("/");
  };

  const logout = () => {
    setToken(null);
  };

  const value = useMemo(
    () => ({
      token,
      login,
      logout,
      signUp,
    }),
    [token]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  return useContext(AuthContext);
};
