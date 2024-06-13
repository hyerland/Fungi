import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Fungi",
  description: "Self-hosted discord bot with an extensive configuration file to fit any servers need, all for free.",
  head: [['link', { rel: 'icon', href: './favicon.ico' }]],

  lastUpdated: true,

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: './favicon.ico',

    footer: {
      message: 'Released under the <a href="https://github.com/hyerland/Fungi/blob/main/LICENSE">MIT License</a>.',
      copyright: 'Copyright © 2024 - Present, <a href="https://github.com/hyerland">Adam Garza</a>'
    },
    
    editLink: {
      pattern: 'https://github.com/hyerland/fungi/edit/main/docs/:path'
    },

    nav: [
      { text: 'Home', link: '/' },
      {
        text: 'Documentation',
        items: [
          { text: 'Guides 📚', link: '/guides/' },
          { text: 'Configuration 🔨', link: '/config/' }
        ]
      },
      { text: 'Community', link: '/community/' }
    ],

    sidebar: {
      '/guides/': [
        {
          text: 'Guides 📚',
          items: [
            { text: 'Introduction', link: '/guides/' },
            { text: 'Getting Started 🚀', link: '/guides/getting-started' },
          ]
        }
      ],

      '/community/': [
        {
          text: 'Community 🌎',
          items: [
            { text: 'People of Fungi', link: '/community/' },
          ]
        }
      ],
      '/config/': [
        {
          text: 'Configuration 🔨',
          items: [
            { text: 'Overview', link: '/config/' },
            { text: 'Settings', link: '/config/settings' },
            { text: 'Other', link: '/config/other' },
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/hyerland/fungi' },
      { icon: 'twitter', link: 'https://x.com/adamg_dev' }
    ]
  }
})
