<template>
  <div class="flex flex-row justify-between align-middle px-2">
    <UButton variant="ghost" href="/" size="md" icon="ci:logo" class="my-2 text-2xl font-bold">
        Custos
    </UButton>

    <UNavigationMenu :items="navigationItems"/>
  </div>
</template>

<script lang="ts" setup>
import type { NavigationMenuItem } from '@nuxt/ui'

const navigationItems = ref<NavigationMenuItem[]>([
  {
    label: 'Home',
    icon: 'lucide-home',
    to: '/',
  },
  {
    label: 'Playground',
    icon: 'lucide-send',
    to: '/playground'
  },
  {
    label: 'Flagged Users',
    icon: 'lucide-flag',
    to: '/flagged-users'
  },
  {
    label: 'Configuration',
    icon: 'lucide-settings',
    to: '/config'
  }
]);
</script>

<style>

</style>