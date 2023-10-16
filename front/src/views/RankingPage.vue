<template>
    <div>
        <h2 class="text-2xl font-semibold text-center p-4">Classement des Joueurs</h2>
        <table class="w-full border-collapse border border-gray-300">
            <thead>
                <tr>
                    <th class="table-cell">Position</th>
                    <th class="table-cell">Joueur</th>
                    <th class="table-cell">Paris Parfaits</th>
                    <th class="table-cell">Paris Corrects</th>
                    <th class="table-cell">Points</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(player, index) in players" :key="player.id" :class="index % 2 === 0 ? 'bg-gray-100' : ''">
                    <td class="table-cell">
                        <span v-if="index < 3" class="pr-2">
                            <font-awesome-icon :icon="faMedal" :class="getMedalColor(index)" />
                        </span>
                        {{ index + 1 }}
                    </td>
                    <td class="table-cell">{{ player.name }}</td>
                    <td class="table-cell">{{ player.perfectBets }}</td>
                    <td class="table-cell">{{ player.correctBets }}</td>
                    <td class="table-cell">{{ player.points }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faMedal } from '@fortawesome/free-solid-svg-icons';

export default {
    data() {
        return {
            players: [
                { id: '1', name: 'Théo Laperrouse', points: 5, perfectBets: 1, correctBets: 2 },
                { id: '2', name: 'A', points: 4, perfectBets: 1, correctBets: 2 },
                { id: '3', name: 'B', points: 3, perfectBets: 1, correctBets: 2 },
                { id: '4', name: 'C', points: 2, perfectBets: 1, correctBets: 2 },
                { id: '5', name: 'D', points: 1, perfectBets: 1, correctBets: 2 },
            ],
        }; // TO DELETE
    },
    components: {
        FontAwesomeIcon,
    },
    created() {
        this.faMedal = faMedal;
    },
    methods: {
        getMedalColor(index) {
            switch (index) {
                case 0:
                    return 'text-yellow-500';
                case 1:
                    return 'text-gray-400';
                case 2:
                    return 'text-yellow-600';
                default:
                    return 'text-black';
            }
        },
    },
};
</script>
<style scoped>
.table-cell {
    padding: 0.75rem;
    border: 1px solid #e5e7eb;
    text-align: center;
}
</style>
