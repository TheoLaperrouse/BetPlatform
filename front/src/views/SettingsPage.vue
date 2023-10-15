<template>
    <div>
        <h2 class="text-2xl font-semibold mb-4">Paramètres</h2>
        <form @submit.prevent="saveSettings">
            <div class="mb-4">
                <label for="firstName">Prénom</label>
                <input type="text" id="firstName" v-model="user.firstName" />
            </div>
            <div class="mb-4">
                <label for="lastName">Nom</label>
                <input type="text" id="lastName" v-model="user.lastName" />
            </div>
            <div class="mb-4">
                <label for="email">Email</label>
                <input type="text" id="email" v-model="user.email" />
            </div>
            <div class="mb-4">
                <label for="password">Mot de passe</label>
                <input type="password" id="password" v-model="user.password" />
            </div>
            <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded">
                Enregistrer
            </button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                firstName: '',
                lastName: '',
                email: '',
                password: '',
            },
        };
    },
    methods: {
        saveUser() {
            return;
        },
    },
};
</script>
