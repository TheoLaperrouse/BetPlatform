<template>
    <div id="app" class="flex">
        <template v-if="isAppRoute">
            <MenuPanel class="min-w-[250px]" />
        </template>
        <router-view class="flex-auto" />
    </div>
</template>

<script>
import MenuPanel from '@/components/MenuPanel.vue';
export default {
    components: {
        MenuPanel,
    },
    computed: {
        isAppRoute() {
            return !['Signin', 'Register'].includes(this.$route.name);
        },
    },
};
</script>
