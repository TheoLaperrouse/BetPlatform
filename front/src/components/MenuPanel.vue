<template>
    <div class="menu">
        <ul>
            <li><router-link to="/">Accueil</router-link></li>
            <li><router-link to="/paris">Paris</router-link></li>
            <li><router-link to="/classement">Classement</router-link></li>
            <!-- Ajoutez d'autres liens vers les pages de votre application -->
        </ul>
    </div>
</template>

<style>
.menu {
    position: fixed;
    top: 0;
    left: -300px; /* Réglez la largeur que vous souhaitez pour le menu dépliant */
    width: 300px; /* Réglez la largeur que vous souhaitez pour le menu dépliant */
    height: 100%;
    background-color: #333;
    color: #fff;
    overflow-y: auto;
    transition: left 0.3s;
}

.menu ul {
    list-style: none;
    padding: 0;
}

.menu li {
    padding: 10px;
}

.menu a {
    text-decoration: none;
    color: #fff;
}
</style>
