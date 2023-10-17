import { Toast } from '@/components/toast.ts';
import { baseURL } from './api.config';

export const createUser = async (user) => {
    const response = await fetch(`${baseURL}/users`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: user.first_name,
            last_name: user.last_name,
            email: user.email,
            password: user.password,
        }),
    });

    if (!response.ok) {
        const { detail } = await response.json();
        return Toast.fire({
            icon: 'error',
            title: detail,
        });
    }

    const token = await response.json();
    return token;
};

export const updateUser = async (userData, userId) => {
    const response = await fetch(`${baseURL}/users/${userId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    });

    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: "Erreur lors de la modification de l'utilisateur",
        });
    }

    const user = await response.json();
    return user;
};

export const getUsers = async () => {
    const response = await fetch(`${baseURL}/users`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: 'Erreur lors de la récupération du classement',
        });
    }

    const users = await response.json();
    return users;
};

export const login = async (userData) => {
    const response = await fetch(`${baseURL}/users/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userData }),
    });

    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: 'Erreur lors de la connection',
        });
    }

    const user = await response.json();
    return user;
};
