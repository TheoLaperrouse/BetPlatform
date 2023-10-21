<template>
    <div
        class="rounded-lg p-4 max-w-[1200px] min-h-[120px]"
        :class="{ 'bg-blue-200': isPlayed, 'bg-gray-200': !isPlayed }"
    >
        <div class="flex flex-col items-center">
            <h2 class="text-center text-lg font-semibold text-black">{{ teamDivision }}</h2>
            <p class="text-center text-black">{{ teams[0] ?? 'Exempt' }} VS {{ teams[1] ?? 'Exempt' }}</p>
            <template v-if="!isPlayed">
                <input type="range" min="0" :max="max" v-model="sliderValue" @input="updateSliderValue" />
                <p class="text-center text-black">{{ sliderValue }} - {{ max - sliderValue }}</p>
            </template>
            <p v-else class="text-center text-black font-bold text-lg">{{ score[0] }} - {{ score[1] }}</p>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        max: {
            type: Number,
            default: 14,
        },
        teams: {
            type: Array,
            default: () => [],
        },
        teamDivision: {
            type: String,
            default: '',
        },
        score: { type: Array, default: () => [] },
    },
    data() {
        return {
            sliderValue: 7,
        };
    },
    computed: {
        isPlayed() {
            return this.score.length === 2;
        },
    },
    methods: {
        updateSliderValue(event) {
            this.sliderValue = event.target.value;
        },
    },
};
</script>
