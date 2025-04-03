<template>
  <div class="p-4 flex gap-4 flex-col">
    <UCard>
      <h2 class="text-2xl font-bold mb-4">
        Flagged User Inbox
      </h2>
      <UTable :data="mockData" :columns="columns" />
    </UCard>
  </div>
</template>

<script lang="ts" setup>
import type { TableColumn } from '@nuxt/ui';
import { TITLE_SUFFIX } from '~/assets/data/appData';
import type { FlaggedUser } from '~/assets/types/flaggedUsers';

const FlagsComponent = resolveComponent('UserFlags');

const mockData = reactive([
  {
    id: "1",
    username: "GlitchDev",
    flags: ['slurs'],
    message: "Fuck you!"
  },
  {
    id: "2",
    username: "CodeNinja",
    flags: ["spam", "harassment"],
    message: "This shit is rigged!"
  },
  {
    id: "3",
    username: "TechGuru",
    flags: ["slurs"],
    message: "You're all a bunch of worthless cunts."
  },
  {
    id: "4",
    username: "User123",
    flags: ["hate speech", "misinformation"],
    message: "I'm telling you, vaccines are poison!"
  },
  {
    id: "5",
    username: "DevMaster",
    flags: ["spam"],
    message: "DMCA takedown notice sent!"
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
    id: "8",
    username: "WebWizard",
    flags: ["misinformation"],
    message: "Bitcoin is the only future, don't listen to the haters."
  },
  {
    id: "9",
    username: "DataDynamo",
    flags: ["spam", "harassment"],
    message: "Join my MLM scheme and get rich quick!"
  },
  {
    id: "10",
    username: "CryptoQueen",
    flags: ["scams"],
    message: "Invest in this coin, it's going to the moon!"
  },
  {
    id: "11",
    username: "DesignDiva",
    flags: ["slurs"],
    message: "You're all ugly and talentless."
  },
  {
    id: "12",
    username: "MarketingMaven",
    flags: ["misinformation", "spam"],
    message: "Click here to get a free iPhone!"
  },
  {
    id: "13",
    username: "AIWhiz",
    flags: ["hate speech"],
    message: "Humans are inferior and deserve to be eradicated."
  },
  {
    id: "14",
    username: "GameChanger",
    flags: ["harassment", "slurs"],
    message: "Go kill yourselves, you pathetic losers."
  },
  {
    id: "15",
    username: "CodeCrafter",
    flags: ["spam"],
    message: "Anyone else having trouble with the forum?"
  }
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

useHead({
  title: 'Flagged Users Inbox' + TITLE_SUFFIX
});
</script>

<style>

</style>