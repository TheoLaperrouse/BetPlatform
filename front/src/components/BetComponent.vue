<template>
    <div class="bg-white rounded-lg p-4 m-4 min-w-[300px]">
        <div class="flex flex-col items-center">
            <h2 class="text-center text-lg font-semibold text-black">{{ teamDivision }}</h2>
            <p class="text-center text-black">
                {{ teams[0] }} : {{ sliderValue }} - {{ max - sliderValue }} : {{ teams[1] }}
            </p>
            <input type="range" min="0" :max="max" v-model="sliderValue" @input="updateSliderValue" />
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
    },
    data() {
        return {
            sliderValue: this.max,
        };
    },
    methods: {
        updateSliderValue(event) {
            this.sliderValue = event.target.value;
        },
    },
};
</script>
