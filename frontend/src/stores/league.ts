import { defineStore } from 'pinia'
import { ref } from 'vue'
import { getActiveLeague } from '../api/leagues'

interface League {
  id: string
  name: string
  season: string
  lock_date: string
}

export const useLeagueStore = defineStore('league', () => {
  const activeLeague = ref<League | null>(null)

  async function loadActiveLeague() {
    const res = await getActiveLeague()
    activeLeague.value = res.data
  }

  return {
    activeLeague,
    loadActiveLeague,
  }
})
