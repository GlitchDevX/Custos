<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl max-w-full">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold flex flex-row gap-2 justify-start items-center">
                    AI Powered Analysis
                </h2>
                <p class="muted-text">
                    Deep content checks utilizing a neuronal network built to flag user-content with a profound understanding.
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
    flags: ["obscene", "insult", "toxicity"],
    content: "You're all a bunch of worthless cunts.",
  },
  {
    flags: ["toxicity", "obscene", "sexual_explicit"],
    content: "I hope you all choke on your own cum.",
  },
  {
    flags: ["insult", "threat", "toxicity"],
    content: "Kill yourselves, fags!",
  },
  {
    flags: ["toxicity"],
    content: "Hahaha d@mb b!tch",
  },
] as FlaggedContent[]);

const FlagsComponent = resolveComponent('ContentFlag');
const columns = [
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