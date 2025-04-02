import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import Predict from './views/Predict.vue'
import { useAuthStore } from './stores/auth'

const routes = [
  { path: '/', redirect: '/predict' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  {
    path: '/predict',
    component: Predict,
    meta: { requiresAuth: true },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()

  if (to.meta.requiresAuth && !auth.accessToken) {
    next('/login')
  } else if (to.path === '/login' && auth.accessToken) {
    next('/predict') // already logged in, redirect away from login
  } else {
    next()
  }
})

export default router
