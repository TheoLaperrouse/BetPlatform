<template>
    <div
        class="rounded-lg p-4 max-w-[1200px] min-h-[145px]"
        :class="{ 'bg-blue-200': isPlayed, 'bg-gray-200': !isPlayed }"
    >
        <div class="flex flex-col items-center">
            <p class="text-center text-black">{{ match.teams[0] ?? 'Exempt' }} VS {{ match.teams[1] ?? 'Exempt' }}</p>
            <div class="text-center text-black">{{ formattedDate }}</div>
            <template v-if="!isPlayed">
                <div class="flex items-center justify-center">
                    <input
                        type="number"
                        min="0"
                        :max="3"
                        v-model="betScore[0]"
                        @input="isModified = true"
                        class="text-center text-black rounded p-1 m-1"
                    />
                    <span class="mx-2">-</span>
                    <input
                        type="number"
                        min="0"
                        :max="3"
                        v-model="betScore[1]"
                        @input="isModified = true"
                        class="text-center text-black rounded p-1 m-1"
                    />
                </div>
                <div v-if="isModificationOver" class="text-red-500">Pari fermé! Match dans - de 48h</div>
                <button
                    v-else
                    @click="sendBet"
                    :class="[
                        'bg-blue-500 hover:bg-blue-700 text-white font-semibold px-2 rounded',
                        { 'opacity-50 cursor-not-allowed': !isBetValid || !isModified },
                    ]"
                    :disabled="!isBetValid || !isModified"
                >
                    Mettre à jour mon pari
                </button>
            </template>
            <p v-else class="text-center text-black font-bold text-lg">{{ match.score[0] }} - {{ match.score[1] }}</p>
        </div>
    </div>
</template>

<script>
import { sendBet, updateBet } from '@/services/bets.service.js';
import { formatDate } from '@/services/date.utils.js';
import moment from 'moment/min/moment-with-locales';

export default {
    props: {
        max: {
            type: Number,
            default: 14,
        },
        match: { type: Object },
        bet: { type: Object, default: null },
    },
    data() {
        return {
            betScore: [0, 0],
            isSended: false,
            isModified: false,
        };
    },
    mounted() {
        if (this.bet) {
            this.betScore = this.bet?.bet_score ?? [0, 0];
        }
    },
    computed: {
        isPlayed() {
            return this.match.score.length === 2;
        },
        isBetValid() {
            return (this.betScore[0] === 3 && this.betScore[1] < 3) || (this.betScore[0] < 3 && this.betScore[1] === 3);
        },
        isModificationOver() {
            const date = this.match?.match_date;
            if (!date) {
                return true;
            }
            const matchDate = moment(date);
            const currentDate = moment();
            return matchDate.diff(currentDate, 'days') <= 1;
        },
        formattedDate() {
            return formatDate(this.match.match_date);
        },
    },
    methods: {
        async sendBet() {
            this.isModified = false;
            if (this.bet) {
                return updateBet(this.bet.id, this.betScore);
            }
            return sendBet({ match_id: this.match.id, bet_score: this.betScore });
        },
    },
};
</script>
