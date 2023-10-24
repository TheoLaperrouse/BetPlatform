<template>
    <div class="p-4">
        <h2 class="text-2xl font-semibold text-center p-4">Mes paris</h2>
        <ul>
            <li
                v-for="bet in bets"
                :key="bet.id"
                class="mb-2 p-2 border border-gray-300 rounded-lg py-4"
                :class="statusClass[bet.status]"
            >
                {{ bet.bet_score }} - Statut :
                <span :class="statusTextClass[bet.status]">{{ statusText[bet.status] }}</span>
            </li>
        </ul>
    </div>
</template>

<script>
import { getMyBets } from '@/services/bets.service.js';

export default {
    data() {
        return {
            bets: [],
        };
    },
    async created() {
        this.statusText = ['Pas joué', 'Faux', 'Correct', 'Parfait'];
        this.statusClass = ['bg-gray-600', 'bg-red-600', 'bg-green-600', 'bg-blue-600'];
        this.statusTextClass = ['text-white', 'text-white', 'text-black', 'text-white'];
        this.bets = await getMyBets();
    },
};
</script>
