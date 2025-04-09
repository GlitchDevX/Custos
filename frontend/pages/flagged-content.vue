<template>
  <div class="py-4 px-8 flex gap-4 flex-col">
    <PageTitle>
      Flagged Content Inbox
    </PageTitle>
    <UTable :data="data" :columns="columns" :loading="loading" />
    <UCard>
      <div class="flex gap-2 items-center">
        <h2 class="text-2xl font-bold" >
          Pipeline Status
        </h2>
        <UBadge v-if="status.active" label="Active" icon="lucide-circle-dot" color="success" />
        <UBadge v-else label="Inactive" icon="lucide-circle-dot" color="error" />
      </div>
      
      <UProgress v-model="status.processed" :max="status.total" class="mt-4" />
      
      <span class="text-2xl font-bold mt-8">
        {{ status.processed }} / {{ status.total }}
      </span>
    </UCard>
  </div>
</template>

<script lang="ts" setup>
import type { TableColumn } from '@nuxt/ui';
import { TITLE_SUFFIX } from '~/assets/data/appData';
import { FLAGGED_CONTENT_PATH, PIPELINE_PATH } from '~/assets/ts/backendConnector';
import type { FlaggedUser as FlaggedContent } from '~/assets/types/flaggedContent';

onMounted(() => {
  loadData();
});


const status = reactive({
	active: false,
	total: 0,
	processed: 0,
	ratio: 0.0
});
async function loadStatus() {
  status = await $fetch<any>(PIPELINE_PATH);
}

onMounted(() => {
  loadStatus();
})

const data = ref<FlaggedContent[]>([]);
const loading = ref(true);
async function loadData() {
  loading.value = true;

  const result = await $fetch<FlaggedContent[]>(FLAGGED_CONTENT_PATH);  
  data.value = result;
  
  loading.value = false;
}

const FlagsComponent = resolveComponent('UserFlags');
const columns = [
  {
    accessorKey: 'reportId',
    header: 'Report Id'
  },
  {
    accessorKey: 'userId',
    header: 'User Id'
  },
  {
    accessorKey: 'flags',
    header: 'Flags',
    cell: ({ row }) =>  {
      const flags = row.getValue<string[]>('flags');
      return h(FlagsComponent, { flags: flags });
    }
  },
  {
    accessorKey: 'content',
    header: 'Content'
  }
] as TableColumn<FlaggedContent>[]

useHead({
  title: 'Flagged Users Inbox' + TITLE_SUFFIX
});
</script>

<style>

</style>