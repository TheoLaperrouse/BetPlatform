import { Toast } from '@/components/toast.ts';
import { baseURL } from './api.config';

export const getMyBets = async () => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/bets/my_bets`, {
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

    Toast.fire({
        icon: 'success',
        title: 'Pari Envoyé',
    });

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

    Toast.fire({
        icon: 'success',
        title: 'Pari envoyé',
    });

    const bets = await response.json();
    return bets;
};

export const updateBet = async (betId, bet_score) => {
    const token = localStorage.getItem('jwtToken');
    const response = await fetch(`${baseURL}/bets/${betId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ bet_score }),
    });
    if (!response.ok) {
        return Toast.fire({
            icon: 'error',
            title: "Erreur lors de l'envoi du pari",
        });
    }

    Toast.fire({
        icon: 'success',
        title: 'Pari mis à jour',
    });

    const bets = await response.json();
    return bets;
};
