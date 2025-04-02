<template>
  <div class="p-4 flex gap-4 flex-col">
    <MetricsBigNumber :zahl="12"/>
  </div>
</template>

<script lang="ts" setup>
import { TITLE_SUFFIX } from '~/assets/data/appData';

useHead({
  title: 'Monitoring Dashboard' + TITLE_SUFFIX
})
</script>

<style>

</style>