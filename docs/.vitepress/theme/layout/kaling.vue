<!--.vitepress/theme/MyLayout.vue-->
<script setup>
import DefaultTheme from 'vitepress/theme'
const { Layout } = DefaultTheme
import { useRouter } from 'vitepress';
const router = useRouter();
import { watch } from 'vue';

// Only run this on the client. Not during build.
if (typeof window !== 'undefined' ) {

  watch(() => router.route.data.relativePath, (path) => {
    console.log(path)
    import('../../scroll').then(async (module) => {
    const { useScroll } = module
      await useScroll()
      // use code
    })
  }, { immediate: true });
}

</script>

<template lang="pug">
Layout
  //- template(#doc-before) My custom sidebar top content
</template>