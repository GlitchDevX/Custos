<template>
  <div class="p-4 flex gap-4 flex-col">
    <PageTitle>Endpoint Playground</PageTitle>
    <UAccordion :items="endpoints" :unmountOnHide="false">
      <template #mailValidation>
        <PlaygroundMailValidation />
      </template>
      <template #realtimeContent>
        <PlaygroundRealtimeContentCheck />
      </template>
      <template #pipelineCheck>
        <UAlert color="warning" title="Not implemented" icon="lucide-triangle-alert" />
      </template>
    </UAccordion>
  </div>
</template>

<script lang="ts" setup>
import type { AccordionItem } from '@nuxt/ui';
import { TITLE_SUFFIX } from '~/assets/data/appData';

useHead({
  title: 'Endpoint Playground' + TITLE_SUFFIX
})

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
    label: 'Pipeline Check',
    icon: 'lucide-workflow',
    slot: 'pipelineCheck'
  }
] as AccordionItem[];
</script>

<style>

</style>