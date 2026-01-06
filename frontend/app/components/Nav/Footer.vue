<template>
  <div v-if="runtimeConfig.public.promoMode">
    <USeparator class="w-full" />
    <UFooter>
      <template #left>
        <UNavigationMenu
          :items="legalLinks"
          variant="link"
          :ui="{
            item: 'p-0'
          }"
        />
      </template>

      <template #default>
        <span class="text-dimmed">
          Made with ☕ by
          <ULink to="https://glitchdev.me" target="_blank" >GlitchDev</ULink>
        </span>
      </template>

      <template #right>
        <UButton 
          variant="soft"
          color="neutral"
          icon="lucide:github"
          to="https://github.com/GlitchDevX/custos"
          target="_blank"
        />
        <UButton 
          variant="soft"
          color="neutral"
          icon="lucide:container"
          to="https://hub.docker.com/repository/docker/glitchdevx/custos/general"
          target="_blank"
        />
      </template>
    </UFooter>
  </div>
  <div v-else class="mt-4"/>
</template>

<script lang="ts" setup>
import type { NavigationMenuItem } from '@nuxt/ui';

const runtimeConfig = useRuntimeConfig()

const legalLinks: NavigationMenuItem[] = [
  {
    label: "Legal Notice",
    to: "/legal-notice"
  },
  {
    label: "Privacy Policy",
    to: "/privacy-policy"
  }
]
</script>

<style></style>