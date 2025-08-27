<template>
    <div class="w-full h-16">
        <div class="flex flex-row justify-between align-middle px-2 fixed header-container z-50 w-full">
            <UButton variant="ghost" href="/" size="md" icon="ci:custos-logo" class="my-2 text-2xl font-bold">
                Custos
            </UButton>

            <UNavigationMenu :items="navigationItems"/>
        </div>
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
    label: 'Monitoring',
    icon: 'lucide-chart-column',
    to: '/monitoring'
  },
  {
    label: 'Playground',
    icon: 'lucide-send',
    to: '/playground'
  },
  {
    label: 'Configuration',
    icon: 'lucide-settings',
    to: '/config'
  }
]);
</script>

<style scoped>
.header-container {
  backdrop-filter: blur(5px);
  border-bottom: 1px var(--ui-bg-muted) solid;
  background: color-mix(in oklch increasing hue, var(--ui-bg) 50%, rgba(57, 57, 57, 0) 50%)
}
</style>