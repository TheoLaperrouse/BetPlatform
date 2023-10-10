<template>
    <div class="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center">
        <BetSlider class="w-full"></BetSlider>
    </div>
</template>
<script>
import BetSlider from '@/components/BetSlider.vue';

export default {
    components: {
        BetSlider,
    },
};
</script>
