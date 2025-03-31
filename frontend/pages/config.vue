<template>
  <div class="p-4 flex gap-4 flex-col">
    <UTabs :items="items">
      <template #mailValidation>
        <ConfigMailValidation />
      </template>
      <template #realtimeCheck>
        <ConfigRealtime />
      </template>
      <template #pipelineCheck>
        <ConfigPipeline />
      </template>
    </UTabs>
  </div>
</template>

<script lang="ts" setup>
import type { TabsItem } from '@nuxt/ui'

const items: TabsItem[] = [
  {
    label: 'Mail Validation',
    icon: 'lucide-mail',
    slot: 'mailValidation'
  },
  {
    label: 'Realtime Content Check',
    icon: 'lucide-clock',
    slot: 'realtimeCheck'
  },
  {
    label: 'Reported Pipeline Check',
    icon: 'lucide-workflow',
    slot: 'pipelineCheck'
  }
]
</script>

<style>

</style>