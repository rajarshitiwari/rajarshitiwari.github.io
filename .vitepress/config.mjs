import { defineConfig } from 'vitepress'


// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Dr. Rajarshi Tiwari",
  description: "Personal and Research Site",
  // https://vitepress.dev/reference/default-theme-config
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'About', link: '/about'},
      { text: 'Research', link: '/research'},
      { text: 'CV', link: '/cv/cv-rajarshi' }
    ],

    sidebar: [
      {
        text: 'About Me',
        items: [
          { text: 'About', link: '/about' }
        ]
      },
      {
        text: 'Research Interests',
        items: [
          { text: 'Research', link: '/research' }
        ]
      },
      {
        text: 'Random Entries',
        items: [
          { text: 'Random', link: '/random' }
        ]
      },
      {
        text: 'Curriculum Vitae',
        items: [
          { text: 'CV', link: '/cv/cv-rajarshi' }
        ]
      },
      {
        text: 'Useful References',
        items: [
          { text: 'References', link: '/references' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/rajarshitiwari' }
    ]
  },
  markdown: {
    math: true
  }
})