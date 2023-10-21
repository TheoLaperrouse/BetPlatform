import { Toast } from '@/components/toast.ts';
import { baseURL } from './api.config';

export async function setAccessToken(access_token) {
    localStorage.setItem('jwtToken', access_token);
    localStorage.setItem('currentUser', JSON.stringify(await getMe()));
}

export const login = async (userCredentials) => {
    const response = await fetch(`${baseURL}/users/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userCredentials),
    });

    if (!response.ok) {
        const { detail } = await response.json();
        return Toast.fire({
            icon: 'error',
            title: detail,
        });
    }

    const user = await response.json();
    return user;
};

export const getUsers = async () => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/users`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        },
    });

    if (!response.ok) {
        const { detail } = await response.json();
        return Toast.fire({
            icon: 'error',
            title: detail,
        });
    }

    const users = await response.json();
    return users;
};

export const getMe = async () => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/users/me`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        },
    });

    if (!response.ok) {
        const { detail } = await response.json();
        return Toast.fire({
            icon: 'error',
            title: detail,
        });
    }

    const user = await response.json();
    return user;
};

export const createUser = async (user) => {
    const response = await fetch(`${baseURL}/users`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
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

export const updateUser = async (userId, userData) => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/users/${userId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(userData),
    });

    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: "Un champ n'a pas été rempli",
        });
    }
    Toast.fire({
        icon: 'success',
        title: 'Utilisateur mis à jour',
    });
    const new_token = await response.json();
    return new_token;
};
