<template>
  <div class="py-4 px-8 flex gap-4 flex-col relative">
    <PageTitle>
      Flagged Content Inbox
    </PageTitle>
    <div class="">
      <UTable :data="data" :columns="columns" :loading="loading" class="mb-48"/>
    </div>
    <div class="relative w-full">
      <PipelineStatus class="fixed z-10 left-[2rem] bottom-[2rem]" style="width: calc(100% - 4rem)" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import type { TableColumn } from '@nuxt/ui';
import { TITLE_SUFFIX } from '~/assets/data/appData';
import { FLAGGED_CONTENT_PATH } from '~/assets/ts/backendConnector';
import type { FlaggedUser as FlaggedContent } from '~/assets/types/flaggedContent';

onMounted(() => {
  loadData();
});

const data = ref<FlaggedContent[]>([]);
const loading = ref(true);
async function loadData() {
  loading.value = true;

  const result = await $fetch<FlaggedContent[]>(FLAGGED_CONTENT_PATH);  
  data.value = result;
  
  loading.value = false;
}

const FlagsComponent = resolveComponent('PipelineContentFlags');
const CheckboxComponent = resolveComponent('UCheckbox');
const columns = [
  {
    accessorKey: 'reportId',
    header: 'Report Id',
    meta: {
      class: {
        th: 'max-w-20',
        td: 'max-w-20 truncate'
      }
    }
  },
  {
    accessorKey: 'userId',
    header: 'User Id',
    meta: {
      class: {
        th: 'max-w-20',
        td: 'max-w-20 truncate'
      }
    }
  },
  {
    accessorKey: 'falseReport',
    header: 'False Report',
    cell: ({ row }) => {
      return h(CheckboxComponent, { modelValue: row.getValue<boolean>('falseReport'), class: 'pointer-events-none' })
    },
    meta: {
      class: {
        th: 'max-w-18',
        td: 'max-w-18 truncate'
      }
    }
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
  },
  {
    accessorKey: 'reportedAt',
    header: 'Reported At',
    meta: {
      class: {
        th: 'max-w-24',
        td: 'max-w-24 truncate'
      }
    }
  }
] as TableColumn<FlaggedContent>[]

useHead({
  title: 'Flagged Users Inbox' + TITLE_SUFFIX
});
</script>

<style>

</style>