// @ts-check
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  site: "https://nayo126.github.io",
  base: "/auto-blog",
  trailingSlash: "always",
  build: {
    format: "directory",
  },
});
