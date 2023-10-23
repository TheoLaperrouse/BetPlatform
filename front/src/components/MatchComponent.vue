<template>
    <div
        class="rounded-lg p-4 max-w-[1200px] min-h-[120px]"
        :class="{ 'bg-blue-200': isPlayed, 'bg-gray-200': !isPlayed }"
    >
        <div class="flex flex-col items-center">
            <p class="text-center text-black">{{ match.teams[0] ?? 'Exempt' }} VS {{ match.teams[1] ?? 'Exempt' }}</p>
            <template v-if="!isPlayed">
                <input type="range" min="0" :max="max" v-model="sliderValue" @input="updateSliderValue" />
                <p class="text-center text-black">{{ betScore[0] }} - {{ betScore[1] }}</p>
                <button @click="sendBet" class="bg-blue-500 hover-bg-blue-700 text-white font-semibold px-2 rounded">
                    Mettre à jour mon pari
                </button>
            </template>
            <p v-else class="text-center text-black font-bold text-lg">{{ match.score[0] }} - {{ match.score[1] }}</p>
        </div>
    </div>
</template>

<script>
import { sendBet } from '@/services/bets.service.js';

export default {
    props: {
        max: {
            type: Number,
            default: 14,
        },
        match: { type: Object },
    },
    data() {
        return {
            sliderValue: 7,
        };
    },
    computed: {
        isPlayed() {
            return this.match.score.length === 2;
        },
        betScore() {
            return [this.sliderValue, this.max - this.sliderValue];
        },
    },
    methods: {
        updateSliderValue(event) {
            this.sliderValue = event.target.value;
        },
        async sendBet() {
            await sendBet({ match_id: this.match.id, bet_score: this.betScore });
        },
    },
};
</script>
