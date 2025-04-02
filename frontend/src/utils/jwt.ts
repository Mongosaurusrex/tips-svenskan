export function isTokenExpired(token: string): boolean {
  try {
    const payload = JSON.parse(atob(token.split('.')[1]))
    const now = Math.floor(Date.now() / 1000)
    return payload.exp && payload.exp < now
  } catch (e) {
    console.error('Failed to decode JWT', e)
    return true
  }
}
