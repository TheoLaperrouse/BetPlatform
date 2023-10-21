<template>
    <div class="flex-col justify-center items-center h-screen p-10">
        <h2 class="text-2xl font-semibold mb-4 text-center">Les Paris</h2>
        <div class="mb-4 text-lg font-semibold mb-2 text-center">
            <label for="matchDay">
                <h3 class="">Journée {{ selectedMatchDay }}</h3>
            </label>
            <input type="range" id="matchDay" v-model="selectedMatchDay" min="1" max="7" class="w-[300px] mt-1" />
        </div>
        <div v-if="selectedMatchDay">
            <ul class="grid grid-cols-3 gap-4">
                <li v-for="(bet, index) in matchesByDay[selectedMatchDay]" :key="index">
                    <BetComponent :teams="bet.teams" :team-division="bet.teamDivision" :score="bet.score" />
                </li>
            </ul>
        </div>
        <div class="mt-4 flex justify-center">
            <button class="bg-blue-500 hover-bg-blue-700 text-white font-semibold py-2 px-4 rounded">
                Mettre à jour mes paris
            </button>
        </div>
    </div>
</template>

<script>
import BetComponent from '@/components/BetComponent.vue';
import { getMatches } from '@/services/matchs.service.js';
import { groupBy } from 'lodash';

export default {
    components: {
        BetComponent,
    },
    data() {
        return {
            selectedMatchDay: 1,
            matches: {},
        };
    },
    async created() {
        this.matches = await getMatches();
    },
    computed: {
        matchesByDay() {
            return groupBy(this.matches, 'match_day');
        },
    },
};
</script>
