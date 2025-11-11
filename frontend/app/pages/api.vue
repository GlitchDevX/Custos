<template>
  <div class="mt-0 sm:-mt-16">
    <ApiReference :configuration="scalarConfig" />
  </div>
</template>

<script lang="ts" setup>
import { ApiReference } from '@scalar/api-reference';
import type { AnyApiReferenceConfiguration } from '@scalar/types';
import { TITLE_SUFFIX } from '~/assets/data/appData';
import swaggerFile from '../../public/swagger.json';

useHead({
  title: "API Reference" + TITLE_SUFFIX
});

const runtimeConfig = useRuntimeConfig();

const scalarConfig = {
  ... runtimeConfig.public.docsDev ? {
    url: 'http://localhost:3060/swagger.json',
  } : {
    content: swaggerFile,
  },
  telemetry: false,
  defaultOpenAllTags: true,
  baseServerURL: 'http://localhost:3060',
  hideDarkModeToggle: true,
  hideClientButton: true,
  showToolbar: "never",
  customCss: 'body { background: var(--scalar-background-1); }' // fallback when scalar is loaded on pages other then /api
} satisfies AnyApiReferenceConfiguration;
</script>

<style>
.dark-mode, .light-mode {
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