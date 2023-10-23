import pg from 'pg';

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
        console.error('Error inserting matches', err);
    }
}
