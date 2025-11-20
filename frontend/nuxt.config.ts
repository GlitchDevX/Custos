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
    '@nuxt/content',
    '@nuxtjs/mdc',
    'nuxt-shiki',
  ],

  runtimeConfig: {
    public: {
      docsDev: false,
      promoMode: false,
      version: "v1.2.3"
    }
  },

  css: ['~/assets/css/main.css'],

  routeRules: {
    '/docs': {
      redirect: '/docs/introduction'
    }
  },

  nitro: {
    prerender: {
      routes: ["/docs/introduction"]
    }
  },

  image: {
    dir: "assets/img/",
    quality: 80,
    format: ["webp"],
    ipx: {
      modifiers: {
        quality: 85,
        format: "webp"
      }
    }
  },

  fonts: {
    defaults: {
      weights: [400, 700]
    }
  },

  icon: {
    serverBundle: {
      collections: ['lucide']
    },
    customCollections: [
      {
        prefix: 'ci',
        dir: 'app/assets/custom-icons'
      }
    ],
    mode: 'svg'
  },

  mdc: {
    highlight: {
      theme: 'poimandres',
    }
  },

  content: {
    build: {
      markdown: {
        toc: {
          depth: 3
        }
      }
    }
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
});