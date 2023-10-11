<template>
    <div class="flex flex-col items-center">
        <p class="text-center">{{ sliderValue }} - {{ max - sliderValue }}</p>
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
