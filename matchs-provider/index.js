import Bree from 'bree';
import Graceful from '@ladjs/graceful';

export const bree = new Bree({
    jobs: [
        {
            name: 'matchs-provider',
            interval: 'every 8 hours',
        },
    ],
});

const graceful = new Graceful({ brees: [bree] });
graceful.listen();

(async () => {
    await bree.start();
})();
