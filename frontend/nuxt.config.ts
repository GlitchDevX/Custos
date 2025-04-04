// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  modules: [
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/ui',
    'nuxt-shiki',
  ],

  css: ['~/assets/css/main.css'],

  image: {
    dir: "assets/img/"
  },

  icon: {
    serverBundle: {
      collections: ['lucide']
    },
    customCollections: [
      {
        prefix: 'ci',
        dir: './assets/custom-icons'
      }
    ],
    mode: 'svg'
  },

  shiki: {
    defaultTheme: {
      light: 'poimandres',
      dark: 'poimandres',
    },
    bundledLangs: [
      "yaml",
      "json"
    ],
    bundledThemes: [
      "poimandres"
    ]
  },
})