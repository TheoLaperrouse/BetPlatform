import { Toast } from '@/components/toast.ts';
import { baseURL } from './api.config';

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

export const updateUser = async (userData, userId) => {
    const token = sessionStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/users/${userId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(userData),
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
    const token = sessionStorage.getItem('jwtToken');
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
    const token = sessionStorage.getItem('jwtToken');
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
