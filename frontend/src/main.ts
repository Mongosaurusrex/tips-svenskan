import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import './assets/main.css'

import App from './App.vue'

import { useAuthStore } from './stores/auth'

const setup = ()=> {
  const auth = useAuthStore()
  auth.setup()
}

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
