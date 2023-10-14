<template>
    <div>
        <h2 class="text-2xl font-semibold mb-4">Créer un compte</h2>
        <form @submit.prevent="register">
            <div class="mb-4">
                <label for="firstName" class="block text-gray-600 font-medium text-sm">Prénom</label>
                <input
                    type="text"
                    id="firstName"
                    v-model="firstName"
                    class="w-full mt-1 p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
                    required
                />
            </div>
            <div class="mb-4">
                <label for="lastName" class="block text-gray-600 font-medium text-sm">Nom</label>
                <input
                    type="text"
                    id="lastName"
                    v-model="lastName"
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
</template>

<script>
import createUser from '../services/users.service';

export default {
    data() {
        return {
            firstName: '',
            lastName: '',
            email: '',
            password: '',
        };
    },
    methods: {
        async register() {
            await createUser({ firstName: '', lastName: '', email: this.email, password: this.password });
        },
    },
};
</script>
