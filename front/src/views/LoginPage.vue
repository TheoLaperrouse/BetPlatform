<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="bg-white p-8 rounded-lg shadow-md w-96">
            <h2 class="text-2xl font-semibold mb-6">Connexion</h2>
            <form @submit.prevent="login">
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
                        Confirmer
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: '',
            password: '',
        };
    },
    methods: {
        login() {
            this.$router.push('/');
        },
    },
};
</script>
