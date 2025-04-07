<template>
  <div class="max-w-2xl mx-auto p-6">
    <h1 class="text-2xl font-bold mb-4">Din tabell</h1>

    <draggable
      v-model="teams"
      item-key="id"
      tag="ul"
      class="bg-brand-midblue divide-y divide-brand-blue rounded-lg overflow-hidden"
    >
      <template #item="{ element: team, index }">
        <li class="flex items-center gap-3 p-3 hover:bg-brand-blue">
          <span class="w-6 text-right font-bold">{{ index + 1 }}.</span>
          <img
            v-if="team.logo_url"
            :src="team.logo_url"
            alt="logo"
            class="w-6 h-6 object-contain"
          />
          <span class="flex-1 px-2">{{ team.name }}</span>
          <span class="cursor-move text-sm opacity-50">⠿</span>
        </li>
      </template>
    </draggable>

    <button
      v-if="!prediction"
      :disabled="buttonState === 'submitted'"
      :class="[
        'w-full py-2 rounded font-bold transition',
        buttonState === 'idle' && 'bg-brand-pink hover:bg-pink-600',
        buttonState === 'confirming' && 'bg-yellow-500 hover:bg-yellow-600',
        buttonState === 'submitted' && 'bg-green-600 cursor-default'
      ]"
      @click="handleSubmit"
    >
      {{
        buttonState === 'idle'
          ? 'Spara tips'
          : buttonState === 'confirming'
          ? 'Är du säker?'
          : 'Tack för ditt tips!'
      }}
    </button>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { submitPrediction, getLoggedInUsersPrediction } from '../api/predict'
import { getTeamsFromLeague } from '../api/leagues'
import { useLeagueStore } from '../stores/league'
import draggable from 'vuedraggable'

const leagueStore = useLeagueStore()
const teams = ref([])
const prediction = ref<Prediction | null>(null)

const buttonState = ref<'idle' | 'confirming' | 'submitted'>('idle')

onMounted(async () => {
  await leagueStore.loadActiveLeague()

  try {
    const res = await getLoggedInUsersPrediction(leagueStore.activeLeague?.id)
    prediction.value = res.data

    const entryTeamIds = res.data.entries
      .sort((a, b) => a.predicted_position - b.predicted_position)
      .map((entry) => entry.team_id)

    const teamsRes = await getTeamsFromLeague(leagueStore.activeLeague?.id)
    const fullTeams = teamsRes.data

    teams.value = entryTeamIds.map((id) => fullTeams.find((t) => t.id === id)).filter(Boolean)
  } catch (err: any) {
    if (err.response?.status === 404) {
      const teamsRes = await getTeamsFromLeague(leagueStore.activeLeague?.id)
      teams.value = teamsRes.data
    } else {
      console.error('Error loading prediction', err)
    }
  }
})

const handleSubmit = async () => {
  if (buttonState.value === 'idle') {
    buttonState.value = 'confirming'
    return
  }

  if (buttonState.value === 'confirming') {
    const teamIds = teams.value.map((team) => team.id)

    try {
      await submitPrediction(leagueStore.activeLeague?.id, teamIds)
      buttonState.value = 'submitted'
    } catch (err) {
      console.error('❌ Failed to save prediction', err)
      buttonState.value = 'idle'
    }
  }
}
</script>
