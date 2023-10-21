<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="bg-white p-8 rounded-lg shadow-md w-96">
            <h2 class="text-2xl font-semibold mb-6">Créer un compte</h2>
            <form @submit.prevent="register">
                <div class="mb-4">
                    <label for="first_name" class="block text-gray-600 font-medium text-sm">Prénom</label>
                    <input
                        type="text"
                        id="first_name"
                        v-model="first_name"
                        class="w-full mt-1 p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                        required
                    />
                </div>
                <div class="mb-4">
                    <label for="last_name" class="block text-gray-600 font-medium text-sm">Nom</label>
                    <input
                        type="text"
                        id="last_name"
                        v-model="last_name"
                        class="w-full mt-1 p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                        required
                    />
                </div>
                <div class="mb-4">
                    <label for="email" class="block text-gray-600 font-medium text-sm">Email</label>
                    <input
                        type="email"
                        id="email"
                        v-model="email"
                        class="w-full mt-1 p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                        required
                    />
                </div>
                <div class="mb-4">
                    <label for="password" class="block text-gray-600 font-medium text-sm">Mot de passe</label>
                    <input
                        type="password"
                        id="password"
                        v-model="password"
                        class="w-full mt-1 p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                        required
                    />
                </div>

                <div class="mb-4">
                    <button
                        type="submit"
                        class="w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring"
                    >
                        S'inscrire
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { createUser } from '../services/users.service';
import { getMe } from '../services/users.service';

export default {
    data() {
        return {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
        };
    },
    methods: {
        async register() {
            const { access_token } = await createUser({
                first_name: this.first_name,
                last_name: this.last_name,
                email: this.email,
                password: this.password,
            });
            if (access_token) {
                await setAccessToken(access_token);
                this.$router.push('/');
            }
        },
    },
};
</script>
