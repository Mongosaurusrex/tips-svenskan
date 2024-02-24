import axios from "axios";

export const getThisSeasonsTeams = async () => {
  const response = await axios.get("http://localhost:8000/teams");
  return response.data;
};
