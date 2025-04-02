import { defineStore } from 'pinia'
import { isTokenExpired } from '../utils/jwt'
import api from '../api'

interface User {
  email: string
}

interface AuthState {
  accessToken: string | null
  refreshToken: string | null
  user: User | null
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => {
    const token = localStorage.getItem('accessToken')
    const refresh = localStorage.getItem('refreshToken')
    const userRaw = localStorage.getItem('user')
    const user = userRaw ? JSON.parse(userRaw) : null

    if (token) {
      api.defaults.headers.common.Authorization = `Bearer ${token}`
    }

    return {
      accessToken: token,
      refreshToken: refresh,
      user: user,
    }
  },

  actions: {
    async login(email: string, password: string) {
      const res = await api.post('/auth/login', { email, password })

      this.accessToken = res.data.access_token
      this.refreshToken = res.data.refresh_token
      this.user = { email }

      localStorage.setItem('accessToken', this.accessToken as string)
      localStorage.setItem('refreshToken', this.refreshToken as string)
      localStorage.setItem('user', JSON.stringify(this.user))

      api.defaults.headers.common.Authorization = `Bearer ${this.accessToken}`
    },

    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.user = null

      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
      localStorage.removeItem('user')

      delete api.defaults.headers.common.Authorization
    },

    async refreshAccessToken() {
      if (!this.refreshToken) {
        this.logout()
        return
      }

      try {
        const res = await api.post('/auth/refresh', {
          refresh_token: this.refreshToken,
        })
        this.accessToken = res.data.access_token
        localStorage.setItem('accessToken', this.accessToken as string)
        api.defaults.headers.common.Authorization = `Bearer ${this.accessToken}`
      } catch (err) {
        console.error('Failed to refresh token', err)
        this.logout()
      }
    },

    async setup() {
      if (this.accessToken && isTokenExpired(this.accessToken)) {
        await this.refreshAccessToken()
      }
    },
  },
})
