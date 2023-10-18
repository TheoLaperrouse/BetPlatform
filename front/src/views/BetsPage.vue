<template>
    <div class="flex justify-center items-center h-screen">
        <div class="w-[400px] bg-gray-100 rounded-lg p-4 m-4 shadow-md hover:shadow-lg text-center">
            <h2 class="text-2xl font-semibold mb-4">Les Paris</h2>
            <div class="mb-4">
                <label for="matchDay">
                    <h3 class="text-lg font-semibold mb-2">Journée {{ selectedMatchDay }}</h3>
                </label>
                <input type="range" id="matchDay" v-model="selectedMatchDay" min="1" max="7" class="w-full mt-1" />
            </div>
            <div v-if="selectedMatchDay">
                <ul>
                    <li v-for="(bet, index) in upcomingBets[selectedMatchDay - 1]" :key="index">
                        <BetComponent :teams="bet.teams" :team-division="bet.teamDivision" />
                    </li>
                </ul>
            </div>
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded mt-4">
                Mettre à jour mes paris
            </button>
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
            default: () => [
                [
                    { teams: ['Thorigné', 'Rennes CPB'], teamDivision: 'Régionale 2' },
                    { teams: ['Thorigné', 'Cesson'], teamDivision: 'Départementale 1' },
                ],
            ],
        },
    },
    data() {
        return {
            selectedMatchDay: 1,
        };
    },
};
</script>
