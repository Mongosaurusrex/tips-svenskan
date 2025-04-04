<template>
  <div class="max-w-2xl mx-auto p-6">
    <h1 class="text-2xl font-bold mb-4">Din tabell</h1>

    <ul class="bg-brand-midblue divide-y divide-brand-blue rounded-lg overflow-hidden">
      <li
        v-for="(team, index) in teams"
        :key="team.id"
        class="flex items-center gap-3 p-3 hover:bg-brand-blue"
      >
        <span class="w-6 text-right font-bold">{{ index + 1 }}.</span>
        <img v-if="team.logo_url" :src="team.logo_url" alt="logo" class="w-6 h-6 object-contain" />
        <span class="flex-1 px-2">{{ team.name }}</span>
        <!-- drag handle later -->
      </li>
    </ul>

    <button
      class="w-full bg-brand-pink hover:bg-pink-600 py-2 rounded font-bold"
      @click="submitPredictionForm"
    >
      Spara tips
    </button>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { submitPrediction } from '../api/predict'
import { getTeamsFromLeague } from '../api/leagues'
import { useLeagueStore } from '../stores/league'

const leagueStore = useLeagueStore()
const teams = ref([])

onMounted(async () => {
  await leagueStore.loadActiveLeague()

  const teamsRes = await getTeamsFromLeague(leagueStore.activeLeague?.id)
  teams.value = teamsRes.data
})

const submitPredictionForm = async () => {
  const teamIds = teams.value.map((team) => team.id)

  try {
    await submitPrediction(leagueStore.activeLeague?.id, teamIds)
  } catch (err) {
    console.error('❌ Failed to save prediction', err)
  }
}
</script>
