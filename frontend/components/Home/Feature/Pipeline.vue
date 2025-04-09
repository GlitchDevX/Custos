<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold flex flex-row gap-2 justify-start items-center">
                    AI Powered Pipeline
                </h2>
                <p class="muted-text">
                    Deep content checks utilizing a combination of flexible LLMs and concrete rulesets to flag user-content.
                </p>
            </div>
            <UTable :data="mockData" :columns="columns" />
        </div>
    </div>
</template>

<script lang="ts" setup>
import type { TableColumn } from '@nuxt/ui';
import type { FlaggedUser } from '~/assets/types/flaggedContent';

const FlagsComponent = resolveComponent('PipelineContentFlags');

const mockData = reactive([
  {
    reportId: "3",
    userId: "TechGuru",
    flags: ["slurs"],
    content: "You're all a bunch of worthless cunts.",
  },
  {
    reportId: "6",
    userId: "PixelArtist",
    flags: ["harassment"],
    content: "I hope you all choke on your own vomit.",
  },
  {
    reportId: "7",
    userId: "GamerPro",
    flags: ["slurs", "hate speech"],
    content: "Kill yourselves, fags!",
  },
  {
    reportId: "9",
    userId: "DataDynamo",
    flags: ["spam", "harassment"],
    content: "Join my MLM scheme and get rich quick!",
  },
] as FlaggedUser[]);

const columns = [
  {
    accessorKey: 'id',
    header: 'Id'
  },
  {
    accessorKey: 'username',
    header: 'Username'
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
    accessorKey: 'message',
    header: 'Message'
  }
] as TableColumn<FlaggedUser>[]


</script>

<style>

</style>