<template>
  <div class="flex justify-center items-center bg-brand-blue text-white">
    <div class="w-full max-w-sm p-8 bg-brand-midblue rounded shadow-lg">
      <h2 class="text-2xl font-bold mb-6 text-center">Logga in</h2>

      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block mb-1">E-post</label>
          <input
            v-model="email"
            type="email"
            class="w-full p-2 rounded text-black"
            @input="clearError"
          />
        </div>
        <div>
          <label class="block mb-1">Lösenord</label>
          <input
            v-model="password"
            type="password"
            class="w-full p-2 rounded text-black"
            @input="clearError"
          />
        </div>

        <p v-if="errorMessage" class="text-sm text-red-400">{{ errorMessage }}</p>

        <button
          type="submit"
          class="w-full bg-brand-pink hover:bg-pink-600 py-2 rounded font-bold disabled:opacity-50 disabled:cursor-not-allowed"
          :disabled="!email || !password"
        >
          Logga in
        </button>
        <p class="text-sm text-center mt-4">
          Har du inget konto?
          <router-link to="/register" class="text-brand-pink underline hover:opacity-80">
            Skapa ett här
          </router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

const email = ref('')
const password = ref('')
const errorMessage = ref(null)

const handleLogin = async () => {
  errorMessage.value = null

  try {
    await auth.login(email.value, password.value)
    router.push('/predict')
  } catch (err) {
    if (err.response?.status === 401) {
      errorMessage.value = 'Fel e-post eller lösenord.'
    } else {
      errorMessage.value = 'Något gick fel. Försök igen.'
    }
  }
}

const clearError = () => {
  errorMessage.value = null
}
</script>
