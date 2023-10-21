import { baseURL } from './api.config';
import { Toast } from '@/components/toast.ts';

export const getMatches = async () => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/matches`, {
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

    const matches = await response.json();
    return matches;
};
