export function getFromLocalStorage(key: string): string | null {
  return localStorage.getItem(key)
}
