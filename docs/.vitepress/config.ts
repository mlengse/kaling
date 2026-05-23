import { defineConfig } from 'vitepress'
import { generateSidebar } from './sidebar'
import vitePugPlugin from "vite-plugin-pug-transformer"
import { robots } from 'vite-plugin-robots';
// import UnoCSS from 'unocss/vite'
// import Components from 'unplugin-vue-components/vite'
// import { AnuComponentResolver } from 'anu-vue'
// import { hostname } from 'os'

const sidebar = generateSidebar( {
  root: 'docs',
  rootGroupText: 'Daftar Isi',
  useTitleFromFileHeading: true,
  useTitleFromFrontmatter: true,
  hyphenToSpace: true,
  underscoreToSpace: true,
  collapsed: true,
  collapseDepth: 2,
  sortByFileName: ['pendahuluan', 'survei'],
  excludeFolders: ['examples'],
  excludeFiles: ['404.md'],
  includeEmptyFolder: false,
  convertSameNameSubFileToGroupIndexPage: false,
  convertIndexSubFileToGroupIndexPage: true,
})

export default defineConfig({
  lang: "id",
  title: "Akreditasi Klinik",
  description: "Dokumen referensi persiapan akreditasi Klinik Pratama dan Utama",
  cleanUrls: true,
  sitemap: {
    hostname: 'https://klg.jyg.my.id'
  },
  head: [
    // ['meta', { name: 'google-site-verification', content: 'VERIFIKASI_GOOGLE_ANDA' }], // Nanti user bisa ganti dengan kode verifikasi mereka
    ['meta', { name: 'keywords', content: 'akreditasi klinik, kmk 62/2026, permenkes 14/2021, template dokumen klinik, tkk, pmkp, pkp, sdm, mfk, ppi, rekam medis' }],
    ['meta', { name: 'author', content: 'Klinik Pratama dan Utama' }],
    ['meta', { name: 'robots', content: 'index, follow' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Akreditasi Klinik - Dokumen & Template Lengkap' }],
    ['meta', { property: 'og:description', content: 'Dokumen referensi persiapan akreditasi Klinik Pratama dan Utama sesuai standar instrumen KMK 62/2026.' }],
    ['meta', { property: 'og:url', content: 'https://klg.jyg.my.id' }]
  ],
  locales: {
    root: {
      label: 'Indonesia',
      lang: 'id'
    },
  },
  vite: {
    // viteNext: true,
    plugins: [
      vitePugPlugin({}),
      robots({})
      // UnoCSS({}),
      // Components({
        // resolvers: [
          // AnuComponentResolver()
        // ]
      // }),
    ],
  },
  themeConfig: {
    search: {
      provider: 'local'
    },
    sidebar,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/mlengse/kaling' }
    ]
  }
})
