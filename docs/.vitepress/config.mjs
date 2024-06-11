import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Fungi",
  description: "Self-hosted discord bot with an extensive configuration file to fit any servers need, all for free.",
  head: [['link', { rel: 'icon', href: '/assets/favicon.ico' }]],

  lastUpdated: true,

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: '/assets/favicon.ico',

    footer: {
      message: 'Released under the <a href="https://github.com/hyerland/Fungi/blob/main/LICENSE">MIT License</a>.',
      copyright: 'Copyright © 2024 - Present, <a href="https://github.com/hyerland">Adam Garza</a>'
    },

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Documentation', link: '/guides/' }
    ],

    sidebar: [
      {
        text: 'Guides 📚',
        items: [
          { text: 'Introduction', link: '/guides/' },
          // { text: 'Getting Started 🚀', link: '/guides/getting-started' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/hyerland/fungi' },
      { icon: 'twitter', link: 'https://x.com/adamg_dev' }
    ]
  }
})
