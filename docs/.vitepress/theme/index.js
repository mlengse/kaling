// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import Kaling from './layout/kaling.vue'
import './style.css'

export default {
  ...DefaultTheme,
  Layout: Kaling,
  // Layout: () => {
  //   return h(Theme.Layout, null, {
  //     // https://vitepress.dev/guide/extending-default-theme#layout-slots
  //   })
  // },
  enhanceApp({ app, router, siteData }) {
    // ...
  }
}
