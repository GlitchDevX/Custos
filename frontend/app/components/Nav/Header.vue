<template>
    <div class="w-full h-16">
        <div class="flex flex-row justify-between align-middle px-2 fixed header-container z-1001  w-full">
            <UButton variant="ghost" href="/" size="md" icon="ci:custos-logo" class="my-2 text-2xl font-bold">
                Custos
            </UButton>

            <UNavigationMenu :items="navigationItems" />
            <!--
              <tailwind-include class="
                [&>li:nth-child(1)>a]:text-primary [&>li:nth-child(1)>a>svg]:text-primary
                [&>li:nth-child(2)>a]:text-primary [&>li:nth-child(2)>a>svg]:text-primary
              " />
            -->
        </div>
    </div>
</template>

<script lang="ts" setup>
import type { NavigationMenuItem } from '@nuxt/ui'

const route = useRoute();

const navigationItems = computed<NavigationMenuItem[]>(() => baseHeaderContent.map(markPageWhenChildActive));

function markPageWhenChildActive(navItem: NavigationMenuItem): NavigationMenuItem {
  if (navItem.children !== undefined) {
    const currentPath = route.path;
    const activeChildIndex = navItem.children.findIndex(c => c.to === currentPath);
    
    return {
      ...navItem,
      active: activeChildIndex !== -1,
      ui: activeChildIndex !== -1 ? { childList: `[&>li:nth-child(${activeChildIndex + 1})>a]:text-primary [&>li:nth-child(${activeChildIndex + 1})>a>svg]:text-primary` } : {}
    } satisfies NavigationMenuItem;
  }

  return navItem;
}

const baseHeaderContent: NavigationMenuItem[] = [
  {
    label: 'Home',
    icon: 'lucide:home',
    to: '/',
  },
  {
    label: 'Metrics',
    icon: 'lucide:chart-column',
    to: '/metrics'
  },
  {
    label: 'Docs',
    icon: 'lucide:book',
    children: [
      {
        icon: 'lucide:book-user',
        label: "Guide",
        to: '/docs/get-started'
      },
      {
        icon: 'lucide:boxes',
        label: "API Reference",
        to: '/docs/api'
      }
    ]
  },
  {
    label: 'Playground',
    icon: 'lucide:send',
    to: '/playground'
  },
  {
    label: 'Configuration',
    icon: 'lucide:settings',
    to: '/config'
  }
];
</script>

<style scoped>
.header-container {
  backdrop-filter: blur(5px);
  border-bottom: 1px var(--ui-bg-muted) solid;
  background: color-mix(in oklch increasing hue, var(--ui-bg) 50%, rgba(57, 57, 57, 0) 50%)
}
</style>