import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import path from "path";
import { resolve } from "path";

export default defineConfig({
  base: '/Prompted-AI-Mastery/',
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./client/src"),
    },
  },
  root: path.resolve(__dirname, "client"),
  build: {
    outDir: path.resolve(__dirname, "dist"),
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'client/index.html'),
        auth: resolve(__dirname, 'client/auth.js'), 
      },
      output: {
        entryFileNames: (chunkInfo) => {
          // Keep auth.js at the root of dist
          if (chunkInfo.name === 'auth') {
            return 'auth.js';
          }
          return 'assets/[name]-[hash].js';
        }
      }
    }
  },
  server: {
    port: 3000,
    host: true,
  },
});