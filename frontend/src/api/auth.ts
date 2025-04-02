import api from './index'

export async function loginUser(email: string, password: string) {
  return api.post('/auth/login', { email, password })
}

export async function registerUser(email: string, password: string) {
  return api.post('/auth/register', { email, password })
}
