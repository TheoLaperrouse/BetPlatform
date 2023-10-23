import { Toast } from '@/components/toast.ts';
import { baseURL } from './api.config';

export const sendBets = async (betsData) => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/bets`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
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

export const sendBet = async (betsData) => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/bets`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(betsData),
    });

    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: "Erreur lors de l'envoi du pari",
        });
    }

    const bets = await response.json();
    return bets;
};

export const getMyBets = async () => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/bets`, {
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        },
    });
    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: 'Erreur lors de la récupération des paris',
        });
    }

    const bets = await response.json();
    return bets;
};
