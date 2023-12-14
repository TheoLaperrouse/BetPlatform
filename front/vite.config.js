import { defineConfig } from 'vite';
import Vue from '@vitejs/plugin-vue';
import Eslint from 'vite-plugin-eslint';
import path from 'path';

export default defineConfig({
    plugins: [Vue(), Eslint()],
    server: {
        port: 8080,
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),
        },
    },
});
