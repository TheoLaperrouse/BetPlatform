<template>
    <div class="p-4">
        <h2 class="text-2xl font-semibold text-center p-4">Mes paris ({{ bets.length }})</h2>
        <ul class="grid grid-cols-3 gap-4">
            <li
                v-for="bet in bets"
                :key="bet.id"
                class="p-2 border border-gray-300 rounded-lg py-4"
                :class="statusClass[bet.status] + ' ' + statusTextClass[bet.status]"
            >
                <div class="flex flex-col">
                    <span>{{ getMatch(bet.match_id)?.teams.join(' - ') ?? '' }}</span>
                    <span>Score parié : {{ bet.bet_score.join(' - ') }}</span>
                    <span
                        >Statut : {{ statusText[bet.status] }} ({{
                            formatDate(getMatch(bet.match_id)?.match_date)
                        }})</span
                    >
                    <span>Ajouté le {{ bet.created_at }}</span>
                </div>
            </li>
        </ul>
    </div>
</template>
<script>
import { getMyBets } from '@/services/bets.service.js';
import { getMatches } from '@/services/matchs.service.js';
import { formatDate } from '@/services/date.utils.js';

export default {
    data() {
        return {
            bets: [],
            matchs: [],
        };
    },
    async created() {
        this.statusText = ['Pas joué', 'Faux', 'Correct', 'Parfait'];
        this.statusClass = ['bg-gray-600', 'bg-red-600', 'bg-green-600', 'bg-blue-800'];
        this.statusTextClass = ['text-gray-200', 'text-white', 'text-black', 'text-gray-200'];
        this.bets = await getMyBets();
        this.matchs = await getMatches();
        this.bets.forEach((bet) => {
            bet.created_at = formatDate(bet.created_at);
        });
    },
    methods: {
        getMatch(matchId) {
            return this.matchs.find((match) => match.id === matchId);
        },
        formatDate(date) {
            return formatDate(date);
        },
    },
};
</script>
