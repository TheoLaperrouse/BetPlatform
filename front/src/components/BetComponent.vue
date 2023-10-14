<template>
    <div class="flex flex-col items-center">
        <p class="text-center">{{ teams[0] }} : {{ sliderValue }} - {{ max - sliderValue }} : {{ teams[1] }}</p>
        <input type="range" min="0" :max="max" v-model="sliderValue" @input="updateSliderValue" />
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
