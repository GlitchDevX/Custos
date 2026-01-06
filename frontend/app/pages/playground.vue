<template>
  <div class="px-8 flex flex-col justify-between min-h-[calc(100dvh-64px)]">
    <div class="py-4 flex gap-4 flex-col">
      <PageTitle>Endpoint Playground</PageTitle>
      <UAccordion v-model="active" :items="endpoints" :unmountOnHide="false">
        <template #mailValidation>
          <PlaygroundMailValidation />
        </template>
        <template #realtimeContent>
          <PlaygroundRealtimeContentCheck />
        </template>
        <template #deepAnalysis>
          <PlaygroundDeepAnalysis />
        </template>
      </UAccordion>
    </div>
    
    <NavFooter />
  </div>
</template>

<script lang="ts" setup>
import type { AccordionItem } from '@nuxt/ui';
import { TITLE_SUFFIX } from '~/assets/data/appData';

useHead({
  title: 'Endpoint Playground' + TITLE_SUFFIX
});

const active = ref('0');
const endpoints = [
  {
    label: 'Mail Validation',
    icon: 'lucide-mail',
    slot: 'mailValidation'
  },
  {
    label: 'Realtime Content Check',
    icon: 'lucide-clock',
    slot: 'realtimeContent'
  },
  {
    label: 'Deep Content Analysis',
    icon: 'lucide-brain-circuit',
    slot: 'deepAnalysis'
  }
] as AccordionItem[];
</script>

<style>

</style>