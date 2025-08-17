import { createRouter, createWebHistory } from 'vue-router'
//import { useAuthStore } from '../stores/auth'

import Login from '../pages/Login.vue'
import RequestReset from '../pages/RequestReset.vue'
import ResetPassword from '../pages/ResetPassword.vue'
import Dashboard from '../pages/Dashboard.vue'

const routes = [
  { path: '/login', name: 'login', component: Login, meta: { guestOnly: true } },
  { path: '/reset', name: 'request-reset', component: RequestReset, meta: { guestOnly: true } },
  { path: '/reset/:token', name: 'reset-password', component: ResetPassword, props: true, meta: { guestOnly: true } },
  { path: '/', name: 'dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', redirect: '/' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// router.beforeEach(async (to) => {
//   const auth = useAuthStore()

//   if (to.meta.requiresAuth && !auth.isAuthenticated) {
//     return { name: 'login', query: { redirect: to.fullPath } }
//   }

//   if (to.meta.guestOnly && auth.isAuthenticated) {
//     return { name: 'dashboard' }
//   }
// })

export default router
