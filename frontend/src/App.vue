<template>
  <div class="flex justify-center items-center min-h-screen bg-brand-blue text-white">
    <div class="w-full max-w-sm p-8 bg-brand-midblue rounded shadow-lg">
      <h2 class="text-2xl font-bold mb-6 text-center">Logga in</h2>
      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block mb-1">E-post</label>
          <input v-model="email" type="email" class="w-full p-2 rounded text-black" />
        </div>
        <div>
          <label class="block mb-1">Lösenord</label>
          <input v-model="password" type="password" class="w-full p-2 rounded text-black" />
        </div>
        <button type="submit" class="w-full bg-brand-pink hover:bg-pink-600 py-2 rounded font-bold">
          Logga in
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { loginUser } from './api/auth'

const email = ref('')
const password = ref('')

const handleLogin = async () => {
  try {
    const res = await loginUser(email.value, password.value)
    console.log('✅ Login success:', res.data)
  } catch (err) {
    console.error('❌ Login failed:', err.response?.data || err)
  }
}
</script>
