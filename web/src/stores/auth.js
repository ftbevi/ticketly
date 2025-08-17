// import { defineStore } from 'pinia'
// import jwtDecode from 'jwt-decode'
// import http from '../services/api'

// export const useAuthStore = defineStore('auth', {
//   state: () => ({
//     accessToken: localStorage.getItem('access_token') || null,
//     refreshToken: localStorage.getItem('refresh_token') || null,
//     user: null
//   }),
//   getters: {
//     isAuthenticated: (s) => !!s.accessToken && !isExpired(s.accessToken),
//     email: (s) => s.user?.email || null
//   },
//   actions: {
//     setAccessToken(token) {
//       this.accessToken = token
//       if (token) localStorage.setItem('access_token', token)
//       else localStorage.removeItem('access_token')
//     },
//     setRefreshToken(token) {
//       this.refreshToken = token
//       if (token) localStorage.setItem('refresh_token', token)
//       else localStorage.removeItem('refresh_token')
//     },
//     async login(email, password) {
//       const { data } = await http.post('/auth/login', { email, password })
//       this.setAccessToken(data.access_token)
//       if (data.refresh_token) this.setRefreshToken(data.refresh_token)
//       await this.fetchMe()
//     },
//     async fetchMe() {
//       const { data } = await http.get('/auth/me')
//       this.user = data
//     },
//     logout() {
//       this.user = null
//       this.setAccessToken(null)
//       this.setRefreshToken(null)
//     },
//     async requestReset(email) {
//       await http.post('/auth/request-reset', { email })
//     },
//     async resetPassword(token, password) {
//       await http.post('/auth/reset', { token, password })
//     }
//   }
// })

// function isExpired(token) {
//   try {
//     const { exp } = jwtDecode(token)
//     if (!exp) return false
//     return Date.now() >= exp * 1000
//   } catch {
//     return true
//   }
// }
