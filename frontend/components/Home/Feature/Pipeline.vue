<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold flex flex-row gap-2 justify-start items-center">
                    AI Powered Pipeline <UBadge label="Coming Soon" />
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
import type { FlaggedUser } from '~/assets/types/flaggedUsers';

const FlagsComponent = resolveComponent('UserFlags');

const mockData = reactive([
  {
    id: "3",
    username: "TechGuru",
    flags: ["slurs"],
    message: "You're all a bunch of worthless cunts."
  },
  {
    id: "6",
    username: "PixelArtist",
    flags: ["harassment"],
    message: "I hope you all choke on your own vomit."
  },
  {
    id: "7",
    username: "GamerPro",
    flags: ["slurs", "hate speech"],
    message: "Kill yourselves, fags!"
  },
  {
    id: "9",
    username: "DataDynamo",
    flags: ["spam", "harassment"],
    message: "Join my MLM scheme and get rich quick!"
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