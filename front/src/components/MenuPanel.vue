<template>
    <div class="menu top-0 left-0 w-60 h-screen bg-gray-800 text-white">
        <ul class="list-none p-0 mt-4">
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
        <div class="fixed bottom-4 left-4">
            <button
                @click="logout"
                class="absolute bottom-4 w-10 h-10 text-white bg-red-500 rounded-full hover:bg-red-600 focus:outline-none"
            >
                <font-awesome-icon :icon="faSignOutAlt" />
            </button>
            <button
                @click="toggleMenu"
                class="absolute bottom-4 left-42 w-10 h-10 text-white bg-gray-600 rounded-full hover:bg-gray-700 focus:outline-none"
            >
                <font-awesome-icon :icon="menuClosed ? faArrowRight : faArrowLeft" />
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
} from '@fortawesome/free-solid-svg-icons';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { useUserStore } from '@/store/users.store';

export default {
    components: {
        FontAwesomeIcon,
    },
    data() {
        return {
            menuClosed: localStorage.getItem('menuClosed') === 'true' || false,
            menuLinks: [
                { to: '/', text: 'Accueil', icon: faHome },
                { to: '/bets', text: 'Paris', icon: faFlag },
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
            sessionStorage.removeItem('jwtToken');
            useUserStore().clearUser();
            this.$router.push('/signin');
        },
        toggleMenu() {
            this.menuClosed = !this.menuClosed;
            localStorage.setItem('menuClosed', this.menuClosed);
        },
    },
};
</script>
