<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold flex flex-row gap-2 justify-start items-center">
                    AI Powered Pipeline
                </h2>
                <p class="muted-text">
                    Deep content checks utilizing an LLM to flag user-content with a profound understanding.
                </p>
            </div>
            <UTable :data="mockData" :columns="columns" />
        </div>
    </div>
</template>

<script lang="ts" setup>
import type { TableColumn } from '@nuxt/ui';
import type { FlaggedContent } from '~/assets/types/flaggedContent';

const mockData = reactive([
  {
    userId: "TechGuru",
    falseReport: false,
    flags: ["profanity"],
    content: "You're all a bunch of worthless cunts.",
  },
  {
    userId: "PixelArtist",
    falseReport: false,
    flags: ["harassment"],
    content: "I hope you all choke on your own vomit.",
  },
  {
    userId: "GamerPro",
    falseReport: false,
    flags: ["profanity", "harassment"],
    content: "Kill yourselves, fags!",
  },
  {
    userId: "DataDynamo",
    falseReport: false,
    flags: ["spam", "misinformation"],
    content: "Join my MLM scheme and get rich quick!",
  },
] as FlaggedContent[]);

const FlagsComponent = resolveComponent('PipelineContentFlags');
const CheckboxComponent = resolveComponent('UCheckbox');
const columns = [
  {
    accessorKey: 'userId',
    header: 'User Id',
    meta: { class: { th: 'max-w-28', td: 'max-w-28 truncate' } }
  },
  {
    accessorKey: 'falseReport',
    header: 'False Report',
    cell: ({ row }) => {
      return h(CheckboxComponent, { modelValue: row.getValue<boolean>('falseReport'), class: 'pointer-events-none' })
    },
    meta: { class: { th: 'max-w-18', td: 'max-w-18 truncate' } }
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
] as TableColumn<FlaggedContent>[]



</script>

<style>

</style>