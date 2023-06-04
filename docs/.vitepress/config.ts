import { defineConfig } from 'vitepress'
// import { generateSidebar } from 'vitepress-sidebar';
// import AutoNavPlugin from 'vitepress-auto-nav-sidebar'
import { generateSidebar } from './sidebar'

const sidebar = generateSidebar( {
  root: 'docs',
  rootGroupText: 'Daftar Isi',
  // rootGroupLink: 'https://github.com/jooy2',
  useTitleFromFileHeading: true,
  useTitleFromFrontmatter: true,
  hyphenToSpace: true,
  underscoreToSpace: true,
  collapsed: true,
  collapseDepth: 2,
  sortByFileName: ['referensi'],
  // excludeFiles: ['first.md', 'secret.md'],
  excludeFolders: ['examples'],
  // includeDotFiles: false,
  // includeRootIndexFile: false,
  includeEmptyFolder: false,
  convertSameNameSubFileToGroupIndexPage: false,
  convertIndexSubFileToGroupIndexPage: true,
  // folderLinkNotIncludesFileName: false
})

// console.log(JSON.stringify(sidebar))

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Akreditasi Klinik",
  description: "Dokumen referensi persiapan akreditasi Klinik Dr. Ning Kaling",
  // cleanUrls: true,
  themeConfig: {
    search: {
      provider: 'local'
    },
    // https://vitepress.dev/reference/default-theme-config
    // nav: [
    //   { text: 'Home', link: '/' },
    //   // { text: 'Examples', link: '/markdown-examples' }
    // ],
    // nav,
    // sidebar:[
    //   {
    //     text: 'Home',
    //     link: '/',
    //     items: [
    //       {
    //         text: 'Referensi',
    //         link: '/referensi'
    //       }
    //     ]
    //   },
    //   {
    //     text: 'Bab 1',
    //     link: '/1',
    //     items: [
    //       {
    //         text: 'Standar 1',
    //         link: '/1/1'
    //       }
    //     ]
    //   }
    // ],
    sidebar,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/mlengse/kaling' }
    ]
  }
})
