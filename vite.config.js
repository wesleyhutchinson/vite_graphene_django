import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    outDir: "dist",
    assetsDir: "static",
  },
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  devServer: {
    historyApiFallback: true,
    proxy: {
      "/api*": {
        // Forward frontend dev server request for /api to django dev server
        target: "http://localhost:8000/",
      },
    },
  },
});
