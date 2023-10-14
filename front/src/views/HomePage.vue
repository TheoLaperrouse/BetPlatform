<template>
    <div class="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center">
        <BetComponent :teams="['Thorigné', 'Cesson']" />
    </div>
</template>

<script>
import BetComponent from '@/components/BetComponent.vue';

export default {
    components: {
        BetComponent,
    },
};
</script>
