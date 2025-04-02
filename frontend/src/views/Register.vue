<template>
  <div class="flex justify-center items-center h-full min-h-screen">
    <div class="w-full max-w-sm p-8 bg-brand-midblue rounded shadow-lg text-white">
      <h2 class="text-2xl font-bold mb-6 text-center">Skapa konto</h2>

      <form @submit.prevent="handleRegister" class="space-y-4">
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
          class="w-full bg-brand-pink hover:bg-pink-600 py-2 rounded font-bold disabled:opacity-50 disabled:opacity-50 disabled:cursor-not-allowed"
          :disabled="!email || !password"
        >
          Skapa konto
        </button>
        <p class="text-sm text-center mt-4">
          Redan medlem?
          <router-link to="/login" class="text-brand-pink underline hover:opacity-80">
            Logga in här
          </router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { registerUser } from '../api/auth'

const email = ref('')
const password = ref('')
const errorMessage = ref<string | null>(null)

const router = useRouter()
const auth = useAuthStore()

const handleRegister = async () => {
  errorMessage.value = null

  try {
    await registerUser(email.value, password.value)
    await auth.login(email.value, password.value)
    router.push('/predict')
  } catch (err: any) {
    if (err.response?.status === 409) {
      errorMessage.value = 'E-postadressen är redan registrerad.'
    } else {
      errorMessage.value = 'Något gick fel. Försök igen.'
    }
  }
}

const clearError = () => {
  errorMessage.value = null
}
</script>
