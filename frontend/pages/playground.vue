<template>
  <div class="py-4 px-8 flex gap-4 flex-col">
    <PageTitle>Endpoint Playground</PageTitle>
    <UAccordion v-model="active" :items="endpoints" :unmountOnHide="false">
      <template #mailValidation>
        <PlaygroundMailValidation />
      </template>
      <template #realtimeContent>
        <PlaygroundRealtimeContentCheck />
      </template>
      <template #deepCheck>
        <PlaygroundDeepContentCheck />
      </template>
      <template #pipeline>
        <PlaygroundPipeline />
      </template>
    </UAccordion>
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
    label: 'Deep Content Check',
    icon: 'lucide-brain-circuit',
    slot: 'deepCheck'
  },
  {
    label: 'Pipeline Interaction',
    icon: 'lucide-workflow',
    slot: 'pipeline'
  }
] as AccordionItem[];
</script>

<style>

</style>