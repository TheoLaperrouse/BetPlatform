<template>
    <div class="flex-col justify-center items-center h-screen p-10">
        <h2 class="text-2xl font-semibold mb-4 text-center">Les Matchs</h2>
        <div class="mb-4 text-lg font-semibold mb-2 text-center">
            <label for="matchDay">
                <h3 class="">Journée {{ selectedMatchDay }}</h3>
            </label>
            <input type="range" id="matchDay" v-model="selectedMatchDay" min="1" max="18" class="w-[300px] mt-1" />
        </div>
        <div v-if="selectedMatchDay">
            <ul class="grid grid-cols-3 gap-4">
                <li v-for="(match, index) in matchesByDay[selectedMatchDay]" :key="index">
                    <MatchComponent :match="match" :bet="betByMatchId[match.id]" :key="selectedMatchDay" />
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import MatchComponent from '@/components/MatchComponent.vue';
import { getMatches } from '@/services/matchs.service.js';
import { getMyBets } from '@/services/bets.service.js';
import { groupBy, keyBy } from 'lodash';

export default {
    components: {
        MatchComponent,
    },
    data() {
        return {
            selectedMatchDay: 1,
            matches: {},
            bets: [],
        };
    },
    async created() {
        this.matches = await getMatches();
        this.bets = await getMyBets();
    },
    computed: {
        matchesByDay() {
            return groupBy(this.matches, 'match_day');
        },
        betByMatchId() {
            return keyBy(this.bets, 'match_id');
        },
    },
};
</script>
