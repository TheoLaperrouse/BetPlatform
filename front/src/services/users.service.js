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
