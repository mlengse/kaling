import DefaultTheme from 'vitepress/theme'
import Kaling from './layout/kaling.vue'
// import './style.css'
// import type { App } from 'vue'
import { anu } from 'anu-vue'
import 'uno.css'
import 'anu-vue/dist/style.css'
import '@anu-vue/preset-theme-default/dist/style.css'

export default {
  ...DefaultTheme,
  Layout: Kaling,
  enhanceApp({ app }) {
    app.use(anu, {
      registerComponents: false,
    })
  }
}
