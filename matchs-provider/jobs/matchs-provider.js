import { bree } from '../index.js';
import { getMatches } from './utils/api.service.js';
import { insertMatches, updateStatus } from './utils/pg.service.js';

(async () => {
    const matches = await getMatches();
    await insertMatches(matches);
    await updateStatus(matches);
    bree.stop();
})();
