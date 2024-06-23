import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Fungi",
  description: "Self-hosted discord bot with an extensive configuration file to fit any servers need, all for free.",
  head: [
    ['link', { rel: 'icon', href: './favicon.ico' }],
    [
      'script',
      { src: "https://code.iconify.design/iconify-icon/2.1.0/iconify-icon.min.js" }
    ],
  ],

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
    
    search: {
      provider: 'algolia',
      options: {
        appId: '7PX6C4338U',
        apiKey: 'df7a40c506154c3d29acc38b2b821eb5',
        indexName: 'fungibot'
      }
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
      {
        text: 'Community',
        items: [
          { text: 'People of Fungi 🍄', link: '/developers/' },
          { text: 'Developers', link: '/developers/overview' }
        ]
      },
    ],

    sidebar: {
      '/guides/': [
        {
          text: 'Guides 📚',
          items: [
            { text: 'What is Fungi?', link: '/guides/' },
            { text: 'Getting Started 🚀', link: '/guides/getting-started' },
          ]
        }
      ],

      '/developers/': [
        {
          text: 'Developers 💻',
          items: [
            // { text: 'People of Fungi 🍄', link: '/developers/' },
            { text: 'Contributing',
              collapsed: false,
              link: '/developers/overview', 
              // items: [
              //   { text: 'Contributing to Fungi', link: '/developers/fungi' },
              //   { text: 'Contributing to Docs', link: '/developers/docs' }
              //   ]
            },
            { text: 'Changelog', link: 'https://github.com/hyerland/Fungi/blob/main/CHANGELOG.md' },
          ]
        }
      ],
      '/config/': [
        {
          text: 'Configuration 🔨',
          items: [
            { text: 'Overview', 
              link: '/config/', 
              items: [
                { text: 'Commands', link: '/config/commands' },
                { text: 'Settings', link: '/config/settings' },
                { text: 'Other', link: '/config/other' },
                ]
            },
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
