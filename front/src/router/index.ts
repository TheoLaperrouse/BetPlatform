import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import HomePage from '@/views/HomePage.vue';
import BetsPage from '@/views/BetsPage.vue';
import RankingPage from '@/views/RankingPage.vue';

const routes: Array<RouteRecordRaw> = [
    { path: '/', component: HomePage },
    { path: '/signin', component: LoginPage },
    { path: '/bets', component: BetsPage },
    { path: '/ranking', component: RankingPage },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
