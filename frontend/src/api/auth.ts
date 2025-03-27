import api from './index'

export async function loginUser(email, password) {
  return api.post('/auth/login', { email, password })
}
