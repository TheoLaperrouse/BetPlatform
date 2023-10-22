<template>
    <div class="px-4 py-8">
        <h2 class="text-2xl font-semibold text-center p-4">Paramètres</h2>
        <form @submit.prevent="saveUser" class="max-w-md mx-auto space-y-4">
            <div class="mb-4">
                <label for="first_name" class="text-gray-600 font-medium">Prénom</label>
                <input
                    type="text"
                    id="first_name"
                    v-model="user.first_name"
                    class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <div class="mb-4">
                <label for="last_name" class="text-gray-600 font-medium">Nom</label>
                <input
                    type="text"
                    id="last_name"
                    v-model="user.last_name"
                    class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <div class="mb-4">
                <label for="email" class="text-gray-600 font-medium">Email</label>
                <input
                    type="text"
                    id="email"
                    v-model="user.email"
                    class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <div class="mb-4">
                <label for="password" class="text-gray-600 font-medium">Mot de passe</label>
                <input
                    type="password"
                    id="password"
                    v-model="user.password"
                    class="w-full p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <button
                type="submit"
                class="w-full bg-blue-500 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded"
                @click="onUpdateUser(currentUser.id, user)"
            >
                Enregistrer
            </button>
        </form>
    </div>
</template>

<script>
import { updateUser, setAccessToken } from '@/services/users.service';

export default {
    data() {
        return {
            user: {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
            },
        };
    },
    created() {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
        this.user = { ...this.currentUser, password: '' };
    },
    methods: {
        async onUpdateUser(userId, userData) {
            const user = { ...userData };
            delete user.id;
            const { access_token } = await updateUser(userId, user);
            await setAccessToken(access_token);
        },
    },
};
</script>
