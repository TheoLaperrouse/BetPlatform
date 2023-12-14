import { capitalize } from 'lodash';
import moment from 'moment/min/moment-with-locales';

export const formatDate = (date) => {
    const formattedDate = date ? moment(date).locale('fr').format('dddd D MMMM YYYY') : '';
    return capitalize(formattedDate);
};
