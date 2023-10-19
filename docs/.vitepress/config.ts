import { defineConfig } from 'vitepress'
import { generateSidebar } from './sidebar'
import pugPlugin from "vite-plugin-pug"
import Unocss from 'unocss/vite'
import Components from 'unplugin-vue-components/vite'
import { AnuComponentResolver } from 'anu-vue'

const sidebar = generateSidebar( {
  root: 'docs',
  rootGroupText: 'Daftar Isi',
  useTitleFromFileHeading: true,
  useTitleFromFrontmatter: true,
  hyphenToSpace: true,
  underscoreToSpace: true,
  collapsed: true,
  collapseDepth: 2,
  sortByFileName: ['referensi'],
  excludeFolders: ['examples'],
  includeEmptyFolder: false,
  convertSameNameSubFileToGroupIndexPage: false,
  convertIndexSubFileToGroupIndexPage: true,
})

export default defineConfig({
  title: "Akreditasi Klinik",
  description: "Dokumen referensi persiapan akreditasi Klinik Dr. Ning Kaling",
  cleanUrls: true,
  locales: {
    root: {
      label: 'Indonesia',
      lang: 'id'
    },
  },
  vite: {
    plugins: [
      pugPlugin(),
      Unocss(),
      Components({
        resolvers: [
          AnuComponentResolver()
        ]
      }),
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
