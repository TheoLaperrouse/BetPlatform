<template>
    <div>
        <h2 class="text-2xl font-semibold mb-4">Classement des Joueurs</h2>
        <table class="w-full border-collapse border border-gray-300">
            <thead>
                <tr>
                    <th class="p-3">Position</th>
                    <th class="p-3">Joueur</th>
                    <th class="p-3">Points</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(player, index) in players" :key="player.id">
                    <td class="p-3">{{ index + 1 }}</td>
                    <td class="p-3">{{ player.name }}</td>
                    <td class="p-3">{{ player.points }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        players: Array,
    },
};
</script>
