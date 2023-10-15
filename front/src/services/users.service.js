const baseURL = 'http://localhost:8080';

export const createUser = async (userData) => {
    const response = await fetch(`${baseURL}/users`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    });

    if (!response.ok) {
        throw new Error("Échec de la création de l'utilisateur");
    }

    const user = await response.json();
    return user;
};

export const getRanking = async () => {
    const response = await fetch(`${baseURL}/users/ranking`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    if (!response.ok) {
        throw new Error('Échec de récupération du classement');
    }

    const user = await response.json();
    return user;
};

export const login = async (userData) => {
    const response = await fetch(`${baseURL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    });

    if (!response.ok) {
        throw new Error('Échec lors de la connection');
    }

    const user = await response.json();
    return user;
};
