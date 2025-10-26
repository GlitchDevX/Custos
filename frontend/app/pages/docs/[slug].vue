<template>
  <UContainer class="min-h-[calc(100dvh-64px)] flex flex-col px-4 sm:px-6 lg:px-8">
    <UPage class="grow">
      <template #left>
        <UPageAside>
          <span class="text-lg font-bold">Pages</span>
          <UContentNavigation v-if="allPages" :navigation="allPages" :collapsible="false" highlight class="pt-2" />
        </UPageAside>
      </template>

      <template #default>
        <UPageHeader v-bind="page">
          <template #headline>
            <UBreadcrumb :items="breadcrumb" />
          </template>
        </UPageHeader>

        <ContentRenderer v-if="page" :value="page.body" :prose="true" class="mt-8" />
      </template>

      <template #right>
        <UContentToc :links="page?.body.toc?.links" highlight />
      </template>
    </UPage>
    <HomeFooter class="mt-4" />
  </UContainer>
</template>

<script lang="ts" setup>
import type { ContentNavigationItem } from '@nuxt/content';
import { findPageBreadcrumb } from '@nuxt/content/utils';
import type { BreadcrumbItem } from '@nuxt/ui';
import { capitalize } from 'vue';
import { TITLE_SUFFIX } from '~/assets/data/appData';

const route = useRoute();
findPageBreadcrumb()


const { data: page } = await useAsyncData(route.path, () => queryCollection('docs').path(route.path).first());

const { data: allPages } = await useAsyncData(async () => {
  const allDocsPages = await queryCollection('docs').all()
  const allNav = allDocsPages.map(d => {
    const nav = d.navigation;

    if (nav === undefined || typeof nav === 'boolean') {
      return undefined;
    }

    return {
      title: nav.title,
      icon: nav.icon,
      path: d.path,
    } satisfies ContentNavigationItem
  }).filter(x => x !== undefined);
  return allNav;
});

const breadcrumb = computed<BreadcrumbItem[]>(() => 
  route.path.split("/")
    .filter(x => x !== "")
    .map((label) => {
      
      return {
        label: label
          .substring(label.indexOf("-") + 1) // remove number prefix
          .split("-")
          .map(capitalize)
          .join(" ")
      };
    })
);

useSeoMeta({
  title: page.value?.title + ' Documentation' + TITLE_SUFFIX,
  description: page.value?.description
})
</script>

<style scoped>
body {
  --ui-header-heigt: calc(var(--spacing)*16);
}
</style>