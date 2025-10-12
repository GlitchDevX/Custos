<template>
  <UPage>
    <template #left>
      <UPageAside>
          <span>Test Content</span>
      </UPageAside>
    </template>

    <template #default>
      <UPageHeader>
        <template #headline>
          <UBreadcrumb :items="breadcrumb" />
        </template>
      </UPageHeader>

      <ContentRenderer v-if="page" :value="page" />
    </template>
  </UPage>
</template>

<script lang="ts" setup>
import { findPageBreadcrumb } from '@nuxt/content/utils';
import type { BreadcrumbItem } from '@nuxt/ui';
import { capitalize } from 'vue';

const route = useRoute();
findPageBreadcrumb()


const { data: page } = await useAsyncData(route.path, () => queryCollection('docs').path(route.path).first());

const breadcrumb = computed<BreadcrumbItem[]>(() => 
  route.path.split("/")
    .filter(x => x !== "")
    .map((label) => {
      return {
        label: label.split("-").map(capitalize).join(" ")
      };
    })
);

</script>

<style>

</style>