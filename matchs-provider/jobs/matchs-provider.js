import { bree } from '../index.js';
import { getMatches } from './utils/api.service.js';
import { insertMatches } from './utils/pg.service.js';

(async () => {
    const matches = await getMatches();
    await insertMatches(matches);
    bree.stop();
})();
