import pg from 'pg';
import _ from 'lodash';

export const pool = new pg.Pool({
    user: process.env.POSTGRES_USER,
    password: process.env.POSTGRES_PASSWORD,
    database: process.env.POSTGRES_DB,
    host: 'db',
    port: 5432,
});

export async function insertMatches(matches) {
    try {
        for (let match of matches) {
            const { matchId, teams, score, isHome, matchDate, matchDay, link } = match;

            const query = {
                text:
                    'INSERT INTO matches (id, teams, score, match_date, match_day, is_home, link) VALUES ($1, $2, $3, $4, $5, $6, $7) ' +
                    'ON CONFLICT (id) DO UPDATE SET score = EXCLUDED.score',
                values: [matchId, teams, score, matchDate, matchDay, isHome, link],
            };

            await pool.query(query);
        }
        console.log('Matchs bien insérés en base');
    } catch (err) {
        console.error('Erreur sur insertion match', err);
    }
}

export async function getBets() {
    try {
        const query = { text: 'SELECT * FROM bets' };

        const bets = await pool.query(query);
        console.log('Paris bien récupérés en base');
        return bets.rows;
    } catch (err) {
        console.error('Erreur sur récupération des paris', err);
    }
}

export async function updateStatus(matches) {
    try {
        const bets = await getBets();
        for (const match of matches) {
            const filteredBets = bets.filter((bet) => bet.match_id === match.matchId);

            if (_.isNil(match?.score[0]) && _.isNil(match?.score[1])) {
                continue;
            }

            const matchVicIndex = match.score[0] > match.score[1] ? 0 : 1;

            filteredBets.forEach(async (bet) => {
                const { id, bet_score } = bet;
                const betVicIndex = bet_score[0] > bet_score[1] ? 0 : 1;
                let status = 0;

                if (_.isEqual(bet_score, match.score)) {
                    status = 3;
                } else if (matchVicIndex === betVicIndex) {
                    status = 2;
                } else {
                    status = 1;
                }

                await pool.query({
                    text: 'UPDATE public.bets SET status=$1 WHERE id=$2',
                    values: [status, id],
                });
            });
        }
        console.log('Statuts bien mis à jour');
    } catch (err) {
        console.error('Erreur sur la mise à jour des status', err);
    }
}
