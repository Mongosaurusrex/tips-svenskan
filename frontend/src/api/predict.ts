import api from './index'

export const submitPrediction = (
  league_id: string,
  team_ids: string[],
): Promise<{ message: string; prediction_id: string }> => {
  return api.post('/predictions/predict', { league_id, team_ids })
}

export const getLoggedInUsersPrediction = (leagueId: string) => {
  return api.get(`/predictions/${leagueId}`)
}
