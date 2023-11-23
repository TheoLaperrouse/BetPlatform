<template>
    <div>
        <h2 class="text-2xl font-semibold text-center p-4">Classement des Joueurs</h2>
        <table class="w-full border-collapse border border-gray-300">
            <thead>
                <tr>
                    <th class="table-cell">Position</th>
                    <th class="table-cell">Joueur</th>
                    <th class="table-cell">Nombre de paris</th>
                    <th class="table-cell">Paris parfaits</th>
                    <th class="table-cell">Paris corrects</th>
                    <th class="table-cell">Paris incorrects</th>
                    <th class="table-cell">Points</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(player, index) in players" :key="player.id" :class="getRowClass(player.id, index)">
                    <td class="table-cell">
                        <span v-if="index < 3" class="pr-2">
                            <font-awesome-icon :icon="faMedal" :class="getMedalColor(index)" />
                        </span>
                        {{ index + 1 }}
                    </td>
                    <td class="table-cell" :class="{ 'font-bold': player.id === currentUser.id }">
                        {{ `${player.first_name} ${player.last_name}` }}
                    </td>
                    <td class="table-cell">{{ player?.bet_count }}</td>
                    <td class="table-cell">{{ player?.perfect_bets }}</td>
                    <td class="table-cell">{{ player?.correct_bets }}</td>
                    <td class="table-cell">{{ player?.incorrect_bets }}</td>
                    <td class="table-cell">{{ player?.points }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faMedal } from '@fortawesome/free-solid-svg-icons';
import { getUsers } from '../services/users.service';

export default {
    data() {
        return {
            players: [],
        };
    },
    components: {
        FontAwesomeIcon,
    },
    async created() {
        this.faMedal = faMedal;
        this.players = await getUsers();
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
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
        getRowClass(playerId, index) {
            return {
                'bg-highlight': playerId === this.currentUser.id,
                'bg-gray-100': playerId !== this.currentUser.id && index % 2 === 0,
            };
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
.bg-highlight {
    background-color: rgba(255, 255, 0, 0.2); /* Jaune avec une opacité de 0.2 (20%) */
}
</style>
