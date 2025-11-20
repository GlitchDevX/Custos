<template>
    <div class="w-full h-16">
        <div class="flex flex-row justify-between align-middle px-2 fixed header-container z-1001  w-full">
            <div class="flex flex-row items-center gap-1">
              <UButton variant="ghost" href="/" size="md" icon="ci:custos-logo" class="my-2 text-2xl font-bold">
                Custos
              </UButton>
              <UBadge
                v-if="runtimeConfig.public.promoMode"
                variant="outline"
                :label="runtimeConfig.public.version"
                class="mt-1"/>
            </div>

            <div class="flex flex-row items-center gap-2">
              <GitHubStarButton v-if="runtimeConfig.public.promoMode" />
              <UNavigationMenu :items="navigationItems" />
            </div>
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
const runtimeConfig = useRuntimeConfig();

const navigationItems = computed<NavigationMenuItem[]>(() => baseHeaderContent.map(markPageWhenChildActive));

function markPageWhenChildActive(navItem: NavigationMenuItem): NavigationMenuItem {
  if (navItem.children !== undefined) {
    const currentPath = route.path;
    const activeChildIndex = navItem.children.findIndex(c => currentPath.startsWith(c.to));
    
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
    label: 'Docs',
    icon: 'lucide:book',
    exact: false,
    children: [
      {
        icon: 'lucide:boxes',
        label: "API Reference",
        to: '/api',
        prefetch: false, // prevent scalar loading css on other pages 
      },  
      {
        icon: 'lucide:book-user',
        label: "Guide",
        to: '/docs'
      }
    ]
  },
  {
    label: 'Playground',
    icon: 'lucide:send',
    to: '/playground'
  },
  ...runtimeConfig.public.promoMode ? [] : [{
    label: 'Configuration',
    icon: 'lucide:settings',
    to: '/config'
  }]
];
</script>

<style scoped>
.header-container {
  backdrop-filter: blur(5px);
  border-bottom: 1px var(--ui-bg-muted) solid;
  background: color-mix(in oklch increasing hue, var(--ui-bg) 50%, rgba(57, 57, 57, 0) 50%)
}
</style>