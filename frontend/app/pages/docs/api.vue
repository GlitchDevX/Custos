<template>
  <div class="mt-0 sm:-mt-16">
    <ClientOnly>
      <ScalarApiReference :configuration="scalarConfig" />
    </ClientOnly>
  </div>
</template>

<script lang="ts" setup>
import { TITLE_SUFFIX } from '~/assets/data/appData';

useHead({
  title: "API Reference" + TITLE_SUFFIX
});

const scalarConfig = {
  spec: {
    defaultOpenAllTags: true,
    url: '/swagger.json',
    baseServerURL: 'http://localhost:3060',
    hideDarkModeToggle: true,
    showToolbar: "never",
  }
}
</script>

<style>
.dark-mode {
  --scalar-background-1: var(--ui-bg);
  --scalar-background-2: var(--ui-bg-elevated);
  --scalar-background-3: var(--ui-bg-muted);
  --scalar-color-1: var(--ui-text);
  --scalar-color-2: var(--ui-text-toned);
  --scalar-color-3: var(--ui-text-muted);
  --scalar-color-accent: var(--ui-primary);
  --scalar-background-accent: var(--ui-bg-accented);
  --scalar-border-color: var(--ui-border);

  --scalar-header-height: calc(var(--spacing)*16);
}
</style>