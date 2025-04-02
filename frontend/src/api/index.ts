import axios from 'axios'

import { useAuthStore } from '../stores/auth'

const api = axios.create({
  baseURL: 'http://localhost:8000',
})

api.interceptors.response.use(
  (res) => res,
  async (err) => {
    const auth = useAuthStore()

    if (err.response?.status === 401 && auth.refreshToken) {
      await auth.refreshAccessToken()

      err.config.headers.Authorization = `Bearer ${auth.accessToken}`
      return api(err.config)
    }

    return Promise.reject(err)
  },
)

export default api
