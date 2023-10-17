import { Toast } from '@/components/toast.ts';
import { baseURL } from './api.config';

export const sendBets = async (betsData) => {
    const response = await fetch(`${baseURL}/bets`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(betsData),
    });

    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: "Erreur lors de l'envoi des paris",
        });
    }

    const bets = await response.json();
    return bets;
};

export const getMyBets = async (userId) => {
    const response = await fetch(`${baseURL}/bets/${userId}`);

    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: 'Erreur lors de la récupération des paris',
        });
    }

    const bets = await response.json();
    return bets;
};