<template>
    <div class="p-4">
        <h2 class="text-2xl font-semibold text-center p-4">Mes paris</h2>
        <ul>
            <li
                v-for="bet in bets"
                :key="bet.id"
                class="mb-2 p-2 border border-gray-300 rounded-lg py-4"
                :class="statusClass[bet.status] + ' ' + statusTextClass[bet.status]"
            >
                <div class="flex flex-col">
                    <span>{{ getMatch(bet.match_id)?.teams.join(' - ') ?? '' }}</span>
                    <span>Score parié : {{ bet.bet_score.join(' - ') }}</span>
                    <span>Statut : {{ statusText[bet.status] }}</span>
                    <span>Ajouté le {{ bet.created_at }}</span>
                </div>
            </li>
        </ul>
    </div>
</template>
<script>
import { getMyBets } from '@/services/bets.service.js';
import { getMatches } from '@/services/matchs.service.js';
import { format } from 'date-fns';

export default {
    data() {
        return {
            bets: [],
            matchs: [],
        };
    },
    async created() {
        this.statusText = ['Pas joué', 'Faux', 'Correct', 'Parfait'];
        this.statusClass = ['bg-gray-600', 'bg-red-600', 'bg-green-600', 'bg-blue-600'];
        this.statusTextClass = ['text-white', 'text-white', 'text-black', 'text-white'];
        this.bets = await getMyBets();
        this.matchs = await getMatches();
        this.bets.forEach((bet) => {
            bet.created_at = format(new Date(bet.created_at), 'dd/MM/yyyy');
        });
    },
    methods: {
        getMatch(matchId) {
            return this.matchs.find((match) => match.id === matchId);
        },
    },
};
</script>
