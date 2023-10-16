/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./src/**/*.{vue,js}', './public/index.html'],
    theme: {
        extend: {
            spacing: {
                42: '10.5rem',
            },
        },
    },
    plugins: [],
};
