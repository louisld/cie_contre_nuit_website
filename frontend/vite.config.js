import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: '../app/static/assets',
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, 'src/main.js'),
      },
      output: {
        entryFileNames: 'main.js',
        assetFileNames: 'main.css',
      },
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "bulma/bulma";`,
      },
    },
  },
});