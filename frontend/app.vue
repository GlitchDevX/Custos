<template>
  <div class="app-wrapper">
    <UApp>
      <NavHeader />
      <NuxtPage />
    </UApp>
  </div>
</template>

<script lang="ts" setup>
useHead({
  link: [
    { rel: 'shortcut icon', href: '/favicon.png' },
  ]
})
</script>

<style>
* {
  font-family: Inter;
}
</style>