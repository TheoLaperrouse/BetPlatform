<template>
    <div class="menu bg-gray-800 text-white min-h-screen">
        <ul class="fixed list-none p-0 mt-4">
            <li class="py-4 ml-6" v-for="(link, index) in menuLinks" :key="index">
                <router-link
                    :class="{ 'text-indigo-400': $route.path === link.to }"
                    :to="link.to"
                    class="flex items-center"
                >
                    <font-awesome-icon :icon="link.icon" class="mr-2" />
                    <span :title="link.text">{{ link.text }}</span>
                </router-link>
            </li>
            <li class="py-4 ml-6 pt-4">
                <a :href="githubLink" target="_blank" class="flex items-center">
                    <font-awesome-icon :icon="faGithub" class="mr-2" />
                    <span> Repo Github </span>
                </a>
            </li>
        </ul>
        <div class="fixed bottom-0 left-4">
            <button
                @click="logout"
                class="absolute bottom-4 w-10 h-10 text-white bg-red-500 rounded-full hover:bg-red-600 focus:outline-none"
            >
                <font-awesome-icon :icon="faSignOutAlt" />
            </button>
        </div>
    </div>
</template>

<script>
import {
    faHome,
    faFlag,
    faTrophy,
    faGear,
    faSignOutAlt,
    faArrowLeft,
    faArrowRight,
    faTableTennisPaddleBall,
} from '@fortawesome/free-solid-svg-icons';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
    components: {
        FontAwesomeIcon,
    },
    data() {
        return {
            menuLinks: [
                { to: '/', text: 'Accueil', icon: faHome },
                { to: '/matchs', text: 'Matchs', icon: faTableTennisPaddleBall },
                { to: '/bets', text: 'Mes Paris', icon: faFlag },
                { to: '/ranking', text: 'Classement', icon: faTrophy },
                { to: '/settings', text: 'Paramètres', icon: faGear },
            ],
        };
    },
    created() {
        this.faSignOutAlt = faSignOutAlt;
        this.faArrowLeft = faArrowLeft;
        this.faArrowRight = faArrowRight;
        this.faGithub = faGithub;
        this.githubLink = 'https://github.com/TheoLaperrouse/BetPlatform';
    },
    methods: {
        logout() {
            localStorage.removeItem('jwtToken');
            this.$router.push('/signin');
        },
    },
};
</script>
