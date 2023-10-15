// betService.js
const baseURL = 'http://localhost:8080'; // L'URL de votre API

export const sendBets = async (betsData) => {
    const response = await fetch(`${baseURL}/bets`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(betsData),
    });

    if (!response.ok) {
        throw new Error("Échec de l'envoi des paris");
    }

    const bets = await response.json();
    return bets;
};

export const getMyBets = async (userId) => {
    const response = await fetch(`${baseURL}/bets/${userId}`);

    if (!response.ok) {
        throw new Error('Échec de la récupération des paris');
    }

    const bets = await response.json();
    return bets;
};
