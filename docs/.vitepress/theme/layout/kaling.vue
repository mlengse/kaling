<!--.vitepress/theme/MyLayout.vue-->
<script setup>
import DefaultTheme from 'vitepress/theme'
const { Layout } = DefaultTheme
import { useRouter } from 'vitepress';
const router = useRouter();
import { watch } from 'vue';
// import { ABtn } from 'anu-vue'
if (typeof window !== 'undefined' ) {
  watch(() => router.route.data, () => {
    import('../../scroll').then(async (module) => {
    const { useScroll } = module
      await useScroll()
    })
  }, { immediate: true });
}

</script>

<template lang="pug">
Layout
  template(#doc-before) 
    //- br
    //- ABtn.text-sm(variant="outline") Button
    //- br
</template>

<style>
.vp-doc{
  hyphens: auto;
  text-align: justify;
  text-justify: auto;
  
}

.vp-doc h1, 
.vp-doc h2 {
  text-align: start;

}
</style>