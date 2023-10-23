import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import HomePage from '@/views/HomePage.vue';
import MatchPages from '@/views/MatchPages.vue';
import RankingPage from '@/views/RankingPage.vue';
import SettingsPage from '@/views/SettingsPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';

const routes: Array<RouteRecordRaw> = [
    { path: '/', name: 'Home', component: HomePage },
    { path: '/signin', name: 'Signin', component: LoginPage },
    { path: '/matchs', name: 'Matchs', component: MatchPages },
    { path: '/ranking', name: 'Ranking', component: RankingPage },
    { path: '/settings', name: 'Settings', component: SettingsPage },
    { path: '/register', name: 'Register', component: RegisterPage },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const publicPages = ['/signin', '/register'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('jwtToken');
    if (authRequired && !loggedIn) {
        next('/signin');
    } else {
        next();
    }
});

export default router;
