import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import path from "path";
import { resolve } from "path";

export default defineConfig({
  base: '/your-repo-name/', // REPLACE with your actual GitHub repo name!
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
        login: resolve(__dirname, 'client/login-signup.html'),
        student: resolve(__dirname, 'client/student-view.html'),
        teacher: resolve(__dirname, 'client/teacher-view.html'),
        // Add any other HTML files you have
      }
    }
  },
  server: {
    port: 3000,
    host: true,
  },
});