import { defineConfig } from 'vitepress'
import { generateSidebar } from './sidebar'
import vitePugPlugin from "vite-plugin-pug-transformer"
import UnoCSS from 'unocss/vite'
import Components from 'unplugin-vue-components/vite'
import { AnuComponentResolver } from 'anu-vue'
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
  includeEmptyFolder: false,
  convertSameNameSubFileToGroupIndexPage: false,
  convertIndexSubFileToGroupIndexPage: true,
})

export default defineConfig({
  lang: "id",
  title: "Akreditasi Klinik",
  description: "Dokumen referensi persiapan akreditasi Klinik Dr. Ning Kaling",
  cleanUrls: true,
  // viteNext: true,
  sitemap: {
    hostname: 'https://klg.jyg.my.id'
  },
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
