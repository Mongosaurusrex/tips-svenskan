import api from './index'

export const getTeamsFromLeague = async (
  leagueId: string,
): Promise<{ id: string; name: string; short_name?: string; logo_url?: string }> => {
  return api.get(`/leagues/${leagueId}/teams`)
}

export const getActiveLeague = async () => {
  return api.get("/leagues/active")
}
