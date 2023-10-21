export const BASE_API_URL = 'http://fastapifftt.thorigne-tt.net';

const isTFTTRegex = /THORIGNE/i;
const matchDayRegex = /tour n°(\d+)/;

function filterNullValues(arr) {
    return arr.filter((element) => element !== null);
}

function convertDateToISO(dateString) {
    const [day, month, year] = dateString.split('/');
    const isoDate = `${year}-${month}-${day}`;
    return isoDate;
}

function formatMatches(matches) {
    return matches
        .filter(({ equa, equb }) => isTFTTRegex.test(equa) || isTFTTRegex.test(equb))
        .map(({ equa, equb, scorea, scoreb, datereelle, lien, libelle }) => {
            const teams = [equa, equb];
            let score = [scorea, scoreb];
            if (equa === null) {
                score = [0, 14];
            } else if (equb === null) {
                score = [14, 0];
            }

            const dayMatch = libelle.match(matchDayRegex);
            return {
                teams: filterNullValues(teams),
                score: filterNullValues(score),
                isHome: isTFTTRegex.test(equa),
                matchDate: convertDateToISO(datereelle),
                matchDay: dayMatch.length > 1 ? dayMatch[1] : 0,
                link: lien,
            };
        });
}

export async function getMatches() {
    const response = await fetch(`${BASE_API_URL}/matches/club/03350060`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });
    const matches = await response.json();

    console.log("Matchs bien récupérés depuis l'api");
    return formatMatches(matches);
}
