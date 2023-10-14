<template>
    <div>
        <h2 class="text-2xl font-semibold mb-4">Paris à venir</h2>
        <div class="mb-4">
            <label for="matchDay" class="block text-gray-600 font-medium text-sm">Sélectionner la journée</label>
            <input type="range" id="matchDay" v-model="selectedMatchDay" min="1" max="7" class="w-full mt-1" />
        </div>
        <div v-if="selectedMatchDay">
            <h3 class="text-lg font-semibold mb-2">Journée {{ selectedMatchDay }}</h3>
            <ul>
                <li v-for="(bet, index) in upcomingBets[selectedMatchDay - 1]" :key="index">
                    <BetComponent :teamNames="bet.teams" :betAmount="bet.amount" />
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import BetComponent from '@/components/BetComponent.vue';

export default {
    components: {
        BetComponent,
    },
    props: {
        upcomingBets: {
            type: Array,
            default: () => [],
        },
    },
    data() {
        return {
            selectedMatchDay: 1,
        };
    },
};
</script>
