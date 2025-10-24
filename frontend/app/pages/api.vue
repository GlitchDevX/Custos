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

const scalarConfig = {
  content: swaggerFile,
  telemetry: false,
  defaultOpenAllTags: true,
  baseServerURL: 'http://localhost:3060',
  hideDarkModeToggle: true,
  hideClientButton: true,
  showToolbar: "never",
  customCss: 'body { background: var(--scalar-background-1); }'
} satisfies AnyApiReferenceConfiguration;
</script>

<style>

</style>