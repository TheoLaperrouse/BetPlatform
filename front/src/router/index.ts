import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import HomePage from '@/views/HomePage.vue';
import BetsPage from '@/views/BetsPage.vue';
import RankingPage from '@/views/RankingPage.vue';
import SettingsPage from '@/views/SettingsPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';

const routes: Array<RouteRecordRaw> = [
    { path: '/', name: 'Home', component: HomePage },
    { path: '/signin', name: 'Signin', component: LoginPage },
    { path: '/bets', name: 'Bets', component: BetsPage },
    { path: '/ranking', name: 'Ranking', component: RankingPage },
    { path: '/settings', name: 'Settings', component: SettingsPage },
    { path: '/register', name: 'Register', component: RegisterPage },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
