// import axios from 'axios'
// import { useAuthStore } from '../stores/auth'

// const http = axios.create({
//   baseURL: import.meta.env.VITE_API_BASE_URL,
//   timeout: 15000
// })

// // Anexa o Bearer token
// http.interceptors.request.use((config) => {
//   const auth = useAuthStore()
//   if (auth.accessToken) {
//     config.headers.Authorization = `Bearer ${auth.accessToken}`
//   }
//   return config
// })

// // Trata 401/403 e tenta refresh
// let isRefreshing = false
// let queue = []

// function processQueue(error, token = null) {
//   queue.forEach(p => (error ? p.reject(error) : p.resolve(token)))
//   queue = []
// }

// http.interceptors.response.use(
//   (res) => res,
//   async (error) => {
//     const auth = useAuthStore()
//     const original = error.config

//     if ((error.response?.status === 401 || error.response?.status === 403) && !original._retry) {
//       if (!auth.refreshToken) {
//         auth.logout()
//         return Promise.reject(error)
//       }

//       if (isRefreshing) {
//         return new Promise((resolve, reject) => {
//           queue.push({ resolve, reject })
//         }).then((token) => {
//           original.headers.Authorization = `Bearer ${token}`
//           return http(original)
//         })
//       }

//       original._retry = true
//       isRefreshing = true
//       try {
//         const { data } = await axios.post(
//           `${import.meta.env.VITE_API_BASE_URL}/auth/refresh`,
//           { refresh_token: auth.refreshToken }
//         )
//         auth.setAccessToken(data.access_token)
//         processQueue(null, data.access_token)
//         original.headers.Authorization = `Bearer ${data.access_token}`
//         return http(original)
//       } catch (e) {
//         processQueue(e, null)
//         auth.logout()
//         throw e
//       } finally {
//         isRefreshing = false
//       }
//     }
//     return Promise.reject(error)
//   }
// )

// export default http
